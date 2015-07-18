
# implementation of card game - Memory


# http://www.codeskulptor.org/#user40_86vri8qi5Tl0q2l.py

 
import simplegui
import random


#===============================================================================
# helper functions
#===============================================================================


def create_memory_deck():
    l=list(range(0,8))
    l.extend(range(0,8))
    #return l.copy() #python3
    return l[:]
             

#===============================================================================
# Init globals
#===============================================================================

# constants
_DECK_SIZE = 16
_CANVAS_WIDTH = 800
_CANVAS_HEIGHT = 100
_CARD_FONT_SIZE = _CANVAS_HEIGHT/3
_CARD_FONT_COLOR = "White"
_CANVAS_WIDTH_STEP = _CANVAS_WIDTH / _DECK_SIZE
_IS_GAME_OVER = 0

# variables

#\param the_state
# 0 : init game
# 1 : 1 unexposed card
# 2 : a pair of cards has been exposed
the_state = 0

#\param the_first_card_index
# index of the first exposed card of the pair to guess on each turn
the_first_card_index = 0
the_second_card_index = 0

turns = 0
the_deck = create_memory_deck()
the_exposed_deck = [False]*len(the_deck)
assert(len(the_deck)==_DECK_SIZE)
assert(len(the_exposed_deck)==_DECK_SIZE)


game_over = _DECK_SIZE # _IS_GAME_OVER if all the cards has been paired.


#===============================================================================
# more helper functions
#===============================================================================

def new_game():
    global the_deck, the_exposed_deck, turns, the_sate, game_over
    global the_first_card_index, the_second_card_index
    
    game_over = _DECK_SIZE
    the_state = 0
    turns = 0
    the_first_card_index = 0
    the_second_card_index = 0
    random.shuffle(the_deck)
    the_exposed_deck = [False]*len(the_deck)
    assert(len(the_exposed_deck)==_DECK_SIZE)

#-------------------------------------------------------------------------------


#===============================================================================
# define event handlers
#===============================================================================
     

def set_state():
    if the_state == 0:
        return 1
    elif the_state == 1:
        return 2
    else:
        return 1    

#-------------------------------------------------------------------------------

def apply_game_rules(pos):
    
    global the_state, turns, game_over
    global the_exposed_deck
    global the_first_card_index, the_second_card_index

    index = pos[0] // _CANVAS_WIDTH_STEP

    if the_state == 1:
        # handle case: cards not paired in the previous turn
        if turns>0:
            if (the_deck[the_first_card_index] != \
                the_deck[the_second_card_index]):
                the_exposed_deck[the_second_card_index] = False
                the_exposed_deck[the_first_card_index] = False
        #handle current turn
        turns+=1
        the_first_card_index = index
        the_exposed_deck[index] = True

    elif the_state == 2:
        the_second_card_index = index
        the_exposed_deck[index] = True
        # pair found
        if (the_deck[the_first_card_index] == the_deck[the_second_card_index]):
            game_over-=2
            
#-------------------------------------------------------------------------------

def mouseclick(pos):

    global the_state

    # reset required after game over
    if game_over == _IS_GAME_OVER:
        return

    # ignore already exposed cards
    index = pos[0] // _CANVAS_WIDTH_STEP
    if the_exposed_deck[index] == True:
        return
    
    # setting the_state
    the_state = set_state()

    # actions per the_state
    apply_game_rules(pos)
    
#-------------------------------------------------------------------------------
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    xcoord = _CANVAS_WIDTH_STEP / 2
    ycoord = _CANVAS_HEIGHT - _CARD_FONT_SIZE
    FILL_COLOR = "Green"
    LINE_COLOR = "Black"
    for index in xrange(0, len(the_deck)):
        assert(xcoord <= _CANVAS_WIDTH)
        if(the_exposed_deck[index]):
           canvas.draw_text(str(the_deck[index]), (xcoord, ycoord), \
                            _CARD_FONT_SIZE, _CARD_FONT_COLOR)
        else:
            canvas.draw_polygon([(xcoord, _CANVAS_HEIGHT), (xcoord, 0)], 
                                _CANVAS_WIDTH_STEP-2, 
                                FILL_COLOR, 
                                LINE_COLOR)
        xcoord +=  _CANVAS_WIDTH_STEP

    label.set_text(str(turns))


#-------------------------------------------------------------------------------


#===============================================================================
# create frame & register event handlers
#===============================================================================

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", _CANVAS_WIDTH, _CANVAS_HEIGHT)

frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
# label = frame.add_label("Turns = " +  str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

#===============================================================================
# main loop
#===============================================================================

new_game()
frame.start()

# Always remember to review the grading rubric
