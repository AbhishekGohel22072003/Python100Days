import os #Imported to clear the screen every time we type 'yes'
# os.system('cls')


logo = "logo will be here"
print(logo)

print("Welcome to the secret auction program.")

my_bidders = {}
i=0

def add_bidder():
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
        
        # max_bid = 0
        
        for i in my_bidders:
            if my_bidders[i][1]>max_bid:
                # max_bid = my_bidders[i][1]
                index = i
        
        print(f"The winner is {my_bidders[i][0]} with a bid of ${my_bidders[i][1]}")

add_bidder()