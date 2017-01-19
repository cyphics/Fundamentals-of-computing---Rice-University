# implementation of card game - Memory

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import sys

CARD_WIDTH=50
# Stores shuffled values of cards
card_values=[]
# Stores state of cards (hidden(0), turned(1), paired(2))
card_states=[]
# State of the 'turning card' process
click_counter=0
# Position in card_states that are currently evaluated
trial_cards=[]

# Create deck to play with
value_basis=list(range(1,9))
values_to_distribute=value_basis+value_basis


# helper function to initialize globals
def new_game():
    # Set new order cards
    global card_values, card_states, click_counter, trial_cards
    card_values = values_to_distribute
    random.shuffle(card_values)

    # Reset states
    click_counter = 0
    trial_cards = []
    card_states=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global card_states, click_counter, trial_cards, card_values

    # Identify index of clicked card. Divides x by width of card, removes coma, and transforms to integer
    clicked_card = int((pos[0] / 50) - (pos[0] / 50)%1)

    # If card not yet turned
    if card_states[clicked_card] == 0:
      card_states[clicked_card] = 1

      if len(trial_cards) == 0:
          trial_cards.append(clicked_card)
      elif len(trial_cards) == 1:
          trial_cards.append(clicked_card)
          if card_values[trial_cards[0]] == card_values[trial_cards[1]]:
              card_states[trial_cards[0]] = 2
              card_states[trial_cards[1]] = 2
      else:
          if card_values[trial_cards[0]] != card_values[trial_cards[1]]:
              card_states[trial_cards[0]] = 0
              card_states[trial_cards[1]] = 0
          click_counter += 1
          trial_cards=[]
          trial_cards.append(clicked_card)

# cards are logically 50x100 pixels in size
def draw(canvas):
    global card_states, label
    label.set_text("Turns =" + str(click_counter))
    card_position=0
    for card in card_states:
        # If returned
        if (card == 1 or card == 2):
            canvas.draw_text(str(card_values[card_position]), (CARD_WIDTH/2 + card_position * CARD_WIDTH - 8, 58), 32, 'Green')
            canvas.draw_line(((card_position + 1) * CARD_WIDTH,0), ((card_position + 1) * CARD_WIDTH, 100), 1, 'Green')

        # Else
        elif card == 0:
            canvas.draw_line((CARD_WIDTH/2 + card_position * CARD_WIDTH, 0), (CARD_WIDTH/2 + card_position * CARD_WIDTH, 100), CARD_WIDTH, 'Green')
            canvas.draw_line(((card_position + 1) * CARD_WIDTH,0), ((card_position + 1) * CARD_WIDTH, 100), 1, 'Black')
        else:
            print ("ERROR: Bad card state")
        card_position+=1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(click_counter))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
