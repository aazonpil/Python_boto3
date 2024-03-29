def reverse_digit_order(numbers):
    length = len(numbers)
    # Check if the number has only one digit outside the loop
    if length == 1:
        return numbers
    
    reverse_digit = []
    for i in range(length):
        forward_index = i
        negative_index = length - 1 - forward_index
        reverse_digit.append(numbers[negative_index])
    join_reversed = "".join(reverse_digit)
    return join_reversed

# Main
numbers_A = "1"
numbers_B = "123"
numbers_C = "3456"
numbers_D = "1111"
numbers_E = "2662" 

# Calling and printing the results
print("numbers_A:", reverse_digit_order(numbers_A))
print("numbers_B:", reverse_digit_order(numbers_B))
print("numbers_C:", reverse_digit_order(numbers_C))
print("numbers_D:", reverse_digit_order(numbers_D))
print("numbers_E:", reverse_digit_order(numbers_E))



