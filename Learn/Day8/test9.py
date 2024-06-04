
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply
}

def calculator():
    print('Welcome to our calculator')

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        num1 = float(input('Enter first number?: '))
        operation_type = input("Pick an operation above: ")
        num2 = float(input('Enter the second number: '))

        calculation_function = operations[operation_type]
        answer = calculation_function(num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")


        continue_operation = input('Do you want to continue? Y or N: ')

        if continue_operation == 'Y':
            num1 = answer 

            num2 = float(input('Enter the second number: '))
            calculation_function = operations[operation_type]
            answer = calculation_function(num1, num2)

            print(f"{num1} {symbol} {num2} = {answer}")
            

    should_continue = False

    calculator()
        

calculator()