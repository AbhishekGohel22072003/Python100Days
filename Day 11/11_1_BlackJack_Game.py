import random
def blackjack_game():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    # cards = [11]
    
    
    def sum_of(cards):
        sum = 0
        for i in cards:
            sum += i
        
        if sum>21:
            if 11 in cards:
                a = cards.count(11)
                sum = sum - (a*10)
        
        return sum
    
    
    
    
    


    def is_blackjack(list):
        if list == [10,11] or list == [11,10]:
            return True





    dealer_cards = []
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    dealer_sum = sum_of(dealer_cards)
    print(dealer_cards)
    print(dealer_sum)

    user_cards=[]
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    user_sum = sum_of(user_cards)
    print(user_cards)
    print(user_sum)



    print(f"\tYour Cards: {user_cards}, Your current score: {user_sum}")
    print(f"\tDealer's first card: {dealer_cards[0]}")


    if is_blackjack(user_cards):
        print(f'As your cards are {user_cards}, you are a BLACKJACK.')
        if is_blackjack(dealer_cards):
            print(f"But dealer is also a BLACKJACK having cards {dealer_cards}.\n Hence the game is drawn...")
            return
        else:
            print(f"And dealer's cards are: {dealer_cards} and score: {dealer_sum}")
            print("Congratulations! You win!!!")
            return





    # process
    
    while True:
        
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            
            user_cards.append(random.choice(cards))
 
            # user_sum += user_cards[len(user_cards)-1]
            # print(user_sum)
            # Don't do the above one as it will do not work as expected if the cards is of Ace(i.e. 11)
 
            user_sum = sum_of(user_cards)
            print(f"Your Cards: {user_cards}, Your current score: {user_sum}")
            print(f"Dealer's first card: {dealer_cards[0]}")
            
            if user_sum>21:
                print(f"Your final hand: {user_cards}, final score: {user_sum}\nDealer's final hand: {dealer_cards}, final score: {dealer_sum}")
                print("Your score went over 21.\nYou lose. Better luck next time\n\n\n")
                break
            
    
    
    
    
    
    while True:
        if input("Do You Want to Play again? Type 'y' or 'n': ") == 'y':
            blackjack_game()
        else:
            break




    

    # return







print("logo")
blackjack_game()
