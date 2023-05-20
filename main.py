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

price = 0


def coin():
    global price
    choice_menu = MENU[drink]
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    chance = round(total - choice_menu["cost"], 2)
    if total < choice_menu["cost"]:
        print(f"That's coin {total} not enough. Your order cost: {choice_menu['cost']} ")
    elif total == choice_menu["cost"]:
        print(f"That's your {drink}: ☕︎ ")
        price += choice_menu["cost"]

    else:
        menu(drink)
        print(f"Your chance: {chance} and your {drink}: ☕︎")
        price += choice_menu["cost"]


def menu(choice):
    choice_menu = MENU[choice]
    choice_resources = choice_menu["ingredients"]
    for item in resources.keys():
        if item in choice_resources.keys():
            if resources[item] >= choice_resources[item]:
                resources[item] -= choice_resources[item]
    return True


def resources_info():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")


def resources_result(choice):
    choice_menu = MENU[choice]
    choice_resources = choice_menu["ingredients"]
    for item in resources.keys():
        if item in choice_resources.keys():
            if resources[item] < choice_resources[item]:
                return True



start = True

while start:

    drink = input("What would you like ? (espresso/latte/cappuccino: ").lower()
    if drink == "off":
        start = False

    elif drink == "report":
        resources_info()

    elif drink in MENU:
        if resources_result(drink):
            print(f"Resources not enough: {resources}")
            start = False
        else:
            coin()
