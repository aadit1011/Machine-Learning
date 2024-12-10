# Import the necessary libraries
from pandas_profiling import ProfileReport
import pandas as pd

# Example DataFrame
df = pd.read_csv('HR.csv')

# Create a profile report
prof = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

# Export the report to an HTML file
prof.to_file(output_file='output.html')
