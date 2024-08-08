import pandas as pd
import numpy as np

# Create the DataFrame with potential missing values (NaN)
df = pd.DataFrame({
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id': [5002, 5003, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5003, np.nan]
})

# Detect missing values in the DataFrame
# Returns a DataFrame of the same shape with True for missing values and False otherwise
missing_values = df.isnull()

# Display the DataFrame with missing value indicators
print("Missing Values Detection:\n")
print(missing_values)

# Provide a summary of missing values for each column
# Returns a Series with the count of missing values for each column
print("\nSummary of Missing Values:\n")
print(df.isnull().sum())
'''
Output:
   ord_no  purch_amt  ord_date  customer_id  salesman_id
0   False      False    False        False        False
1    True      False    False        False        False
2   False      False     True        False        False
3   False      False    False        False         True
4    True      False    False        False        False
5   False      False    False        False        False
6    True      False    False        False        False
7   False      False    False        False         True
8   False      False    False        False        False
9   False      False    False        False        False
10   True      False    False        False         True
11  False      False    False        False         True

Summary of Missing Values:
ord_no          3
purch_amt        0
ord_date         1
customer_id      0
salesman_id      3
dtype: int64

'''