# template for "Stopwatch: The Game"

import simplegui


#---------------------------------------------------------------    
# define global variables
#---------------------------------------------------------------    

# frame constants
_FRAME_WIDTH = 300.0
_FRAME_HEIGHT = 200.0

# tries counter
tries_success = 0 # number of successes
tries_total = 0   # number of tries

#_TRIES_X_COORD = _FRAME_WIDTH - 80 # left align to: XXX/YYY
_TRIES_X_COORD = _FRAME_WIDTH - 60  # left align to: XX/YY
_TRIES_Y_COORD = 24
_TRIES_FONT_SIZE =  24
_TRIES_FONT_COLOR = "green"
_TRIES_FONT_FACE = "serif"

# timer counter: count time in tenths of seconds
the_time_counter = 0
_TIMER_FONT_SIZE =  40
_TIMER_MSG_LEN = 6 # M:SS:T
_TIMER_X_COORD = (_FRAME_WIDTH / 2) - \
                 (_TIMER_MSG_LEN * (_TIMER_FONT_SIZE/5))
_TIMER_Y_COORD = (_FRAME_HEIGHT / 2) + (_TIMER_FONT_SIZE/4)


_TIMER_FONT_COLOR = "white"
_TIMER_FONT_FACE = "serif"


#---------------------------------------------------------------    
# Helper functions
#---------------------------------------------------------------


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    seconds = (t//10)%60
    minutes = (t//10) // 60
    if minutes >= 10:
        minutes = 0
    retval = str(minutes)+":"
    if seconds<10:
        retval+="0"
    retval+= str(seconds)+"."+str(tenths)
    return retval

#---------------------------------------------------------------

def check_try():
    """ Check the play result: 
    """
    global the_time_counter, tries_total, tries_success
    tries_total+=1
    if the_time_counter % 10 == 0:
        tries_success+=1
        
        
#---------------------------------------------------------------    
# Event Handlers
#---------------------------------------------------------------

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    global the_timer
    the_timer.start()
    
#---------------------------------------------------------------


def stop_button_handler():
    global the_timer
    if the_timer.is_running():
        the_timer.stop()
        check_try()
        
#------------------------------------------------------------------------------

def reset_button_handler():
    global the_timer, tries_total, tries_success, the_time_counter

    the_timer.stop()
    the_time_counter = 0
    tries_total, tries_success = 0, 0

#------------------------------------------------------------------------------

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global the_time_counter
    the_time_counter+=1

#---------------------------------------------------------------

# define draw handler
def draw_handler(canvas):
    #canvas.draw_text(text, point, font_size, font_color, font_face)

    #canvas.draw_text('C', (80, 50), 12, 'Gray', 'serif')

    # draw timer
    canvas.draw_text(format(the_time_counter), \
                     (_TIMER_X_COORD, _TIMER_Y_COORD), \
                     _TIMER_FONT_SIZE, _TIMER_FONT_COLOR, _TIMER_FONT_FACE)

    #draw tries
    canvas.draw_text(str(tries_success) + "/" + str(tries_total), \
                     (_TRIES_X_COORD, _TRIES_Y_COORD), \
                     _TRIES_FONT_SIZE, _TRIES_FONT_COLOR, _TRIES_FONT_FACE)


#---------------------------------------------------------------

# create frame
the_frame = simplegui.create_frame("Stopwatch: The Game", \
                                   _FRAME_WIDTH, _FRAME_HEIGHT)
start_button = the_frame.add_button('Start', start_button_handler, 50)
stop_button = the_frame.add_button('Stop', stop_button_handler, 50)
reset_button = the_frame.add_button('Reset', reset_button_handler, 50)

# register event handlers
the_frame.set_draw_handler(draw_handler)
the_timer = simplegui.create_timer(100.0, timer_handler)

# start frame
the_frame.start()


# Please remember to review the grading rubric
