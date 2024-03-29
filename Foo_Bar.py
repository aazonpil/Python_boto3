"""A number is considered a multiple of another 
number if it can be divided evenly by that number
 meaning without leaving a remainder """

number = float(input("Enter the number:"))

if number >= 0 and number <= 50:
    if number % 5 == 0 and number % 7 == 0:  # Check for every multiple of both 5 and 7 first
        print("FooBar")
    elif number % 5 == 0:  # For every multiple of 5
        print("Foo")
    elif number % 7 == 0:  # For every multiple of 7
        print("Bar")
    else:
        print(None)  # If not a multiple of 5 or 7 within the range
else:
    print("Not applicable")  # If the number is not in the range 0 to 50

