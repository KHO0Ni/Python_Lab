import numpy as np

# Define the dataset
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Find hot days (temperature > 35°C)
hot_days = temperatures[temperatures > 35]

# Find cold days (temperature < 5°C)
cold_days = temperatures[temperatures < 5]

# Output the results
print("Hot days (temperature > 35°C):", hot_days)
print("Cold days (temperature < 5°C):", cold_days)
'''
Output:
PS C:\Users\verma> & C:/Users/verma/AppData/Local/Programs/Python/Python311/python.exe "d:/verma/2 Documents/Anudip/python/days with extreme temperature.py"
Hot days (temperature > 35°C): [36.8 38.7 37.2]
Cold days (temperature < 5°C): []
'''