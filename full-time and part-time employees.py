import numpy as np

# Employee data for full-time employees
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
], dtype=object)  # Use dtype=object to handle mixed types

# Employee data for part-time employees
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
], dtype=object)  # Use dtype=object to handle mixed types

# Combine the datasets
combined_employees = np.vstack((full_time_employees, part_time_employees))

# Output the results
print("Combined Employee Dataset:")
print(combined_employees)
'''
Output:
PS C:\Users\verma> & C:/Users/verma/AppData/Local/Programs/Python/Python311/python.exe "d:/verma/2 Documents/Anudip/python/monthly sales data into quarterly reports.py"
Combined Employee Dataset:
[[101 'John Doe' 'Full-Time' 55000]
 [102 'Jane Smith' 'Full-Time' 60000]
 [103 'Mike Johnson' 'Full-Time' 52000]
 [201 'Alice Brown' 'Part-Time' 25000]
 [202 'Bob Wilson' 'Part-Time' 28000]
 [203 'Emily Davis' 'Part-Time' 22000]]'''