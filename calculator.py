import calc_art
import math

# Define mathematical functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error! Division by zero."

def power(n1, n2):
    return n1 ** n2

def modulo(n1, n2):
    return n1 % n2

def sqrt(n1, n2=None):
    return math.sqrt(n1)

# Dictionary to store operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": modulo,
    "√": sqrt,
}

# List to store calculation history
history = []

# Calculator function
def calculator():
    global history
    print(calc_art.logo)
    should_continue = True
    num1 = float(input("What is the first number?: "))

    while should_continue:
        for symbol in operations:
            if symbol != "√":
                print(symbol)
            if symbol == "√":
                print("& (√)")

        operation_symbol = input("Pick an operation: ")
        if operation_symbol in operations and operation_symbol != "√":
            num2 = float(input("What is the next number?: "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            history.append(f"{num1} {operation_symbol} {num2} = {answer}")
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        elif operation_symbol == "&":
            calculation_function = operations["√"]
            answer = calculation_function(num1)
            history.append(f"√{num1} = {answer}")
            print(f"√{num1} = {answer}")
        else:
            print("Invalid operation. Please try again.")
            continue

        choice = input(f"Type 'y' to continue calculating with {answer}, "
                       f"'n' to start a new calculation, or 'h' to view history: ").lower()
        if choice == "y":
            num1 = answer
        elif choice == "h":
            print("\nCalculation History:")
            # for record in history:
            #     print(record)
            for i in range(len(history)):
                print(f"{i + 1}: {history[i]}")
            choice = input(f"\nType 'y' to continue calculating with {answer}, "
                           f"'n' to start a new calculation, or 'd' to delete history: ").lower()
            if choice == "y":
                num1 = answer
            elif choice == "d":
                print("\nCalculation History:")
                history = []
                input(f"\nPress enter to start a new calculation...").lower()
                should_continue = False
                print("\n" * 100)
                calculator()
            else:
                should_continue = False
                print("\n" * 100)
                calculator()
        else:
            should_continue = False
            print("\n" * 100)
            calculator()

# Run the calculator
calculator()