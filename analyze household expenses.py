import pandas as pd

# Input data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment', 'Healthcare', 'Education', 'Dining Out', 'Clothing', 'Miscellaneous']
expenses = [450, 220, 1300, 280, 160, 100, 200, 180, 90, 50]

# Creating a Pandas Series
expenses_series = pd.Series(expenses, index=categories)

# Displaying the Series
print(expenses_series)
'''
Output:
Groceries          450
Utilities          220
Rent              1300
Transportation     280
Entertainment      160
Healthcare         100
Education          200
Dining Out         180
Clothing            90
Miscellaneous       50
dtype: int64
'''