from database import MENU, dispenser, coins


def report():
    for key, value in dispenser.items():
        if key == 'Coffe':
            print(f'{key}: {value}g')
        elif key == 'Money':
            print(f'{key}: ${value}')
        else:
            print(f'{key}: {value}ml')


def coins_calculate():
    print("Please insert coins.")
    quarter = float(input("how many quarters?: "))
    dime = float(input("how many dimes?: "))
    nickel = float(input("how many nickles?: "))
    penny = float(input("how many pennies?: "))
    total = quarter * coins['quarter'] + dime * coins['dime'] + nickel * coins['nickel'] + penny * coins['penny']

    if total < MENU[order]['cost']:
        print("Sorry that's not enough money. Money refunded")
        coffe_machine()
    else:
        play()
        change = total - MENU[order]['cost']
        print(f"Here is ${change} in change.")
        print(f"Here is your {order.capitalize()} ☕. Enjoy!")
        dispenser['Money'] += MENU[order]['cost']
        coffe_machine()


def play():
    chosen = MENU[order]
    for el, val in chosen['ingredients'].items():
        dispenser[str(el).capitalize()] -= val


def coffe_machine():
    should_continue = True

    while should_continue:
        global order
        order = input("What would you like? (espresso/latte/cappuccino):")

        if order == 'report':
            report()
            continue
        elif order == 'off':
            should_continue = False
        else:
            for el, val in MENU[order]['ingredients'].items():
                if dispenser[str(el).capitalize()] < val:
                    print(f"Sorry there is not enough {el}")
                    break
                else:
                    coins_calculate()


coffe_machine()


