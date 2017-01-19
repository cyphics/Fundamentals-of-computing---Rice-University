# template for "Stopwatch: The Game"
import simplegui
# define global variables

# Variables to draw the digit numbers properly
scale=6 # global scale of number size
score_ratio=2 # scale of score numbers compared to global scale
dw=1*scale # width of digital segment
dl=6*scale # length of digital segment
num_width=dw+dl # width of a digital number on screen
num_sep=3*dw # width between two numbers
min_pos=(20, 100) # Initial position of the timer
min_sep=(min_pos[0]+num_sep+num_width, min_pos[1]) # position of the minutes separator
tensec_pos=(min_sep[0]+num_sep, min_pos[1]) # position of the tens seconds
sec_pos=(tensec_pos[0]+num_width + num_sep, min_pos[1]) # position of the seconds
sec_sep=(sec_pos[0]+ num_width + num_sep, min_pos[1]) # position of the decimal separator
decim_pos=(sec_sep[0]+num_sep, min_pos[1])	# position of the decimal position
success_pos=(min_pos[0]+5*num_width, min_pos[1]-num_width*2) # position of counter of successes
attempts_pos=(success_pos[0]+2*dw+num_width, success_pos[1]) # position of counter of attempts

global_timer=0
number_attempts=0
success_attempts=0


############################
# Draw the digital numbers #
############################

#Draw a dot
def draw_dot(canvas, position):
    canvas.draw_polygon([position, (position[0]+dw, position[1]), (position[0]+dw, position[1]+dw), (position[0], position[1]+dw)], 1, 'Green', 'Green')
# Draw the vertical digital segment
def draw_vert(canvas, position):
    """ Draw the vertical digital segment """
    global dw
    global dl
    canvas.draw_line((position[0], position[1]), (position[0], position[1]+dl), dw, 'Green')
    canvas.draw_polygon([(position[0]-dw/2,position[1]), (position[0]+dw/2,position[1]), (position[0],position[1]-dw/2)], 1, 'Green', 'Green')
    canvas.draw_polygon([(position[0]-dw/2,position[1]+dl), (position[0]+dw/2,position[1]+dl), (position[0],position[1]+dw/2+dl)], 1, 'Green', 'Green')
# Draw the horizontal digital segment
def draw_horiz(canvas, position):
    """ Draw the horizontal digital segment"""
    global dw
    global dl
    canvas.draw_line((position[0], position[1]), (position[0]+dl, position[1]), dw, 'Green')
    canvas.draw_polygon([(position[0],position[1]+dw/2), (position[0],position[1]-dw/2), (position[0]-dw/2,position[1])], 1, 'Green', 'Green')
    canvas.draw_polygon([(position[0]+dl,position[1]+dw/2), (position[0]+dl,position[1]-dw/2), (position[0]+dl+dw/2,position[1])], 1, 'Green', 'Green')
# Draw all the numbers
def draw_one(canvas, position):
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]+dl + 2*dw))

def draw_two(canvas, position):
    draw_vert(canvas, (position[0], position[1]+dl + 2*dw))
    draw_horiz(canvas, (position[0]+dw, position[1]-dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+dl+dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+3*dw+2*dl))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]))

def draw_three(canvas, position):
    draw_horiz(canvas, (position[0]+dw, position[1]-dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+dl+dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+3*dw+2*dl))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]+dl + 2*dw))

def draw_four(canvas, position):
    draw_vert(canvas, (position[0], position[1]))
    draw_horiz(canvas, (position[0]+dw, position[1]+dl+dw))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]+dl + 2*dw))

def draw_five(canvas, position):
    draw_vert(canvas, (position[0], position[1]))
    draw_horiz(canvas, (position[0]+dw, position[1]-dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+dl+dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+3*dw+2*dl))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]+dl + 2*dw))

def draw_six(canvas, position):
    draw_vert(canvas, (position[0], position[1]))
    draw_vert(canvas, (position[0], position[1]+dl + 2*dw))
    draw_horiz(canvas, (position[0]+dw, position[1]-dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+dl+dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+3*dw+2*dl))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]+dl + 2*dw))

def draw_seven(canvas, position):
    draw_horiz(canvas, (position[0]+dw, position[1]-dw))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]+dl + 2*dw))

def draw_eight(canvas, position):
    draw_vert(canvas, (position[0], position[1]))
    draw_vert(canvas, (position[0], position[1]+dl + 2*dw))
    draw_horiz(canvas, (position[0]+dw, position[1]-dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+dl+dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+3*dw+2*dl))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]+dl + 2*dw))

def draw_nine(canvas, position):
    draw_vert(canvas, (position[0], position[1]))
    draw_horiz(canvas, (position[0]+dw, position[1]-dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+dl+dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+3*dw+2*dl))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]+dl + 2*dw))

def draw_zero(canvas, position):
    draw_vert(canvas, (position[0], position[1]))
    draw_vert(canvas, (position[0], position[1]+dl + 2*dw))
    draw_horiz(canvas, (position[0]+dw, position[1]-dw))
    draw_horiz(canvas, (position[0]+dw, position[1]+3*dw+2*dl))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]))
    draw_vert(canvas, (position[0]+dl+2*dw, position[1]+dl + 2*dw))

def draw_min_sep(canvas):
    draw_dot(canvas, (min_sep[0], min_sep[1]+(2*dl/3)))
    draw_dot(canvas, (min_sep[0], min_sep[1]+(3*dl/2)))

def draw_sec_sep(canvas):
    draw_dot(canvas, (sec_sep[0], sec_sep[1]+2*dl+3*dw))




# Function to print convert an interger in a digital number to print
def print_number(canvas, number, position):
    if number == 0:
        draw_zero(canvas, position)
    elif number == 1:
        draw_one(canvas, position)
    elif number == 2:
        draw_two(canvas, position)
    elif number == 3:
        draw_three(canvas, position)
    elif number == 4:
        draw_four(canvas, position)
    elif number == 5:
        draw_five(canvas, position)
    elif number == 6:
        draw_six(canvas, position)
    elif number == 7:
        draw_seven(canvas, position)
    elif number == 8:
        draw_eight(canvas, position)
    elif number == 9:
        draw_nine(canvas, position)
    else:
        print "Error, incorrect time value!"

# Print timer on canvas in correct format (replace format(t) from the template)
def print_time(canvas, time):
    decim_time=time%10
    sec_time=(time//10)%10
    tensec_time=(time//100)%6
    min_time=(time-decim_time-sec_time-tensec_time)/600
    print_number(canvas, decim_time, decim_pos)
    print_number(canvas, sec_time, sec_pos)
    print_number(canvas, tensec_time, tensec_pos)
    print_number(canvas, min_time, min_pos)
    draw_min_sep(canvas)
    draw_sec_sep(canvas)

# Print the score on top right of the canvas
def print_attempts(canvas):
    global dl
    global dw
    global number_attempts
    global success_attempts
    dl/=score_ratio
    dw/=score_ratio
    print_number(canvas, number_attempts%10, attempts_pos)
    print_number(canvas, success_attempts%10, success_pos)
    canvas.draw_line((success_pos[0]+dw+num_width, success_pos[1]), (success_pos[0]+2*dw+num_width, success_pos[1]+dw+num_width), 2, 'Green')
    dw*=score_ratio
    dl*=score_ratio

# Timer functions
def reset_timer():
    global global_timer
    global success_attempts
    global number_attempts
    global_timer=0
    timer.stop()
    success_attempts=0
    number_attempts=0

def start_timer():
    timer.start()

def stop_timer():
    global global_timer
    global number_attempts
    global success_attempts
    if timer.is_running():
        timer.stop()
        number_attempts+=1
        if (global_timer%10 == 0):
            success_attempts+=1

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global global_timer
    global_timer+=1

# define draw handler
def draw(canvas):
    print_time(canvas, global_timer)
    print_attempts(canvas)


# create frame
frame = simplegui.create_frame("StopWatch", 400, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)
frame.add_button("Reset timer", reset_timer, 200)
frame.add_button("Start timer", start_timer, 200)
frame.add_button("Stop timer", stop_timer, 200)

# start frame
frame.start()

# Please remember to review the grading rubric
