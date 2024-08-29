number = 10

def decrease_number():
    local_number = 25 #THIS CANNOT BE ACCESIBLE OUTSIDE THE LOCAL SCOPE (i.e. OUTSIDE THE FUNCTION)
    global number
    number -=1
    print(number)


decrease_number()
print(number)





if 2<3:
    a = 'this is not in a local scope unlike other languages like JAVA or C++...... That means this will be accesible outside the if statement'

print(a)





while True:
    b = 'same thing is applicable for loops also as this is also accesible outside the while loop'
    break

print(b)