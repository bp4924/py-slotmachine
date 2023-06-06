import random

MAX_LINES = 3
MIN_BET = 1

ROWS = 3
REELS = 3

symbol_count = {
    "Apple": 2,
    "Banana": 4,
    "Cherry": 6,
    "Eggplant": 8
}


def get_spin(rows, cols, symbols):
    # generate list of all occurances of each symbol
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        # use slice operator to create copy of list
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    # transpose lists
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|")
            else:
                print(column[row])


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
        max_bet_per_line = (balance) / lines
        print(
            f"You have ${balance} available, and have chosen to bet {lines} lines. Your max bet per line is ${max_bet_per_line}) $")
        bet = input("Place your bet $")
#        bet = float(bet)
        print(bet.isdigit())
        if bet.isdigit():
            net_bet = int(bet) * lines
            net_max_bet = (max_bet_per_line * lines)
            print(
                f"You bet ${bet} on {lines} lines for a total bet of ${net_bet}")
            if MIN_BET <= net_bet <= net_max_bet:
                break
            else:
                print(f"You have exceeded your balance")
        else:
            print("please enter a number greater than 0.0")

    return net_bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    net_bet = get_bet(balance, lines)
    print(balance, lines, net_bet)

    slots = get_spin(ROWS, REELS, symbol_count)
    print_slot_machine(slots)


main()
