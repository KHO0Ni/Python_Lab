import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame with student data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group by 'school_code' and calculate mean, min, and max of 'age'
age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Display the calculated statistics
print("Age statistics by school code:\n")
print(age_stats)

# Plot horizontal bar charts for mean, min, and max age for each school
fig, ax = plt.subplots(1, 3, figsize=(15, 8))  # Create a figure with 3 subplots

# Plot mean age
age_stats['mean'].plot(kind='barh', ax=ax[0], color='skyblue', edgecolor='black')
ax[0].set_title('Mean Age by School Code')
ax[0].set_xlabel('Mean Age')

# Plot min age
age_stats['min'].plot(kind='barh', ax=ax[1], color='lightgreen', edgecolor='black')
ax[1].set_title('Min Age by School Code')
ax[1].set_xlabel('Min Age')

# Plot max age
age_stats['max'].plot(kind='barh', ax=ax[2], color='salmon', edgecolor='black')
ax[2].set_title('Max Age by School Code')
ax[2].set_xlabel('Max Age')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the horizontal bar charts
plt.show()
'''
Output:
Age statistics by school code:

             mean  min  max
school_code
s001         12.5   12   13
s002         13.0   12   14
s003         13.0   13   13
s004         12.0   12   12
'''