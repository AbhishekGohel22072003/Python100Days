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

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

for symbol in symbols:
    print(symbol)

operation = input("Enter an operation to do between 1st number and 2nd number from the above options: ")

calculation_function = symbols[operation]

answer  = calculation_function(num1,num2)

print(f'{num1} {operation} {num2} = {answer}')