def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


symbols = {
    '+':add,
    '-':substract,
    '*':multiply,
    '/':divide,
}


def calculator():
    num1 = int(input("Enter 1st number: "))

    for symbol in symbols:
        print(symbol)

    should_continue = 'y'

    while should_continue == 'y':
        operation = input("Pick an operation: ")
        next_number = int(input("What's the next number?: "))

        calculation_function = symbols[operation]

        answer = calculation_function(num1,next_number)

        print(f'{num1} {operation} {next_number} = {answer}')
        
        should_continue= input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation and 'e' to exit the calculation: ")
        
        if should_continue == 'y':
            num1 = answer
        elif should_continue == 'n':
            # break
            calculator()
        elif should_continue == 'e':
            break
            
calculator()