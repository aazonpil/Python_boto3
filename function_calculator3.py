def calculator(number1, number2, operation):

    # Addition operation
    if operation == 'add':
        return number1 + number2

    # Subtraction operation
    elif operation == 'subtract':
        return number1 - number2

    # Multiplication operation
    elif operation == 'multiply':
        return number1 * number2

    # Division operation
    elif operation == 'divide':
        if number2 != 0:
            return number1 / number2
        else:
            return "Error: Division by zero is not allowed."

    # Handle invalid operation input
    else:
        return "Invalid operation."

# Main program
number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
operation = input("Choose operation (add, divide, multiply, subtract): ")

# Calling the calculator function and storing the result
result = calculator(number1, number2, operation)

# Printing the result
print(f"The {operation} of {number1} and {number2} gives this result: {result}")
