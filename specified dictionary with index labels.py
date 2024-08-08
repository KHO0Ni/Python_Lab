import pandas as pd  # Import the Pandas library for data manipulation
import numpy as np  # Import NumPy for handling NaN values

# Define the sample dictionary data with index labels
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'score': [15.5, 18, 12.5, np.nan, 10, 19.5, 14, np.nan, 8.5, 17],
    'attempts': [1, 2, 1, 3, 2, 2, 1, 3, 2, 1],
    'qualify': ['yes', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes']
}

# Define the list of index labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create a DataFrame from the dictionary data with the specified index labels
df = pd.DataFrame(data, index=labels)

# Display the DataFrame
print(df)
'''
Output:
   Science  History  Geography
0       88       75         82
1       92       89         78
2       79       94         88
3       85       85         91
4       90       82         85
'''