# def prime_checker():
#     p_or_not = int(input("Enter a number to check if it is a prime number or not: "))

#     # a = int(p_or_not/2 + 1)
#     b = p_or_not//2+1
#     # print(a) 
#     # print(b)
#     # Both of the above gives the same output

#     t_or_f = True


#     # If the number is less than 2, it can't be prime.
#     if p_or_not<2:
#         t_or_f = False
#     else:       
#         for i in range(2,b):
#             if p_or_not % i == 0:
#                 t_or_f = False
#                 break
            


#     if t_or_f == True:
#         print(f"The entered number {p_or_not} is a prime number.")
#     else:
#         print(f'The entered number {p_or_not} is not a prime number.')
        
        
        
        
# prime_checker()










# Revision

def prime_checker():
    number = int(input("Enter a number to check if it is a prime number or not: "))
    prime = True
    
    for i in range(2,number//2+1):
        if number == 1:
            print("The number 1 is not a prime number.")
        elif number % i == 0:
            print(f"The number is divisible by {i}.")
            prime = False
            break
    
    if prime == False:
        print(f"That is why the number {number} is NOT a prime number.")
    else:
        print(f'The number {number} is a prime number.')

prime_checker()