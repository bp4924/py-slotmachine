import random

MAX_LINES = 3
MIN_LINES = 1
MIN_BET = 1


ROWS = 3
REELS = 3

symbol_count = {
    "Gold    ": 1,
    "Apple   ": 2,
    "Banana  ": 4,
    "Cherry  ": 6,
    "Eggplant": 8
}

symbol_value = {
    "Gold    ": 20,
    "Apple   ": 9,
    "Banana  ": 8,
    "Cherry  ": 7,
    "Eggplant": 6
}

spin_count = 0


def check_winnings(columns, lines, bet, values):
    bet = int(bet)
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


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
                print(column[row], end=" | ")
            else:
                print(column[row])


def deposit():
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero!")
        else:
            print("please enter a number greater than 0")

    return amount


def get_number_of_lines(balance):
    while True:
        lines = 0
        print(f"initial lines {lines}")

        lines = input(
            f"How many lines do you want to bet ( {MIN_LINES} - {MAX_LINES} )? ")

        if lines.isdigit():
            lines = int(lines)
            if lines > balance:
                print(
                    f"Based on your balance, you cannot bet more than {balance} lines")
                lines = 0
                print(f"reset lines {lines}")
                get_number_of_lines(balance)
            elif 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please choose a number between 1 and {MAX_LINES}")
        else:
            print("please enter a number")
    return lines


def get_bet(balance, lines):
    # currently doesn't like non-integer bet amounts.
    while True:
        max_bet_per_line = int(balance / lines)

        print(
            f"You have ${balance} available, and have chosen to bet {lines} lines. Your max bet per line is ${max_bet_per_line}")
        bet = input("Place your bet $")

        if bet.isdigit():
            net_bet = int(bet) * lines
            net_max_bet = (max_bet_per_line * lines)
            print(
                f"You bet ${bet} on {lines} lines for a total bet of ${net_bet}")
            if MIN_BET <= net_bet <= net_max_bet:
                break
            else:
                print("")
                print(f"You have exceeded your balance. Please enter a lower amount")
                print("")
        else:
            print("Please enter a number greater than 0")

    return bet, net_bet


def game(balance, spin_count):
    lines = get_number_of_lines(balance)
    bet, net_bet = get_bet(balance, lines)

    print("")
    print(f"Spin {spin_count} Results:")
    print("")

    slots = get_spin(ROWS, REELS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    line_count = len(winning_lines)

    print("")
    print(f"winning lines - {line_count}")
    if line_count != 0:
        print(f"You won ${winnings} on line",  *winning_lines)
    winnings = winnings - net_bet
    return winnings


def main(spin_count):
    balance = deposit()
    print("")

    while True:
        print(f"Current balance is ${balance}")
        if balance == 0:
            print("")
            print("Game over!")
            print("Thank you for playing")
            break

        spin = input("Press enter to spin (q to quit).")
        if spin != "":
            print(f"Your balance is ${balance}")
            print("Thank you for playing")
            break
        spin_count += 1

        balance += game(balance, spin_count)


main(spin_count)
