



def find_min_max(numbers):
    if not numbers:  # Check if the list is empty
        return None, None  # Return None for both min and max if the list is empty
    return min(numbers), max(numbers)  # Return the min and max values directly
    
# List of numbers
Numbers_A = [3, 4, 5, 6]
Numbers_B = [-1, -2, -3, -4]
Numbers_C = [0, 0, 0, 0]
Numbers_empty = []


# Using the function and displaying the output
print("Numbers_A:", find_min_max(Numbers_A))
print("Numbers_B:", find_min_max(Numbers_B))
print("Numbers_C:", find_min_max(Numbers_C))
print("Numbers_empty:", find_min_max(Numbers_empty))
