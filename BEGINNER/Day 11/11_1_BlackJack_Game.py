import random
def blackjack_game():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    # cards = [11]             <------For Testing
    
    
    def sum_of(cards):
        # This function will do the sum of the cards and if the sum is getting>21 and if it has ACE(i.e. 11) then it will convert them into 1
        sum = 0
        for i in cards:
            sum += i
        
        if sum>21:
            if 11 in cards:
                a = cards.count(11)
                sum = sum - (a*10)
        
        return sum
    
    
    
    
    


    def is_blackjack(list):
        # This check for starting only i.e. for starting two cards
        if list == [10,11] or list == [11,10]:
            return True



    while True:

        dealer_cards = []    #This will resets the values of dealer_cards every time we start over the game
        dealer_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        dealer_sum = sum_of(dealer_cards)
        # print(dealer_cards)
        # print(dealer_sum)

        user_cards=[]      #This will resets the values of user_cards every time we start over the game
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        user_sum = sum_of(user_cards)
        # print(user_cards)
        # print(user_sum)



        print(f"\tYour Cards: {user_cards}, Your current score: {user_sum}")
        print(f"\tDealer's first card: {dealer_cards[0]}\n")







        # process
        
        while True:
            # first we will check if the user is blackjack or not
            # if the user is blackjack and dealer is also a blackjack then DRAW
            # if the user is blackjack and dealer is NOT a blackjack then USER WIN
            if is_blackjack(user_cards):
                print(f'\tAs your cards are {user_cards}, you are a BLACKJACK.')
                if is_blackjack(dealer_cards):
                    print(f"\tBut dealer is also a BLACKJACK having cards {dealer_cards}.\n Hence the game is drawn...\n")
                    break
                    # return   <--Removed after I added the second while loop to play the BLACKJACK GAME again
                else:
                    print(f"\tAnd dealer's cards are: {dealer_cards} and score: {dealer_sum}")
                    print("Congratulations! You win!!!\n")
                    break
                    # return   <--Removed after I added the second while loop to play the BLACKJACK GAME again
                    
                    
            
            
            
            user_input = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_input == 'y':
                # if user want to get a card then we will add the card to the user_cards
                user_cards.append(random.choice(cards))
    
                # user_sum += user_cards[len(user_cards)-1]
                # print(user_sum)
                # Don't do the above one as it will do not work as expected if the cards is of Ace(i.e. 11)
    
    
    
                user_sum = sum_of(user_cards)       #This will use the sum_of function to avoid any bugs
                print(f"\tYour Cards: {user_cards}, Your current score: {user_sum}")
                print(f"\tDealer's first card: {dealer_cards[0]}\n")
                
                
                
                # if the user's score exceeds 21 then user will lose
                if user_sum>21:
                    print(f"\tYour final hand: {user_cards}, final score: {user_sum}\n\tDealer's final hand: {dealer_cards}, final score: {dealer_sum}")
                    print("\tYour score went over 21.\nYou lose. Better luck next time...\n")
                    break
                
                
            # if user type 'n' before exceeding 21 then dealer's process will be done
            elif user_input == 'n':
                def dealer_process(dealer_cards,cards):
                    dealer_sum = sum_of(dealer_cards)
                    while dealer_sum < 17:
                        dealer_cards.append(random.choice(cards))
                        dealer_sum = sum_of(dealer_cards)
                    return dealer_sum
                
                dealer_sum = dealer_process(dealer_cards=dealer_cards,cards=cards)    # Positional arguments are required
                # dealer_sum = dealer_process(dealer_cards,cards)
                
                print(dealer_sum)
                
                if (dealer_sum>22) or (dealer_sum<user_sum):
                    print(f"\tYour final hand: {user_cards}, final score: {user_sum}\n\tDealer's final hand: {dealer_cards}, final score: {dealer_sum}\n")
                    if dealer_sum>22:
                        print("\tDealer's score went over 21.")
                    elif dealer_sum<user_sum:
                        print("\tYour score is higher than the dealer's score.\n")
                    print('Congratulation!! You win....\n')
                    break
                
                elif dealer_sum == user_sum:
                    print(f"\tYour final hand: {user_cards}, final score: {user_sum}\n\tDealer's final hand: {dealer_cards}, final score: {dealer_sum}\n")
                    print("\tHence it is a DRAW.....\n")
                    break
                
                elif dealer_sum>user_sum:
                    print(f"\tYour final hand: {user_cards}, final score: {user_sum}\n\tDealer's final hand: {dealer_cards}, final score: {dealer_sum}\n")
                    print(f"Sorry, You lose!\n\tBetter luck next time...\n")
                    break
                
                
            elif user_input not in ['y', 'n']:
                print("\tPlease Enter either 'y' or 'n'\n")
                
                
            
        play_again = input("Do You Want to Play again? Type 'y' or 'n': ")
        if play_again != 'y':
            break



    





logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)           

                                      
     

blackjack_game()
