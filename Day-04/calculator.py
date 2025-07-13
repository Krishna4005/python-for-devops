def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"


if __name__ == "__main__":
    print("Simple Calculator")
    a = float(input("Enter first number: "))  # User inputs: 10
    b = float(input("Enter second number: "))  # User inputs: 5
    operation = input("Enter operation (+, -, *, /): ")  # User inputs: *

    result = calculator(a, b, operation)  # Function call: calculator(10.0, 5.0, '*')
    print(f"Result: {result}")  # Expected output: 50.0
