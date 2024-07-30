import matplotlib.pyplot as plt

# Categories and updated expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
new_expenses = [1000, 500, 300, 200, 150]

# Set the figure size for better readability
plt.figure(figsize=(10, 6))

# Create the bar chart
plt.bar(categories, new_expenses, color='lightcoral')

# Set the labels and title
plt.xlabel('Categories')  # Label for x-axis
plt.ylabel('Expenses ($)')  # Label for y-axis
plt.title('Monthly Expenses in Different Spending Categories (Updated)')  # Title of the chart

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.show()
