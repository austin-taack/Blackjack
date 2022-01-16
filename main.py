# This project runs a game of Blackjack. The current iteration of this project runs on the command line,
# but future versions will hopefully feature a GUI. The user plays against an automated dealer.


from random import shuffle


# Dealer runs the procedure for the dealer the player is trying to beat
class Dealer:

    # Initializes the dealer's hand
    def __init__(self):
        self.face_up_card = ""
        self.face_down_card = ""
        self.hand = []

    # Deal cards to each player
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
debug = True

deck = []
shuffle_deck()
dealer = Dealer()
player_hand = []

dealer.deal()
print("Cards have been delt.")
print("You have the " + player_hand[0][0] + " of " + player_hand[0][1] + " and the " +
      player_hand[1][0] + " of " + player_hand[1][1] + ".")
print("The dealer has the " + dealer.face_up_card[0] + " of " + dealer.face_up_card[1] + " and one card face-down.")
if debug:
    print("Debug mode: the face down card is the " + dealer.face_down_card[0] + " of " + dealer.face_down_card[1] + ".")
print()

while True:
    print("It is now your turn.")
    response = ""

    while True:
        print("Type 'hit' for another card or 'stand' to end your turn (without quotation marks).")
        response = input()
        if response == 'hit' or response == 'stand':
            break
        else:
            print("Please enter a valid command.")

    if response == 'hit':
        draw_card(player_hand)
        bust = sum_cards(player_hand) <= 21
        print("You have drawn the " + player_hand[-1][0] + " of " + player_hand[-1][1] + ".")
        if bust:
            print("You have busted.")
            break
