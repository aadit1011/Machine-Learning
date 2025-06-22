# custom_ensemble.py
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin

class CustomEnsemble(BaseEstimator, ClassifierMixin):
    def __init__(self, models, column_sets, full_columns):
        self.models = models
        self.column_sets = column_sets
        self.full_columns = full_columns
    
    def predict(self, X):
        if isinstance(X, dict):
            X = pd.DataFrame([X])
        X = X[self.full_columns]
        
        predictions = []
        for model, cols in zip(self.models, self.column_sets):
            if cols is not None:
                X_sub = X[cols]
            else:
                X_sub = X
            pred = model.predict(X_sub)
            predictions.append(pred)
        
        pred_matrix = np.vstack(predictions).T
        final_pred = []
        for row in pred_matrix:
            male_votes = np.sum(row == 1)
            female_votes = np.sum(row == 0)
            final_pred.append(1 if male_votes > female_votes else 0)
        
        return np.array(final_pred)
    
    def predict_proba(self, X):
        if isinstance(X, dict):
            X = pd.DataFrame([X])
        X = X[self.full_columns]
        
        probas = []
        for model, cols in zip(self.models, self.column_sets):
            if cols is not None:
                X_sub = X[cols]
            else:
                X_sub = X
            probas.append(model.predict_proba(X_sub))
        
        return np.mean(probas, axis=0)