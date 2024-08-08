import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame with student data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group by 'class' and count the number of students in each class
class_counts = student_data['class'].value_counts()

# Display the counts for each class
print("Number of students in each class:\n")
print(class_counts)

# Generate a bar chart for the class counts
# The 'class_counts.plot' function creates a bar chart where:
# - 'kind' specifies the type of plot ('bar' for a bar chart)
# - 'color' sets the color of the bars
# - 'edgecolor' sets the color of the bar borders
class_counts.plot(kind='bar', color='skyblue', edgecolor='black')

# Add titles and labels to the chart for better readability
plt.title('Number of Students in Each Class')   # Title of the bar chart
plt.xlabel('Class')                            # Label for the x-axis
plt.ylabel('Number of Students')               # Label for the y-axis

# Display the bar chart
plt.show()
'''
Output:
Number of students in each class:

class
VI    4
V     2
Name: count, dtype: int64
'''