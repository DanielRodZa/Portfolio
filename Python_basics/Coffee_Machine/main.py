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

CHOICES = ['espresso','latte','cappucino']


def is_resource_sufficient(order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enought {item}.")
            return False
    return True

def process_coin(drink):

    print(f"Please insert coin. (Coffee cost: {drink})")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_succesful(money_received, drink_cost, profit):

    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")

        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕. Enjoy!!')

def print_report(profit):
    print(f"Water: {resources['water']}ml.")
    print(f"Milk: {resources['milk']}ml.")
    print(f"Coffee: {resources['coffee']}g.")
    print(f"Money: ${profit}.")

def main():
    is_on = True
    profit = 0
    while is_on:
        choice = input("What would you like? (espresso/latte/cappucino): ")
        if choice.lower() == "off":
            is_on = False
        elif choice.lower() == 'report':
            print_report(profit)
        elif choice.lower() in CHOICES:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coin(drink['cost'])
                if is_transaction_succesful(payment, drink["cost"], profit):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Please select a valid option.")

if __name__ == "__main__":
    main()