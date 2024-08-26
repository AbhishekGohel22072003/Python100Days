global_variable = 10

def modify_global_variable():
    global global_variable
    global_variable += 1

modify_global_variable()
print(global_variable)   
# Output : 11
# But this is not an efficient way
# Because some times chaging the global variable directly can cause some BUG ISSUES

# That's why the following function is an efficient way to modify a GLOBAL VARIABLE
def efficiently_modify_global_variable():
    return global_variable - 1 
global_variable = efficiently_modify_global_variable()  #MOST MOST MOST IMPORTANT LINES 
global_variable = efficiently_modify_global_variable()  #MOST MOST MOST IMPORTANT LINES 
print(global_variable)   # 9     (as 11-1-1)



'''Important question below'''


# What will be printed in the console when the code is run?

# DO NOT run the code, just pretend to be a computer.

# i = 50
# def foo():
#     i = 100
#     return i

# foo()
# print(i)


# 1
# 100

# 2
# 50

# 3
# 150

# 4
# NameError



# Correct Answer
# 2
# 50


#  Explanation
# The print statement is outside the function foo(). So it can't access the local variable i = 100. It only sees the global i, which 
# is equal to 50.