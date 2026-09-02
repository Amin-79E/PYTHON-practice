
def calculate_quarters(cents):
    quarters = 0
    while cents >= 25:
        quarters += 1
        cents = cents - 25

    return quarters


def calculate_dimes(cents):
    dimes = 0
    while cents>=10:
        dimes += 1
        cents = cents - 10

    return dimes

def calculate_nickels(cents):
    nickels = 0
    while cents >= 5:
        nickels += 1
        cents = cents - 5

    return nickels

def calculate_pennies(cents):
    pennies = 0
    while cents >=1:
        pennies += 1
        cents = cents -1

    return pennies

def enter():
    while True:
        try:
            cents = int((input("Enter the amount af cents : ")))
            if cents >0:
                return cents
        except ValueError:
            continue
            

def main():
    
    cents = enter()


    quarters = calculate_quarters(cents)
    cents = cents - (quarters * 25)

    dimes = calculate_dimes(cents)
    cents = cents - (dimes * 10)

    nickels = calculate_nickels(cents)
    cents = cents - (nickels * 5)

    pennies = calculate_pennies(cents)
    cents = cents - (pennies)

    coins = quarters + dimes + nickels + pennies

    print(f"That would give you: {coins}")

if __name__ == "__main__":
    main()
