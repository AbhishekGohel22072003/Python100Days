#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
print()

# Easy Level
password = ""

for char in range(1,nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char
    
    
for num in range(1,nr_numbers + 1):
    random_num = random.choice(numbers)
    password += random_num

for sym in range(1,nr_symbols + 1):
    random_sym = random.choice(symbols)
    password += random_sym

print(f'The easy to crack password is {password}')






# Hard Level


# My Thinking was as below





# list_pass = []

# for i in password:
#     list_pass.append(i)
# # print(list_pass)

# hard_password = ''
# for i in range(1,len(list_pass) + 1):
#     random_list_pass = random.choice(list_pass)
#     hard_password += random_list_pass

# print(f'The hard to crack password is {hard_password}')









# How actually it is:



list_pass = []

for i in password:
    list_pass.append(i)
# print(list_pass)

random.shuffle(list_pass) #This is very important function in the random module

hard_password = ''

for i in list_pass:
    hard_password += i

print(f'The hard to crack password is {hard_password}')