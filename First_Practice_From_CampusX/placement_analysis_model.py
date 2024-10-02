# Importing necessary libraries
import pandas as pd   # For data manipulation and analysis
import numpy as np    # For numerical computing
import matplotlib.pyplot as plt  # For data visualization

# Load dataset from a CSV file
df = pd.read_csv('placement.csv')

# Display the dataframe to check its contents
df

# ---------------- Data Preprocessing ----------------

# Dropping the first column (possibly index column) and keeping relevant data
df = df.iloc[:, 1:]

# Display the dataframe after column removal
df

# ---------------- Exploratory Data Analysis (EDA) ----------------

# Importing matplotlib again for plotting (although it's already imported)
import matplotlib.pyplot as plt 

# Creating a scatter plot to visualize the relationship between 'cgpa', 'iq', and 'placement'
# 'c' is used to color the points based on the 'placement' value (binary classification)
plt.scatter(df['cgpa'], df['iq'], c=df['placement'])

# ---------------- Feature and Label Selection ----------------

# Splitting the dataset into features (X) and target/labels (y)
# Features (X) are all columns except the last one, which is 'placement'
x = df.iloc[:, 0:-1]

# Labels (y) is the last column, which is 'placement'
y = df.iloc[:, -1]

# Display the feature set
x

# Display the labels
y

# ---------------- Splitting Data for Training and Testing ----------------

# Importing train_test_split to split the dataset into training and testing sets
from sklearn.model_selection import train_test_split

# Splitting the data into training (90%) and testing (10%) sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# Display the training features
x_train

# Display the testing features
x_test

# Display the testing labels
y_test

# Display the training labels
y_train

# ---------------- Data Standardization ----------------

# Importing StandardScaler to normalize the feature data
from sklearn.preprocessing import StandardScaler

# Creating an instance of StandardScaler
scaler = StandardScaler()

# Fitting the scaler on the training data and transforming it
x_train = scaler.fit_transform(x_train)

# Display the standardized training data
x_train

# Applying the same transformation to the test data
x_test = scaler.transform(x_test)

# Display the standardized testing data
x_test

# ---------------- Model Training Using Logistic Regression ----------------

# Importing Logistic Regression model
from sklearn.linear_model import LogisticRegression 

# Creating an instance of LogisticRegression
clf = LogisticRegression()

# Training (fitting) the model on the standardized training data
clf.fit(x_train, y_train)

# ---------------- Model Prediction ----------------

# Predicting the labels for the test dataset
y_pred = clf.predict(x_test)

# Display the true test labels
y_test

# ---------------- Model Accuracy Testing ----------------

# Importing accuracy_score to calculate the model's accuracy
from sklearn.metrics import accuracy_score

# Calculating the accuracy by comparing predicted and actual labels
accuracy_score(y_test, y_pred)

# ---------------- Decision Boundary Visualization ----------------

# Importing plot_decision_regions from mlxtend for decision boundary visualization
from mlxtend.plotting import plot_decision_regions

# Plotting the decision boundary for the training data
# 'legend=2' will display the legend in the plot
plot_decision_regions(x_train, y_train.values, clf=clf, legend=2)
