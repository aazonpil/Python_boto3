def print_min_max(numbers):
    if numbers:  # Check if the list is not empty
        # Find the smallest and highest number
        smallest_number = min(numbers)
        highest_number = max(numbers)
        print(highest_number,  smallest_number)
    else:
        print(None)

# List of numbers
Numbers_A = [3, 4, 5, 6]
Numbers_B = [-1, -2, -3, -4]
Numbers_C = [0, 0, 0, 0]
Numbers_empty = []

# Automatically print the minimum and maximum for each list
print("Numbers_A:")
print_min_max(Numbers_A)

print("\nNumbers_B:")
print_min_max(Numbers_B)

print("\nNumbers_C:")
print_min_max(Numbers_C)

print("\nNumbers_empty:")
print_min_max(Numbers_empty)
