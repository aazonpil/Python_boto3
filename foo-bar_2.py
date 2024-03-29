def check_number(number):
    if 0 <= number <= 50:
        if number % 5 == 0 and number % 7 == 0:  # Check for multiple of both 5 and 7 first
            print("FooBar")
        elif number % 5 == 0:  # Then check for multiple of 5
            print("Foo")
        elif number % 7 == 0:  # Then check for multiple of 7
            print("Bar")
        else:
            print("Not applicable")
    else:
        print("Error")

# Use these numbers:
number1 = 10
number2 = 35
number3 = 42
number4 = 9
number5 =70

check_number(number1)
check_number(number2)
check_number(number3)
check_number(number4)
