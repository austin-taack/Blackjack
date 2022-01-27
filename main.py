# This project runs a game of Blackjack. The current iteration of this project runs on the command line,
# but future versions will hopefully feature a GUI. The user plays against an automated dealer.


from random import shuffle
from time import sleep


# Dealer runs the procedure for the dealer the player is trying to beat
class Dealer:

    # Initializes the dealer's hand
    def __init__(self):
        self.face_up_card = ""
        self.face_down_card = ""
        self.hand = []

    # Deals cards to each player
    def deal(self):
        drawn_card = deck.pop(0)
        player_hand.append(drawn_card)

        drawn_card = deck.pop(0)
        self.face_up_card = drawn_card

        drawn_card = deck.pop(0)
        player_hand.append(drawn_card)

        drawn_card = deck.pop(0)
        self.face_down_card = drawn_card

        self.hand.append(self.face_up_card)
        self.hand.append(self.face_down_card)


# Shuffles the deck
def shuffle_deck():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Clubs", "Spades", "Diamonds"]

    for suit in suits:
        for value in values:
            card = [value, suit]
            deck.append(card)

    shuffle(deck)


# Draws a card from the deck and adds it to the given hand
def draw_card(hand):
    drawn_card = deck.pop(0)
    hand.append(drawn_card)


# Finds the total of a player's hand
def sum_cards(hand):
    value_table = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10
    }

    card_sum = 0
    ace_count = 0

    for card in hand:
        if card[0] == "Ace":
            ace_count += 1
        else:
            card_sum += value_table[card[0]]

    for ace in range(ace_count):
        points_until_bust = 21 - card_sum
        if points_until_bust >= 11:
            card_sum += 11
        else:
            card_sum += 1

    return card_sum


# Runs the main flow of the game
debug = False

print("Welcome to Blackjack. Let's start a new game.")
sleep(1)
print()

keep_playing = True

while keep_playing:

    # Initializes the game
    deck = []
    shuffle_deck()
    dealer = Dealer()
    player_hand = []
    player_bust = False
    dealer_bust = False

    # Deals cards and reads them off
    dealer.deal()
    print("Cards have been delt.")
    sleep(1)
    print("You have the " + player_hand[0][0] + " of " + player_hand[0][1] + " and the " +
          player_hand[1][0] + " of " + player_hand[1][1] + ".")
    sleep(1)
    print("The dealer has the " + dealer.face_up_card[0] + " of " + dealer.face_up_card[1] + " and one card face-down.")
    sleep(1)
    if debug:
        print("Debug mode: the face down card is the " + dealer.face_down_card[0] + " of " + dealer.face_down_card[1] +
              ".")
        sleep(1)
    print()

    # Carries out the player's turn
    while True:
        print("It is now your turn.")
        sleep(1)

        print("Type 'hit' for another card or 'stand' to end your turn (without quotation marks).")
        response = input()
        if response == 'hit':
            draw_card(player_hand)
            print("You have drawn the " + player_hand[-1][0] + " of " + player_hand[-1][1] + ".")
            sleep(1)
            if sum_cards(player_hand) > 21:
                player_bust = True
                print("Bust.")
                sleep(1)
                break
        elif response == 'stand':
            break
        else:
            print("Please enter a valid command.")

    print()

    # Carries out the dealer's turn
    if not player_bust:
        print("It is now the dealer's turn.")
        sleep(1)

        while True:
            if sum_cards(dealer.hand) <= 16:
                draw_card(dealer.hand)
                print("The dealer drew the " + dealer.hand[-1][0] + " of " + dealer.hand[-1][1] + ".")
                sleep(1)
                if sum_cards(dealer.hand) > 21:
                    sleep(1)
                    dealer_bust = True
                    break
            else:
                break

        print()

    # Handles end of the turn
    print("The dealer's face-down card was the " + dealer.face_down_card[0] + " of " + dealer.face_down_card[1] + ".")
    sleep(1)

    dealer_score = sum_cards(dealer.hand)
    player_score = sum_cards(player_hand)
    print("You: " + str(player_score) + " \tDealer: " + str(dealer_score))
    sleep(1)

    if dealer_score > player_score or player_bust:
        print("Sorry, you lose.")
    elif dealer_score < player_score or dealer_bust:
        print("You win!")
    else:
        print("It's a tie.")

    sleep(1)
    print()

    while True:
        print("Would you like to play again? Type 'Y' for yes or 'N' for no (without quotation marks).")
        response = input()

        if response == 'N':
            print("Thanks for playing!")
            keep_playing = False
            break
        elif response == 'Y':
            print()
            break
        else:
            print("Please enter a valid command.")
