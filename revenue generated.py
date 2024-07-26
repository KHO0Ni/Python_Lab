import numpy as np

# Input revenue arrays for two categories
category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])

# Calculate the total revenue by adding the two arrays element-wise
total_revenue = category1_revenue + category2_revenue

# Output the total revenue
print("Total Revenue:", total_revenue)
'''
Output:
Total Revenue: [ 950 1300 1500 1150]
'''