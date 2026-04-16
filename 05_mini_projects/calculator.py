print("================================")
print("       SIMPLE CALCULATOR")
print("================================\n")

# defining a function for addition
def add(*args):
    return sum(args)

# defining a function for subtraction
def subtract(*args):
    if len(args) == 2:
        return args[0] - args[1]
    else:
        return "Error: Subtraction requires exactly two arguments."

# defining a function for multiplication
def multiply(*args):
    if len(args) == 2:
        return args[0] * args[1]
    else:
        return "Error: Multiplication requires exactly two arguments."

# defining a function for division
def divide(*args):
    if len(args) == 2:
        if args[1] != 0:
            return args[0] / args[1]
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Division requires exactly two arguments."
    
# main function to run the calculator
def main():
    print("Welcome to the Simple Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    
    operation = input("Enter the operation you want to perform: ").lower()
    
    if operation in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    else:
        print("Error: Invalid operation. Please choose from add, subtract, multiply, or divide.")

if __name__ == "__main__":
    main()