name = input("Enter your name: ")
l_name = input("Enter the name of the person you love: ")

name_lower = name.lower() #will convert name into lower case
l_name_lower = l_name.lower()

concate = name_lower + l_name_lower

T = concate.count("t")
U = concate.count("u")
R = concate.count("r")
E = concate.count("e")

L = concate.count("l")
O = concate.count("o")
V = concate.count("v")
E = concate.count("e")

True_sum = T+R+U+E
Love_sum = L+O+V+E

if True_sum>=10:
    str_True_sum = str(True_sum)
    sum = 0
    for i in str_True_sum:
        sum += int(i)
    True_sum = sum
    
if Love_sum>=10:
    str_Love_sum = str(Love_sum)
    sum = 0
    for i in str_Love_sum:
        sum += int(i)
    Love_sum = sum

str_True_sum = str(True_sum)
str_Love_sum = str(Love_sum)

result = str_True_sum + str_Love_sum

print(f"The percentage of love of {name} with {l_name} is {result}%")