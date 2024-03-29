def print_digit_reverse_order(numbers_A,numbers_B,numbers_C,numbers_D, numbers_E):
    i=len(numbers)
    reverse_digit=[]
    while i>0:
        i -=1 
        reverse_digit.append(numbers[i])
    join_reversed= "".join(reverse_digit)
    return join_reversed

#Main
numbers_A="1"
numbers_B="123"
numbers_C="3456"
numbers_D="1111"
numbers_E="2662"

#calling


print("numbers_A:",print_digit_reverse_order (numbers_A))

print("numbers_B:",print_digit_reverse_order(numbers_B)) 

print("numbers_C:",print_digit_reverse_order(numbers_C)) 

print("numbers_D:",print_digit_reverse_order(numbers_D))

print("numbers_E:",print_digit_reverse_order(numbers_E))

if i==1: 
    print(numbers[i])
else:
    print print_digit_reverse_order(numbers_A,numbers_B,numbers_C,numbers_D, numbers_E):