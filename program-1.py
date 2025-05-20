# Define a Calculator c
class Calculator:
    # This function runs when a new Calculator object is created
    def __init__(math, a, b, operation):
        math.a = a  # first number
        math.b = b  # second number
        math.operation = operation.lower()  # convert operation to lowercase

    # This function performs the calculation
    def calculate(math):
        if math.operation == "add":
            return math.a + math.b
        elif math.operation == "subtract":
            return math.a - math.b
        elif math.operation == "multiply":
            return math.a * math.b
        elif math.operation == "divide":
            if math.b != 0:
                return math.a / math.b
            else:
                return "Cannot divide by zero"
        else:
            return "Unknown operation"

# Main program
# Ask user for input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add / subtract / multiply / divide): ")

# Create a Calculator object
calc = Calculator(a, b, operation)

# Get and print the result
result = calc.calculate()
print("Result:", result)
