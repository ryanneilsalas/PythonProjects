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

profit = 0
is_on = True


def check_resources(pick_drink_resource):
    for item in pick_drink_resource:
        if pick_drink_resource[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def calculate_transaction(total_coins, drinks):
    if total_coins >= drinks["cost"]:

        change = round(total_coins - drinks["cost"], 2)
        global profit
        profit = round(total_coins - change, 2)
        print(f"Your change is ${change}")
        take_resources(drink["ingredients"])
    else:
        print("Sorry that's not enough money. Money Refunded")


def take_resources(taken_resource):
    for item in taken_resource:
        resources[item] -= taken_resource[item]


while is_on:
    pick_coffee = input("What would you like? espresso/latte/cappuccino: ")
    if pick_coffee == "off":
        is_on = False
    elif pick_coffee == "report":
        print(f"Water : {resources["water"]}ml"
              f"\nMilk: {resources["milk"]}ml"
              f"\nCoffee: {resources["coffee"]}g"
              f"\nProfit: ${profit}"
              )
    elif pick_coffee == "espresso" or pick_coffee == "latte" or pick_coffee == "cappuccino":
        drink = MENU[pick_coffee]
        if check_resources(drink["ingredients"]):
            print("Please Insert Coin: ")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            calculate_transaction(total, drink)
        print(f"Here is your {pick_coffee}. Enjoy!")
    else:
        print("Sorry, We dont have that coffe")
