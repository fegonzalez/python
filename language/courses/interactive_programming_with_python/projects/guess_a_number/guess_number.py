
#-------------------------------------------------------------------------------
# http://www.codeskulptor.org/#user40_WRLGNBDZLASluUy.py
#-------------------------------------------------------------------------------



# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

#-------------------------------------------------------------------------------

# variables

# define secret number
MIN_SECRET_NUMBER = 0 # const
max_secret_number = 99
secret_number = MIN_SECRET_NUMBER

# define game players
human_player_guess_number = 0
# computer_guess_number = 0 # future use

#define number of guesses
max_num_guesses = 10
num_guesses = 0

    
#-------------------------------------------------------------------------------

# functions

# helper function to start and restart the game
def new_game():
    global secret_number, human_player_guess_number , num_guesses, max_num_guesses
    # global computer_guess_number
    human_player_guess_number = 0
    # computer_guess_number = 0
    num_guesses = 0
    max_num_guesses = int(math.ceil(math.log(max_secret_number - MIN_SECRET_NUMBER + 1, 2)))
    # print "DEBUG: max_num_guesses", max_num_guesses
    
    # init secret number
    secret_number = random.randrange(MIN_SECRET_NUMBER, max_secret_number+1)
    print "NEW GAME BEGINS:", "Guess a number between", \
        MIN_SECRET_NUMBER, "and", max_secret_number, "(both included)." \
                    " (",max_num_guesses-num_guesses, "guesses more )"
    
    # uncomment for debug only
    # print "DEBUG: secret_number =", secret_number
    # print "DEBUG: max_num_guesses =", max_num_guesses
    
#-------------------------------------------------------------------------------

# define event handlers for control panel
def range100():
    """ button that changes the range to [0,100) """
    global MIN_SECRET_NUMBER, max_secret_number
    MIN_SECRET_NUMBER = 0
    max_secret_number = 99
    
    # and starts a new game 
    print("\n\n\n")
    new_game()
    
#-------------------------------------------------------------------------------

def range1000():
    """ button that changes the range to [0,1000)  """
    global MIN_SECRET_NUMBER, max_secret_number
    MIN_SECRET_NUMBER = 0
    max_secret_number = 999
    
    # and starts a new game 
    print("\n\n\n")
    new_game()
    
#-------------------------------------------------------------------------------

def input_guess(guess):
    """ After each guess, your program should include in its output the number 
    of remaining guesses. Once the player has used up those guesses, they lose, 
    the game prints out an appropriate message, and a new game immediately 
    starts. """
    
    # assert(int(guess))
    global human_player_guess_number, secret_number, \
        num_guesses, max_num_guesses

    try:
        human_player_guess_number = int(guess)
        
        #handle bad input
        if (human_player_guess_number < MIN_SECRET_NUMBER) or \
           (human_player_guess_number > max_secret_number):
            print "\nOut of range  [", MIN_SECRET_NUMBER, ", ", \
                max_secret_number+1, "), try again."
            return

        #valid input
        print "\nGuess was ", human_player_guess_number
        # case: win & new game
        if(human_player_guess_number == secret_number):
            print("... Correct!")
            print("\nGAME OVER - YOU WIN")
            print("\n\n\n")
            new_game()
            return
        else:
            num_guesses += 1            
            # case: lose (max_num_guesses reached) & new game
            if(num_guesses >= max_num_guesses):
                print("\nGAME OVER - YOU LOSE (no more guesses)")
                print "The secret number was: ", secret_number
                print("\n\n\n")
                new_game()
                return
            # case: continue game
            else:
                if(human_player_guess_number < secret_number):
                    print "... Higher" \
                    " (",max_num_guesses-num_guesses, "guesses more )"
                else:
                    print "... Lower" \
                    " (", max_num_guesses-num_guesses, "guesses more )"

    except ValueError:
        print ("\nNot a valid guess, try again.")
    
#-------------------------------------------------------------------------------

# create frame
frame = simplegui.create_frame('Guess the Number Game', 200, 200)
frame.add_input("Guess the number", input_guess, 100)
frame.add_button("Range: 0 - 100", range100)
frame.add_button("Range: 0 - 1000", range1000)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

#-------------------------------------------------------------------------------

# Auto-test
#secret_number = 74	
#input_guess("50")
#input_guess("75")
#input_guess("62")
#input_guess("68")
#input_guess("71")
#input_guess("73")
#input_guess("74")
