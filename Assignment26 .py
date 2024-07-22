import numpy as np  # Import the numpy library and alias it as np

# Define the list
my_list = [1, 2, 3, 4, 5]

# Convert the list to a NumPy array
my_array = np.array(my_list)

# Display the NumPy array
print("The NumPy array is:", my_array)

# Display the first and last index elements
print("The first element is:", my_array[0])
print("The last element is:", my_array[-1])

# Multiply each element by 2
multiplied_array = my_array * 2

# Display the result
print("The array with each element multiplied by 2 is:", multiplied_array)
'''
Output :
The NumPy array is: [1 2 3 4 5]
The first element is: 1
The last element is: 5
The array with each element multiplied by 2 is: [ 2  4  6  8 10]
'''