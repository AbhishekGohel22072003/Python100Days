MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def money_insertion():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))

    money_inserted = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return money_inserted


money = 0

while True:
    # The while loop will only be stop whenever the owner turns it off
    choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if choice == 'report':
        print(
            f'Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${money:.2f}')
        continue
    elif choice == "off":
        print("The machine has been turned off by the owner.....")
        break
    elif choice in ["espresso", 'latte', 'cappuccino']:
        # we will check if we have enough resources to make the selected item or not
        if resources['water'] < MENU[choice]['ingredients']['water']:
            print("Sorry not enough water.")
            continue
        if choice != "espresso":
            # as there is no need of milk in making of espresso
            if resources['milk'] < MENU[choice]['ingredients']['milk']:
                print("Sorry not enough milk.")
                continue
        if resources['coffee'] < MENU[choice]['ingredients']['coffee']:
            print("Sorry not enough coffee.")
            continue


        # now we will take money from the customer
        money_inserted = money_insertion()


        # now we will check if the inserted money is enough to purchase the selected item or not
        if money_inserted < MENU[choice]['cost']:
            print("Sorry, that's not enough money. Money refunded.")
            continue
        else:
            change = money_inserted - MENU[choice]['cost']
            rounded_change = round(change, 2)
            money += MENU[choice]['cost']


        # The resources will be deducted only after receiving the enough amount from the customer
        resources['water'] -= MENU[choice]['ingredients']['water']
        if choice != 'espresso':
            resources['milk'] -= MENU[choice]['ingredients']['milk']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']


        # Provides the change if needed
        if change != 0.0:
            print(f'Here is ${rounded_change:.2f} in change.')

        print(f'Here is your {choice}. Enjoy!')

    else:
        print("Invalid item/ item not in the menu...")
