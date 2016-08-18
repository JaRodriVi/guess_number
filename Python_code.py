# guess_number
# A game, consist in guess the number
# Python Code

import math
import random
import simplegui

num_range=100
cpu_num = 0

message = " "

lower = "Lower"
higher = "Higher"
correct = "Correct"

# helper function to start and restart the game
def new_game():
    global cpu_num
    
    cpu_num= random.randint(1,num_range)
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global message
    
    guess = int(guess)
    
    if guess < cpu_num:
        message = higher
        print higher
        
    elif guess > cpu_num:
        message=lower
        print lower
        
    else:
        message = correct
        new_game()
        
        
def draw(canvas):
    canvas.draw_text(message, (60, 100), 30, 'Red')
    
# create frame
f=simplegui.create_frame("Guess Number",200,200)

# register event handlers for control elements and start frame
f.add_button("Range=100", range100,100)
f.add_button("Range=1000", range1000,100)

f.add_input("Enter number:", input_guess, 100)

f.set_draw_handler(draw)

# call new_game 
new_game()

f.start()
# always remember to check your completed program against the grading rubric
