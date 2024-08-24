# NOTE that this program is done with recursion but you should do it as i have written at last in the comment
# Reason behind it is that when we choose 'n',  every time the function will be called recursively
# which might create an issue of STACK OVERFLOW

# whereas in the code at last in comments with nested while loops instead of recursion,
# DOES NOT create an isuue of STACK OVERFLOW

# Also the TIME COMPLEXITIES of both the programs are SAME, SO NO WORRIES ABOUT TIME COMPLEXITY




# FOR EXTRA KNOWLEDGE OF THIS PARTICULAR PROGRAM YOU CAN FOLLOW THE LINK GIVEN BELOW
# https://chatgpt.com/share/1b11a447-c6a8-42c8-b4e2-eb7a5c5b04a9




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











# BELOW CODE IS GIVEN BY CHATGPT:

# def add(n1, n2):
#     return n1 + n2

# def substract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# symbols = {
#     '+': add,
#     '-': substract,
#     '*': multiply,
#     '/': divide,
# }

# def calculator():
#     while True:
#         num1 = int(input("Enter 1st number: "))

#         for symbol in symbols:
#             print(symbol)

#         should_continue = 'y'

#         while should_continue == 'y':
#             operation = input("Pick an operation: ")
#             next_number = int(input("What's the next number?: "))

#             calculation_function = symbols[operation]
#             answer = calculation_function(num1, next_number)

#             print(f'{num1} {operation} {next_number} = {answer}')

#             should_continue = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'e' to exit: ")

#             if should_continue == 'y':
#                 num1 = answer
#             elif should_continue == 'n':
#                 break
#             elif should_continue == 'e':
#                 return

# calculator()
