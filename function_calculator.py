def calculator(number1, number2, operation):
    # Define nested functions for each operation
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

    # Determine and perform the operation
    if operation == 'add':
        return add(number1, number2)
    elif operation == 'subtract':
        return subtract(number1, number2)
    elif operation == 'multiply':
        return multiply(number1, number2)
    elif operation == 'divide':
        return divide(number1, number2)
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