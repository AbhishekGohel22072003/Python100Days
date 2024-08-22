# name = input("Enter your name: ")
# l_name = input("Enter the name of the person you love: ")

# name_lower = name.lower() #will convert name into lower case
# l_name_lower = l_name.lower()

# concate = name_lower + l_name_lower

# T = concate.count("t")
# U = concate.count("u")
# R = concate.count("r")
# E = concate.count("e")

# L = concate.count("l")
# O = concate.count("o")
# V = concate.count("v")
# E = concate.count("e")

# True_sum = T+R+U+E
# Love_sum = L+O+V+E

# if True_sum>=10:
#     str_True_sum = str(True_sum)
#     sum = 0
#     for i in str_True_sum:
#         sum += int(i)
#     True_sum = sum
    
# if Love_sum>=10:
#     str_Love_sum = str(Love_sum)
#     sum = 0
#     for i in str_Love_sum:
#         sum += int(i)
#     Love_sum = sum

# str_True_sum = str(True_sum)
# str_Love_sum = str(Love_sum)

# result = str_True_sum + str_Love_sum

# print(f"The percentage of love of {name} with {l_name} is {result}%")






# Revision
your_name = input("Enter your name: ").lower()
crush_name = input("Enter the name of your crush: ").lower()

mixed_name = your_name+crush_name

t = mixed_name.count('t')
r = mixed_name.count('r')
u = mixed_name.count('u')
e = mixed_name.count('e')

l = mixed_name.count('l')
o = mixed_name.count('o')
v = mixed_name.count('v')
e = mixed_name.count('e')


sum_true = t+r+u+e
sum_love = l+o+v+e

if sum_true >=10:
    str_true = str(sum_true)
    sum_true = 0
    for i in str_true:
        sum_true += int(i)

if sum_love >=10:
    str_love = str(sum_love)
    sum_love = 0
    for i in str_love:
        sum_love += int(i)
        
print(f"The percentage of true love between you and {crush_name} is {sum_true}{sum_love}%...")