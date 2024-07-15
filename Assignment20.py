def print_dict_items(dict_num):
    print("key  value")
    for key, value in dict_num.items():
        print(f"{key:<5}{value}")

# Example dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Call the function to print key-value pairs
print_dict_items(dict_num)
