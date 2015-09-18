# implementation of card game - Memory

import simplegui
import random

# declaring global variables
WIDTH = 960
HEIGHT = 100

deck = [0, 1, 2, 3, 4, 5, 6, 7]
deck = deck + deck

sectors = range(60, 961, 60)

exposed = []

state = 0

first = -1
second = -1

counter = 0

# helper function to initialize globals
def new_game():
    global deck, exposed, state, first, second, counter
    random.shuffle(deck)
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    state = 0
    first = -1
    second = -1
    counter = 0
    label.set_text("Turns = 0")
    
     
# define event handlers
def mouseclick(pos):
    global state, first, second, counter
    idx = find_card(pos)
    if not exposed[idx]:
        if state == 0:
            exposed[idx] = True
            state = 1
            first = idx
        elif state == 1:
            exposed[idx] = True
            state = 2
            second = idx
            counter += 1
            label.set_text("Turns = " + str(counter))
        else:
            if deck[first] != deck[second]:
                exposed[first] = False
                exposed[second] = False
            exposed[idx] = True
            state = 1
            first = idx
        
def find_card(pos):
    i = 0
    found = False
    while not found:
        if pos[0] < sectors[i]:
            found = True
        else:
            i += 1
    return i
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(1, 16):
        canvas.draw_line([i * 60, 0], [i * 60, HEIGHT], 2, "Red")
    for i in range(16):
        if exposed[i]:
            canvas.draw_polygon([(i * 60, 0), ((i + 1) * 60, 0), ((i + 1) * 60, HEIGHT), (i * 60, HEIGHT)], 2, "Red", "Black")
            canvas.draw_text(str(deck[i]), [(i * 60) + 15, 70], 60, "White")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.set_canvas_background("Green")
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
