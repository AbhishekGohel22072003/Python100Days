# Why do we use return instead of print?



# Because if we want to add that function as an argument in another function then return would be helpful instead of print
# That is the main reason to use return instead of print




# for example

def add_return(num1, num2):
    return num1 + num2


def add_print(num1, num2):
    print(num1+num2)


return_var = add_return(2,add_return(5,4))
print(return_var)  #11


print_var = add_print(2,add_print(5,4))
print(print_var)  
# Error as 2nd argument is now string and string and numbers cannot be concatenated

# Output:

# 9            <--------------NOTE THIS (9 because it will first count for 5+4 that is why it is printed)
# Traceback (most recent call last):
#   File "c:\Users\Abhishek Gohel\Desktop\Python 100 Days\Day 10\10_6_Return_VS_Print.py", line 25, in <module>
#     print_var = add_print(2,add_print(5,4))
#                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "c:\Users\Abhishek Gohel\Desktop\Python 100 Days\Day 10\10_6_Return_VS_Print.py", line 18, in add_print
#     print(num1+num2)
#           ~~~~^~~~~\



