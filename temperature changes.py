import matplotlib.pyplot as plt

# Days and new temperature data
days = list(range(1, 32))
new_temperature = [60, 62, 65, 66, 67, 69, 70, 72, 74, 76, 75, 73, 70, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51]

# Creating the line chart
plt.figure(figsize=(12, 6))
plt.plot(days, new_temperature, marker='o', linestyle='-', color='b')

# Set the labels and title
plt.xlabel('Days')  # Label for x-axis
plt.ylabel('Temperature (°F)')  # Label for y-axis
plt.title('Daily Temperature Changes Over Time in a City')  # Title of the chart

# Add grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Display the chart
plt.show()
