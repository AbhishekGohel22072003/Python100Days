import random

randomInteger = random.randint(1,3)
# Computer will randomly pick either 1 or 2 or 3

random_rps = None
# Initializing variable to use in below if_else ladder

if randomInteger == 1:
    random_rps = "Rock"
elif randomInteger == 2:
    random_rps = "Paper"
elif randomInteger == 3:
    random_rps = "Scissors"

player_input = input("Enter R for 'Rock', P for 'Paper' and S for 'Scissors' : ")
# This will take input from the user
if player_input not in "R" or "P" or "S":
    print("Please Enter A valid Entry(i.e. 'R' or 'P' or 'S')")
else:
    player_input_full_name = None
    # initializing variable to use in below if_else ladder

    if player_input == "R":
        player_input_full_name = "Rock"
    elif player_input == "P":
        player_input_full_name = "Paper"
    elif player_input == "S":
        player_input_full_name = "Scissors"



    print(f"The entry choosen by computer was {random_rps} against yours {player_input_full_name}")
    # This will say what computer and you have chose



    # below code will print the result as per your entry and entry chosen by computer

    if player_input_full_name == random_rps:
        print("It is a draw...")
    elif random_rps == "Rock" and player_input_full_name == "Scissors":
        print("Sorry, you lose. Better luck next time...\nTo play again press Ctrl+Alt+n")
    elif random_rps == "Rock" and player_input_full_name == "Paper":
        print("You won!! \nIf you enjoyed and want to play again then press Ctrl+Alt+n")
    elif random_rps == "Paper" and player_input_full_name == "Rock":
        print("Sorry, you lose. Better luck next time...\nTo play again press Ctrl+Alt+n")
    elif random_rps == "Paper" and player_input_full_name == "Scissors":
        print("You won!! \nIf you enjoyed and want to play again then press Ctrl+Alt+n")
    elif random_rps == "Scissors" and player_input_full_name == "Rock":
        print("You won!! \nIf you enjoyed and want to play again then press Ctrl+Alt+n")
    elif random_rps == "Scissors" and player_input_full_name == "Paper":
        print("Sorry, you lose. Better luck next time...\nTo play again press Ctrl+Alt+n")
