def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero is not allowed.")
        return None

# Main program starts here
number1 = float(input("Enter number1: "))
number2 = float(input("Enter number2: "))
operation = input("Choose the operation (add, subtract, multiply, divide): ")

# Performing the chosen operation

