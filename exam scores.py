import pandas as pd

# Input data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Creating a Pandas Series
scores_series = pd.Series(exam_scores, index=students)

# Displaying the Series
print(scores_series)
'''
Output:
Alice      92
Bob        88
Charlie    76
David      94
Eve        82
Frank      90
Grace      85
Hannah     89
Ivy        78
Jack       91
dtype: int64
'''