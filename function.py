def display_min_max(numbers):
    if not numbers:
        print(None)
    else:
        numbers_sorted = sorted(numbers)
        max_value = numbers_sorted[-1]  # Last item in the sorted list is the max value
        min_value = numbers_sorted[0]   # First item in the sorted list is the min value
        print(max_value, min_value)

# Main List of numbers
Numbers_A = [3, 4, 5, 6]
Numbers_B = [-1, -2, -3, -4]
Numbers_C = [0, 0, 0, 0]
Numbers_empty = []

# Display the output automatically
print("Numbers_A:")
display_min_max(Numbers_A)

print("\nNumbers_B:")
display_min_max(Numbers_B)

print("\nNumbers_C:")
display_min_max(Numbers_C)

print("\nNumbers_empty:")
display_min_max(Numbers_empty)
