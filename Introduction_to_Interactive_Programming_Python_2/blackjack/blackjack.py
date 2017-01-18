# Mini-project #6 - Blackjack
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (CARD_SIZE[0]/2, CARD_SIZE[1]/2)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")
background = simplegui.load_image("https://cyphix.org/blackjack.png")
BACKGROUND_SIZE = (1280, 720)
HALF_BACKGROUND_SIZE = (BACKGROUND_SIZE[0]/2, BACKGROUND_SIZE[1]/2)

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
dealer_hand_position = (HALF_BACKGROUND_SIZE[0], BACKGROUND_SIZE[1]/5)
player_hand_position = (HALF_BACKGROUND_SIZE[0], BACKGROUND_SIZE[1] /2.1)

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
MONEY = 50


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        string = "( "
        for card in self.hand:
            string += str(card) + " "
        string += ")"
        return string

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        value = 0
        ace = False
        for card in self.hand:
            value +=  VALUES[card.get_rank()]
            if card.get_rank() == "A":
                ace = True
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        if ace == True:
            if value + 10 <= 21:
                value += 10


        return value

    def draw(self, canvas, pos):
        card_number = 0
        for card in self.hand:
            card.draw(canvas, (pos[0] + CARD_SIZE[0] * card_number - CARD_SIZE[0]/2 * len(self.hand), pos[1]))
            card_number += 1



# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) > 0:
            card = self.deck[-1]
            self.deck.pop()
            return card
        else:
            pass


    def __str__(self):
        string = "( "
        for card in self.deck:
            string += str(card) + " "
        string += ")"
        return string

player_hand = Hand()
dealer_hand = Hand()
deck = Deck()

print("Value : " + str(player_hand.get_value()))

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, score
    if in_play:
        score -= MONEY
    else:
        outcome = "New deal. Hit or stand?"
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    in_play = True

def hit():
    global player_hand, deck, in_play, score, outcome
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())
        outcome = "Hit or stand?"
        if player_hand.get_value() > 21:
            in_play = False
            outcome = "You have busted..."
            score -= MONEY
        elif player_hand.get_value() == 21:
            stand()
    else:
        outcome = "You have to start a new deal first"

def stand():
    global dealer_hand, deck, in_play, outcome, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        outcome = "Stand"
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        # Calculate score
        if dealer_hand.get_value() > 21:
            outcome = "Dealer have busted"
            score += MONEY
        else:
            if dealer_hand.get_value() < player_hand.get_value():
                outcome = "You win"
                score += MONEY
            else:
                outcome = "You lose"
                score -= MONEY
        in_play = False
    else:
        outcome = "The deal is already over"



    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    canvas.draw_image(background, HALF_BACKGROUND_SIZE , BACKGROUND_SIZE, HALF_BACKGROUND_SIZE, BACKGROUND_SIZE)
#    canvas.draw_text("Player's hand", (20, 290), 32, 'Black')
#    canvas.draw_text("Value : " + str(player_hand.get_value()), (400, 290), 32, 'Black')
    player_hand.draw(canvas, player_hand_position)
#    canvas.draw_text("Dealer's hand", (20, 30), 32, 'Black')
    dealer_hand.draw(canvas, dealer_hand_position)
    canvas.draw_text(str(score), (BACKGROUND_SIZE[0] -300, BACKGROUND_SIZE[1] - 40), 32, 'White')
    canvas.draw_text(outcome, (HALF_BACKGROUND_SIZE[0]-100, HALF_BACKGROUND_SIZE[1]-50), 32, 'White')
    # Hide dealer's first card if in play
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [dealer_hand_position[0] - CARD_SIZE[0]/2, dealer_hand_position[1] + CARD_SIZE[1]/2], CARD_SIZE)





# initialization frame
frame = simplegui.create_frame("Blackjack", BACKGROUND_SIZE[0], BACKGROUND_SIZE[1])
#frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
