MAX_LINES = 3
MIN_BET = 1


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


def get_bet(balance, lines):
    # currently doesn't like non-integer bet amounts.
    while True:
        max_bet_per_line = int((balance / lines)*100)/100
        print(max_bet_per_line)
        bet = input(
            f"Place your bet. You have ${balance} available, and have chosen to bet {lines} lines. Your max bet per line is ${max_bet_per_line}) $")
        if bet.isdigit():
            net_bet = int(bet) * lines
            net_max_bet = max_bet_per_line * lines
            print(
                f"You bet ${bet} on {lines} lines for a total bet of ${net_bet}")
            if MIN_BET <= net_bet <= net_max_bet:
                break
            else:
                print(f"You have exceeded your balance")
        else:
            print("please enter a number greater than 0")

    return net_bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    net_bet = get_bet(balance, lines)
    print(balance, lines, net_bet)


main()
