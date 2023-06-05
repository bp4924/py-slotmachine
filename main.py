MAX_LINES = 3


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero!")
        else:
            print("please enter a number greater than 0")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "How many lines do you want to bet (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please choose a number between 1 and " + str(MAX_LINES))
        else:
            print("please enter a number")

    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()
