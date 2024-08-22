# # Aim : If we enter a number then we will get addition of those numbers
# # For example, if we enter 54 then we will get 9 as output



# a= int(input("Enter a number: "))

# str_a = str(a)

# sum=0

# for i in str_a:
#     int_i = int(i)
#     sum += int_i

# print(f'The sum of the digits of the number "{str_a}" is: ', sum)


# revision
a= int(input("Enter a number: "))


str_a = str(a)

sum = 0

for i in str_a:
    int_i = int(i)
    sum += int_i
    
print(f"The sum of all the digits present in the number {a} is {sum}")