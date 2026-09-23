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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient]>=resources[ingredient]:
            print("Sorry, the ingredient is not sufficient")
            return False
    return True

def is_transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change=money_received-drink_cost
        print(f"Here is the change: {change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry, the money is not sufficient")
        return False


def process_coin():
    print("please enter the coins: ")
    total=int(input("Enter how many quarters:"))*0.25
    total += int(input("Enter how many dims:")) * 0.1
    total += int(input("Enter how many nickles:")) * 0.05
    total += int(input("Enter how many pennies:")) * 0.01
    return total

def make_coffee(drink_name,ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]
    print(f" Here is your drink {drink_name}")
machine="run"

while machine=="run":
    coffee=input("“What would you like? (espresso/latte/cappuccino): ")
    if coffee=="off":
        machine="stop"
    elif coffee=="report":
        print(f"water:{resources["water"]}")
        print(f"milk:{resources["milk"]}")
        print(f"coffee:{resources["coffee"]}")
        print(f"profit:{profit}")
    else:
        drink=MENU[coffee]
        if is_resources_sufficient(drink["ingredients"]):
            payment= process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(coffee,drink["ingredients"])








