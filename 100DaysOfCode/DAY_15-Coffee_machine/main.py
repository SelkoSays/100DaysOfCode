from menu_supplies import MENU, resources


def check_resources(order):
    if water_level < MENU[order]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
    elif milk_level < MENU[order]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk.")
    elif coffee_level < MENU[order]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
    else:
        pass
    return (water_level >= MENU[order]["ingredients"]["water"]) and\
            (milk_level >= MENU[order]["ingredients"]["milk"]) and\
            (coffee_level >= MENU[order]["ingredients"]["coffee"])

def check_transaction(order, payment):
    change = 0
    if payment > MENU[order]["cost"]:
        change = payment - MENU[order]["cost"]
    return payment >= MENU[order]["cost"],round(change,2)
def refill_machine(item):
    
    # changing global variables
    global water_level
    global milk_level
    global coffee_level

    match item:
        case "water":
            water_level = resources["water"]
            print(f"{item.capitalize()} successfully refilled!")
        case "milk":
            milk_level = resources["milk"]
            print(f"{item.capitalize()} successfully refilled!")
        case "coffee":
            coffee_level = resources["coffee"]
            print(f"{item.capitalize()} successfully refilled!")
        case _:
            water_level = resources["water"]
            milk_level = resources["milk"]
            coffee_level = resources["coffee"]
            print("Coffee machine successfully refilled!")
        


# Coin operated
"""
       Penny = $0.01
       Nickel = $0.05
       Dime = $0.10
       Quarter = $0.25
"""

water_level = resources["water"]
milk_level = resources["milk"]
coffee_level = resources["coffee"]
money_bank = 0


while True:

    # Take order
    order = input("What would you like to drink? (Espresso/Latte/Cappiccino/Coco/Hot water/Hot milk): ").lower()
    if order == "report":
        print(f"Water: {water_level}mL\nMilk: {milk_level}mL\nCoffee: {coffee_level}g\nMoney: ${money_bank}")
    elif order == "refill":
        item = input("What do you want to refill? (Water/Milk/Coffee/All): ").lower()
        refill_machine(item)
        print(f"Water: {water_level}mL\nMilk: {milk_level}mL\nCoffee: {coffee_level}g\nMoney: ${money_bank}")
    elif order == "exit":
        break
    else:
        if order not in MENU:
            continue

        if check_resources(order):
            print("Please insert coins.")
            payment = round((eval(input("How many quarters?: "))*0.25)+(eval(input("How many dimes?: "))*0.1)+(eval(input("How many nickels?: "))*0.05)+(eval(input("How many pennies?: "))*0.01),2)
            checked = check_transaction(order,payment)
            if checked[0]:
                money_bank += MENU[order]["cost"]
                print(f"Here is ${checked[1]:.2f} in change.")
                print(f"Here is your {order.capitalize()} ☕. Enjoy!")
                water_level -= MENU[order]["ingredients"]["water"]
                coffee_level -=  MENU[order]["ingredients"]["coffee"]
                milk_level -=  MENU[order]["ingredients"]["milk"]
            else:
                print("Payment not sufficient! Money refunded.")
        else:
            pass
