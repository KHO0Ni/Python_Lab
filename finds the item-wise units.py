#Lab 2  finds the item-wise units

import pandas as pd
# Load the data from the given file path
file_path = r"D:\verma\2 Documents\Anudip\jupyter\salesdata.csv"
df = pd.read_csv(file_path)
# Create a pivot table to find item-wise units sold
pivot_table = pd.pivot_table(df, 
                             values='Units', 
                             index=['Item'], 
                             aggfunc='sum')

# Display the pivot table
print(pivot_table)
''' output:
Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395
'''
