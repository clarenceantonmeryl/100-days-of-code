from os import system, name


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


bids = {}


def add_bid(name, bid_amount):
    bids[name] = bid_amount


def find_winner():
    highest_bid = 0
    highest_index = 0

    for index in bids:
        if bids[index] > highest_bid:
            highest_bid = bids[index]
            highest_index = index

    print(f"{highest_index} wins with a bid of {highest_bid}")


is_finished = False

while not is_finished:
    clear_screen()
    name_input = input("What is your name? ")
    bid_amount_input = float(input("How much do you bid? "))
    is_more = input("Are there more bidders? ")

    add_bid(name=name_input, bid_amount=bid_amount_input)

    if is_more == "no":
        is_finished = True
    else:
        clear_screen()

clear_screen()

find_winner()

# you are going to hospital now

