import random
def blackjack_game():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


    def is_blackjack(list):
        if list == [10,11] or list == [11,10]:
            return True

    dealer_list = []
    dealer_list.append(random.choice(cards))
    dealer_list.append(random.choice(cards))
    dealer_sum = 0
    for i in dealer_list:
        dealer_sum += i
    # print(dealer_list)
    # print(dealer_sum)

    user_list=[]
    user_list.append(random.choice(cards))
    user_list.append(random.choice(cards))
    user_sum = 0
    for i in user_list:
        user_sum += i
    # print(user_list)
    # print(user_sum)



    print(f"Your Cards: {user_list}, current score: {user_sum}")
    print(f"Dealer's first card: {dealer_list[0]}")


    if is_blackjack(user_list):
        print(f'As your cards are {user_list}, you are a BLACKJACK.')
        if is_blackjack(dealer_list):
            print("But dealer is also a BLACKJACK.\n Hence the game is drawn...")
            return
        else:
            print("Congratulations! You win!!!")
            return





    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        pass








blackjack_game()