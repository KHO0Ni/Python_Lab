import numpy as np

# Create arrays of zeros, ones, and fives
zeros = np.zeros(10)
ones = np.ones(10)
fives = np.full(10, 5)

# Concatenate the arrays
result = np.concatenate((zeros, ones, fives))

# Print the result
print("Array of 10 zeros, 10 ones, and 10 fives:")
print(result)

'''
output:
Array of 10 zeros, 10 ones, and 10 fives:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
'''