def pos_vs_kw(name, location):
    print(f'Hello, my name is {name}')
    print(f'I am from {location}')
    
    
    
# The arguments(values passed into the parenthesis are called arguments) passed in following line are the positional/non keyword arguments
# Note that positional argument = non keyword argument
pos_vs_kw('abhishek','bhavnagar')
# output : 
# Hello, my name is abhishek
# I am from bhavnagar


pos_vs_kw(location='bhavnagar', name='abhishek')
# output is the same as above