from utils.clear_screen import clear_screen
import random

clear_screen()


deck = []


def draw_card():
    return deck.pop(random.randint(0, len(deck) - 1))


def get_score(cards):
    score = sum(cards)

    while score > 21:
        if 11 in cards:
            cards[cards.index(11)] = 1
            return get_score(cards)
        else:
            break

    return score


user_cards = []
dealer_cards = []


def display_score(is_stand):

    user_score = get_score(user_cards)
    print(f"Your deck: {user_cards} Score: {user_score}")

    if not is_stand:
        print(f"Dealer's deck: [{dealer_cards[1]}]")
    else:
        dealer_score = get_score(dealer_cards)
        print(f"Dealer's deck: {dealer_cards} Score: {dealer_score}")


def setup():
    global deck

    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
            11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
            11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
            11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    global user_cards
    global dealer_cards

    user_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]
    display_score(False)


setup()


def hit():
    user_cards.append(draw_card())
    display_score(False)


def stand():

    dealer_score = get_score(dealer_cards)

    while dealer_score < random.randint(15, 21):
        dealer_cards.append(draw_card())
        dealer_score = get_score(dealer_cards)

    display_score(True)


def play():

    playing = True

    user_score = get_score(user_cards)

    if user_score == 21:
        print("* * * Blackjack * * * YOU WON")
        playing = False

    while playing:

        playing_input = input("Do you want to hit or stand. h or s: ").lower()

        clear_screen()

        if playing_input == "h":
            hit()

            user_score = get_score(user_cards)
            if user_score > 21:
                print("BUST - YOU LOST")
                playing = False
            elif user_score == 21:
                print("YOU WON")
                playing = False

        else:
            stand()

            dealer_score = get_score(dealer_cards)
            user_score = get_score(user_cards)
            if dealer_score > 21:
                print("Dealer Bust - YOU WON")
            elif dealer_score == 21:
                print("YOU LOST")
            elif user_score > dealer_score:
                print("YOU WON")
            elif dealer_score > user_score:
                print("YOU LOST")
            else:
                print("DRAW")

            playing = False

    playing_input = input("Do you want to continue playing. y or n: ").lower()
    if playing_input == 'y':
        clear_screen()
        setup()
        play()


play()
