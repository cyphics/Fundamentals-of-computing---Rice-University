# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

lower_value=0
higher_value=100
moves_to_play=7
moves_left=moves_to_play
num_to_guess=0

# helper function to start and restart the game
def new_game():
    """ Game initialization """
    global num_to_guess
    global moves_left
    moves_left=moves_to_play
    print ""
    print "Guess a number between 0 and", higher_value-1, "in ", moves_to_play, "moves"
    num_to_guess=random.randrange(lower_value, higher_value)
    print ""

# define event handlers for control panel
def range100():
    """ Starts a new game with 0-100 range """
    global higher_value
    global moves_to_play
    higher_value=100
    moves_to_play=7
    new_game()

def range1000():
    """ Starts a new game with 0-1000 range """
    global higher_value
    global moves_to_play
    higher_value=1000
    moves_to_play=10
    new_game()

def input_guess(guess):
    """ defines the moves of the player """
    global moves_left
    num=int(guess)
    print "Your guess is:",num
    if num<num_to_guess:
        print "Higher"
    elif num>num_to_guess:
        print "Lower"
    else:
        print "Correct!"
        print ""
        new_game()
        return

    moves_left-=1
    print "You have", moves_left, "moves left"
    print ""
    if moves_left==0:
        print "You lost. The number to guess was:", num_to_guess
        print ""
        new_game()



# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("What's your guess?", input_guess, 100)
frame.start()

# call new_game
new_game()


# always remember to check your completed program against the grading rubric
