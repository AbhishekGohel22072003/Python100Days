# import random


# print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

# number = random.randint(1,100)

# while True:
#     difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

#     if difficulty == 'easy':
#         attempts = 10
#         break
#     elif difficulty == 'hard':
#         attempts = 5
#         break
#     elif difficulty not in ['easy','hard']:
#         print("You must type either 'easy' or 'hard'...")
    
# while True:
#     if attempts == 0:
#         print(f"You have {attempts} remaining to guess the number.")
#         print(f"You lose to guess a number. Better luck next time...")
#         print(f"The number was {number}.")
#         break
    
    
#     print(f"You have {attempts} remaining to guess the number.")
#     guessed_number = int(input("Make a guess: "))
    
#     if guessed_number == number:
#         print(f"You got it! The answer was {number}")
#         break
#     else:    
#         if guessed_number < number:
#             print("Too low.")
#         elif guessed_number > number:
#             print("Too high.")
        
#         attempts -= 1
#         if attempts != 0:
#             print("Guess again.")






'''
# Below code is given by chatgpt

# BUT THE ABOVE CODE WHICH IS DONE BY ME IS ALSO A VERY GOOD CODE
'''







import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        attempts = 10
        break
    elif difficulty == 'hard':
        attempts = 5
        break
    elif difficulty not in ['easy', 'hard']:
        print("You must type either 'easy' or 'hard'...")
    
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    
    if guessed_number == number:
        print(f"You got it! The answer was {number}")
        break
    else:
        if guessed_number < number:
            print("Too low.")
        else:
            print("Too high.")
        
        attempts -= 1
        if attempts > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses. You lose.")
            print(f"The number was {number}.")
