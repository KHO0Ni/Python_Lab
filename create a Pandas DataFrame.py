import pandas as pd  # Import the Pandas library for data manipulation

# Define the sample data as a dictionary
data = {
    'Science': [88, 92, 79, 85, 90],      # Science scores
    'History': [75, 89, 94, 85, 82],      # History scores
    'Geography': [82, 78, 88, 91, 85]     # Geography scores
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

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