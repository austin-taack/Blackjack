# This project runs a game of Blackjack. The current iteration of this project runs on the command line,
# but future versions will hopefully feature a GUI. The user plays against an automated dealer.


from random import shuffle


# Dealer runs the procedure for the dealer the player is trying to beat
class Dealer:

    # Initializes the dealer's hand
    def __init__(self):
        self.face_up_card = ""
        self.face_down_card = ""

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


# Shuffles the deck
def shuffle_deck():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Clubs", "Spades", "Diamonds"]

    for suit in suits:
        for value in values:
            card = value + " of " + suit
            deck.append(card)

    shuffle(deck)


# Runs the main flow of the game
deck = []
shuffle_deck()
dealer = Dealer()
player_hand = []

dealer.deal()
print("Cards have been delt.")
print("You have the " + player_hand[0] + " and the " + player_hand[1] + ".")
print("The dealer has the " + dealer.face_up_card + " and one card face-down.")
print("Debug mode: the face down card is the " + dealer.face_down_card + ".")
