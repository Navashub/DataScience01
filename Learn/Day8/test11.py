def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"
    
operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

def calculator():
    num1 = float(input("Enter the first number: "))

    print("Available operations: ")
    for symbol in operations.keys():
        print(symbol, end=' ')
    print()

    should_continue = True
    while should_continue:
        operation = input("Choose an operation symbol: ")
        num2 = float(input("Enter the second number: "))

        calculation_function = operations.get(operation)
        if calculation_function:
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation} {num2} = {answer}")

            choice = input("Do you want to continue with this result? (yes/no): ")
            if choice.lower() == 'yes':
                num1 = answer
            else:
                should_continue = False
calculator()
