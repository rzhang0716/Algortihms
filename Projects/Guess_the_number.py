
import simplegui
import random
import math




# helper function to start and restart the game

num_range = 100
guess_times = 7
secret_number = 0

def new_game():
    global secret_number
    global guess_times
    global num_range
    secret_number = random.randrange(0,num_range)
    if num_range == 100:
        guess_times =7
    elif num_range == 1000:
        guess_times = 10
    

# define event handlers for control panel
def range100():
    global num_range
    global guess_times
    guess_times = 7
    num_range = 100
    new_game()

def range1000():
    global num_range
    global guess_times
    guess_times = 10
    num_range = 1000
    new_game()
    
def input_guess(guess):
    guess = int(guess)
    print('Guess was ' + str(guess))
    global guess_times
    guess_times -= 1
    if guess == secret_number:
        print('Correct, you win!')
        new_game()
    else:
        if guess_times == 0:
            print('Game over, no more try')
            print('Secret_number is ' + str(secret_number))
            new_game()
        else:
            if guess > secret_number:
                print('Higher')
            if guess < secret_number:
                print('Lower')
            print('Numbers of guess is ' + str(guess_times))

# Create the frame
frame = simplegui.create_frame('input_guess', 200, 200)
frame.add_button('new game', new_game, 100)
frame.add_button('Range is [0,100)', range100, 100)
frame.add_button('Range is [0,1000)', range1000, 100)
frame.add_input('Guess', input_guess,100)
