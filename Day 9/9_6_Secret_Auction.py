import os #Imported to clear the screen every time we type 'yes'
# os.system('cls')


# DID YOU KNOW?
# if we do following then i will be changed every time the function called
# i.e.

# i = 0
# def i_changer():
#     global i
#     i +=1
# i_changer()
# i_changer()
# i_changer()
# i_changer()
# print(i)     # 4




logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

print("Welcome to the secret auction program.")

my_bidders = {}
i=0

def add_bidder():
    global i
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    
    y_or_n = input("Are there any other bidders? Type 'yes' or 'no'.")
    
    new_bidder = [name,bid]
    
    my_bidders[i] = new_bidder
    
        
    if y_or_n == 'yes':
        os.system('cls')
        i +=1
        add_bidder()
    
    elif y_or_n == 'no':
        os.system('cls')
        max_bid = 0
        
        for i in my_bidders:
            if my_bidders[i][1]>max_bid:
                max_bid = my_bidders[i][1]
                index = i
        
        print(f"The winner is {my_bidders[index][0]} with a bid of ${my_bidders[index][1]}")

add_bidder()
print(my_bidders)