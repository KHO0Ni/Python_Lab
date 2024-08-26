import numpy as np
from scipy.linalg import solve

# Coefficient matrix
A = np.array([[7, 2],
              [4, 5]])

# Right-hand side vector
B = np.array([8, 10])

# Solving for x and y
solution = solve(A, B)

print(solution)
'''
output:
[0.74074074 1.40740741]
'''