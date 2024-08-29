# import random

# random_side = random.randint(0,1)

# if random_side == 1:
#     HorT = "h"
# if random_side == 0:
#     HorT = "t"



# random_input = input("Choose a side of a coin 'h' for the Heads and 't' for the Tails: ")

# if random_input not in "h" or "t":
#     print("Please enter either 'h' or 't'....")
# else:
#     if random_input == HorT:
#         print("You have won the toss")
#     else:
#         print("You lose the toss.")





# Practice
import random

ran = random.randint(0,1)

if ran == 1:
    HorT = 'h'
elif ran == 0:
    HorT = 't'
    

user_input = input("Enter 'h' or 't' to choose a side of the coin. i.e. 'h' for Heads And 't' for Tails: ")

if user_input not in ('h','t'):
    print("Enter either 'h' or 't'. To try again press Ctrl+Alt+N")
else:
    if user_input == HorT:
        print("Congrats!! You have won the toss...")
    else:
        print("Sorry, You lose the toss, better luck next time...")