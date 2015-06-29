# Implementation of classic arcade game Pong

# PESENTED TO EVALUATION ( 2 minor fixed since)
# http://www.codeskulptor.org/#user40_KRnw9klLGfVvziz.py

#
# NOTICE Game additions:
#
# 1) increase/decrease paddle velocity
#
# The players can modify the speed of their paddles by keyboard:
#
# paddle 1 increase velocity key  = "e"
# paddle 1 decrease velocity key  = "d"
# paddle 2 increase velocity key  = "right"
# paddle 2 decrease velocity key  = "left"
#
# In addition, the updated value is remembered between games.


import simplegui
import random

#===============================================================================
# Init globals
#===============================================================================

# INFO Units (unless otherwise specified)
#
# position: [pixels]
# velocity: [pixels/second] 


#-------------------------------------------------------------------------------
# constants
#-------------------------------------------------------------------------------

# Canvas
_CANVAS_REFRESH_RATE = 60 # Canvas refresh rate is around 60 frames/sec

# table
WIDTH  = 600
HEIGHT = 400       

# ball
BALL_RADIUS = 20 # pixels
BALL_INIT_POSITION = [WIDTH / 2, HEIGHT / 2]
BALL_INIT_VELOCITY = [0, 0]
BALL_MIN_INIT_X_VEL = 120
BALL_MAX_INIT_X_VEL = 240
BALL_MIN_INIT_Y_VEL = 60
BALL_MAX_INIT_Y_VEL= 180
BALL_DEFAULT_VEL_FACTOR = 1.1 # 10%

# paddles
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT_PADDLE_HORIZ_POSITION = HALF_PAD_WIDTH
RIGHT_PADDLE_HORIZ_POSITION= WIDTH - HALF_PAD_WIDTH
# keep paddles on the screen
PADDLE_TOP_POS = HALF_PAD_HEIGHT
PADDLE_BOTTOM_POS = HEIGHT - HALF_PAD_HEIGHT
# paddle velocity range
PADDLE_X_VEL = 0
PADDLE_DEFAULT_VERT_VELOCITY = 60 # see pixel2canvasrate WARNING
# increase/decrease paddle velocity
MIN_PADDLE_VEL_FACTOR = 1
MAX_PADDLE_VEL_FACTOR = 10
INIT_PADDLE_VEL_FACTOR = 4
# paddle controls
# NICETOHAVE configurable controls by the user.
DEFAULT_PADDLE1_UP_KEY      = "w"
DEFAULT_PADDLE1_DOWN_KEY    = "s"
DEFAULT_PADDLE1_INCVEL_KEY  = "e"
DEFAULT_PADDLE1_DECVEL_KEY  = "d"
DEFAULT_PADDLE2_UP_KEY      = "up"
DEFAULT_PADDLE2_DOWN_KEY    = "down"
DEFAULT_PADDLE2_INCVEL_KEY  = "right"
DEFAULT_PADDLE2_DECVEL_KEY  = "left"

# motion
LEFT = False
RIGHT = True

# scores
_SCORE1_X_COORD = WIDTH/2 * 0.75
_SCORE1_Y_COORD = HEIGHT/2 * 0.30
_SCORE2_X_COORD = WIDTH/2 * 1.20
_SCORE2_Y_COORD = _SCORE1_Y_COORD
_SCORE_FONT_SIZE  = 40
_SCORE_FONT_COLOR = "white"
_SCORE_FONT_FACE = "serif"

     
#-------------------------------------------------------------------------------
# variables 
#-------------------------------------------------------------------------------

# table

# ball
ball_pos = BALL_INIT_POSITION[:]    # these are vectors stored as lists
ball_vel = BALL_INIT_VELOCITY[:]

# paddles
# pos and vel encode vertical info for paddles
paddle1_pos = [0, 0] # vertical distance of left paddle from top
paddle2_pos = [0, 0]
paddle1_vel = [0, 0] # vertical velocity of left paddle
paddle2_vel = [0, 0]
# paddle velocity = PADDLE_DEFAULT_VERT_VELOCITY * paddle_vel_K_factor
paddle1_vel_K_factor = INIT_PADDLE_VEL_FACTOR
paddle2_vel_K_factor = INIT_PADDLE_VEL_FACTOR
# paddle controls
# NICETOHAVE configurable controls by the user.
paddle1_up_key = DEFAULT_PADDLE1_UP_KEY
paddle1_down_key = DEFAULT_PADDLE1_DOWN_KEY
paddle1_incvel_key = DEFAULT_PADDLE1_INCVEL_KEY
paddle1_decvel_key = DEFAULT_PADDLE1_DECVEL_KEY
paddle2_up_key = DEFAULT_PADDLE2_UP_KEY
paddle2_down_key = DEFAULT_PADDLE2_DOWN_KEY
paddle2_incvel_key = DEFAULT_PADDLE2_INCVEL_KEY
paddle2_decvel_key = DEFAULT_PADDLE2_DECVEL_KEY
#handle multi-key pressed
paddle1_up_key_pressed = False
paddle1_down_key_pressed = False
paddle2_up_key_pressed = False
paddle2_down_key_pressed = False

# motion
score1, score2 = 0, 0  # these are ints

# test purpose
test_paused = False


#===============================================================================
# define helper functions
#===============================================================================

def pixel2canvasrate(value):
    """Transforming a position from pixels/second to the canvas refresh rate
    (around 60 frames/sec)

    WARNING 1: (value / _CANVAS_REFRESH_RATE) is an integer division in Python2
    => if value < 60 always returns 0:
    return 0 if value in [0, 60)
    return 1 if value in [60, 120)
    ...

    WARNING 2: 'value_sign' used to resolve a Python 2 issue: different result
    depending on the value sign; caused by the integer division:
    >>> pixel2canvasrate(119) 
    1 
    >>> pixel2canvasrate(-119) 
    -2

    With this solution, pixel2canvasrate(119) == 1, and pixel2canvasrate(119)
    == -1

    """
    assert (isinstance(value, (int, float)))
    if value>=0:
        value_sign = 1
    else:
        value_sign = -1
    return (abs(value) / _CANVAS_REFRESH_RATE) * value_sign

#-------------------------------------------------------------------------------

def limit_paddle_vel_factor(new_value):
    """ return a value for paddle1_vel_K_factor or paddle2_vel_K_factor in the 
range [MIN_PADDLE_VEL_FACTOR, MAX_PADDLE_VEL_FACTOR] """

    if (new_value <= MIN_PADDLE_VEL_FACTOR):
        return MIN_PADDLE_VEL_FACTOR
    elif(new_value >= MAX_PADDLE_VEL_FACTOR):
        return MAX_PADDLE_VEL_FACTOR
    else:
        return new_value

    
#-------------------------------------------------------------------------------
# ball
#-------------------------------------------------------------------------------
        
def init_ball_vel(direction):
    """ return velocity vector to init a new play. 
    In the range:
    Horizontal velocity: 120 - 240 pixels per second
    Vertical velocity:  60 - 180 pixels per second
    """
    if direction is LEFT:
        K_HORIZ = - 1
    else:
        K_HORIZ = 1
    if (random.randrange(0,2)==0):
        K_VERT = - 1
    else:
        K_VERT = 1

    return [random.randrange(BALL_MIN_INIT_X_VEL, BALL_MAX_INIT_X_VEL+1) \
            * K_HORIZ, \
            random.randrange(BALL_MIN_INIT_Y_VEL, BALL_MAX_INIT_Y_VEL+1) \
            * K_VERT]

#-------------------------------------------------------------------------------

def update_ball(): 
    """ Update ball position according to the canvas refresh rate (60
    frames/sec) """

    global ball_pos, ball_vel
    
    # update ball position
    ball_pos[0] += pixel2canvasrate(ball_vel[0])
    ball_pos[1] += pixel2canvasrate(ball_vel[1])
        
    # collide and reflect off of the top and bottom walls.
    if ((ball_pos[1] <= BALL_RADIUS) or (HEIGHT-ball_pos[1] <= BALL_RADIUS)):
        handle_reflect_top_bottom()

#-------------------------------------------------------------------------------

def handle_reflect_top_bottom():
    ball_vel[1] = - ball_vel[1]
        
#-------------------------------------------------------------------------------

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel

    ball_pos = BALL_INIT_POSITION[:]
    ball_vel = init_ball_vel(direction)

#-------------------------------------------------------------------------------

def init_paddles():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # numbers

    paddle1_pos = [LEFT_PADDLE_HORIZ_POSITION, HEIGHT / 2]
    paddle2_pos = [RIGHT_PADDLE_HORIZ_POSITION , HEIGHT / 2]
    paddle1_vel = [PADDLE_X_VEL, 0] # vertical velocity of left paddle
    paddle2_vel = [PADDLE_X_VEL, 0]
    # NOTICE design decision: paddle velocity remembered between games
    # paddle1_vel_K_factor = INIT_PADDLE_VEL_FACTOR
    # paddle2_vel_K_factor = INIT_PADDLE_VEL_FACTOR

#-------------------------------------------------------------------------------

def update_paddles():
    """ Update paddle's vertical position according to the canvas refresh rate
    (60 frames/sec) and keeping paddles on the screen"""

    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel

    paddle1_pos[1] += pixel2canvasrate(paddle1_vel[1])
    paddle2_pos[1] += pixel2canvasrate(paddle2_vel[1])
    #print "TEST (update_paddles): (paddle)", paddle1_pos[1], paddle2_pos[1]
    
    # keep paddles on the screen
    # collide and reflect off of top-bottom hand side of canvas
    if (paddle1_pos[1] < PADDLE_TOP_POS):
        paddle1_pos[1] = PADDLE_TOP_POS
    elif (paddle1_pos[1] > PADDLE_BOTTOM_POS):
        paddle1_pos[1] = PADDLE_BOTTOM_POS
    if (paddle2_pos[1] < PADDLE_TOP_POS):
        paddle2_pos[1] = PADDLE_TOP_POS
    elif (paddle2_pos[1] > PADDLE_BOTTOM_POS):
        paddle2_pos[1] = PADDLE_BOTTOM_POS
        
#-------------------------------------------------------------------------------

def handle_goal_or_paddle():
    """ Handle Case: ball surpass gutter => strike the ball or score .
        On strike: increase the velocity of the ball & reflect the ball.
        On goal: increase the score of the goaler.
    """
    global score1, score2, ball_pos, ball_vel, paddle1_pos, paddle2_pos
    
    # Case: ball surpass left gutter ("right" player scores)
    if (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)):
        # strike! => reflect the ball
        if(ball_pos[1] >= (paddle1_pos[1] - HALF_PAD_HEIGHT)) and \
          (ball_pos[1] <= (paddle1_pos[1] + HALF_PAD_HEIGHT)):
           ball_vel[0] = - ball_vel[0] * BALL_DEFAULT_VEL_FACTOR
           ball_vel[1] *= BALL_DEFAULT_VEL_FACTOR
        # goal!
        else: 
            score2+=1
            new_play(RIGHT)
           
    # case: ball surpass right gutter ("left" player scores)
    elif ball_pos[0] >= (WIDTH-1) - (PAD_WIDTH + BALL_RADIUS):
        # strike! => reflect the ball
        if(ball_pos[1] >= (paddle2_pos[1] - HALF_PAD_HEIGHT)) and \
          (ball_pos[1] <= (paddle2_pos[1] + HALF_PAD_HEIGHT)):
           ball_vel[0] = - ball_vel[0] * BALL_DEFAULT_VEL_FACTOR
           ball_vel[1] *= BALL_DEFAULT_VEL_FACTOR
        # goal!
        else:
            score1+=1
            new_play(LEFT)

#-------------------------------------------------------------------------------

def new_play(direction):
    init_paddles()        
    spawn_ball(direction)
    
#-------------------------------------------------------------------------------

def new_game():
    global score1, score2  # these are ints

    score1, score2 = 0, 0
    new_play(random.choice([LEFT, RIGHT]))
    # new_play(random.randrange(LEFT, RIGHT+1)) #not working, always to right


#===============================================================================
# define event handlers
#===============================================================================


#-------------------------------------------------------------------------------
# draw
#-------------------------------------------------------------------------------

def draw(canvas):

    global ball_pos

    if(test_paused):
        return
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], \
                     [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    update_ball()        
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    update_paddles()
    draw_paddles(canvas)
    
    handle_goal_or_paddle() # determine whether paddle and ball collide

    draw_score(canvas)
    
#-------------------------------------------------------------------------------

def draw_paddles(canvas):

    global paddle1_pos, paddle2_pos

    pad1_p1 = [(paddle1_pos[0]), \
               (paddle1_pos[1] + HALF_PAD_HEIGHT)]
    pad1_p2 = [(paddle1_pos[0]), \
               (paddle1_pos[1] - HALF_PAD_HEIGHT)]
    pad2_p1 = [(paddle2_pos[0]), \
               (paddle2_pos[1] + HALF_PAD_HEIGHT)]
    pad2_p2 = [(paddle2_pos[0]), \
               (paddle2_pos[1] - HALF_PAD_HEIGHT)]
    canvas.draw_polygon([pad1_p1, pad1_p2], PAD_WIDTH, 'Yellow')
    canvas.draw_polygon([pad2_p1, pad2_p2], PAD_WIDTH, 'Yellow')
    
#-------------------------------------------------------------------------------

# draw timer
def draw_score(canvas):

    global score1, score2

    canvas.draw_text(str(score1), \
                    (_SCORE1_X_COORD, _SCORE1_Y_COORD), \
                     _SCORE_FONT_SIZE, _SCORE_FONT_COLOR, _SCORE_FONT_FACE)

    canvas.draw_text(str(score2), \
                    (_SCORE2_X_COORD, _SCORE2_Y_COORD), \
                     _SCORE_FONT_SIZE, _SCORE_FONT_COLOR, _SCORE_FONT_FACE)


#-------------------------------------------------------------------------------
# keyboard
#-------------------------------------------------------------------------------
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_vel_K_factor, paddle2_vel_K_factor
    """ Paddle movement: 
    velocity can be increased/decreases via keyboard.

    # handle paddle movement
    player 1 up/down: paddle1_up_key / paddle1_down_key pressed.
    player 2 up/down: paddle2_up_key / paddle2_down_key pressed.
    exception: if both up & down keys are pressed, action ignored.

    # handle increase/decrease paddle speed
    player 1 up/down: paddle1_incvel_key/paddle1_decvel_key pressed
    player 2 up/down: paddle2_incvel_key/paddle2_decvel_key pressed """

    # handle paddle movement
    if (key==simplegui.KEY_MAP[paddle1_up_key] or \
        key==simplegui.KEY_MAP[paddle1_down_key]):
        keydown_paddle1_handler(key)

    elif (key==simplegui.KEY_MAP[paddle2_up_key] or \
        key==simplegui.KEY_MAP[paddle2_down_key]):
        keydown_paddle2_handler(key)

    # handle increase/decrease paddle speed
    elif key==simplegui.KEY_MAP[paddle1_incvel_key]:
        paddle1_vel_K_factor = limit_paddle_vel_factor(paddle1_vel_K_factor+1)
    elif key==simplegui.KEY_MAP[paddle1_decvel_key]:
        paddle1_vel_K_factor = limit_paddle_vel_factor(paddle1_vel_K_factor-1)

    elif key==simplegui.KEY_MAP[paddle2_incvel_key]:
        paddle2_vel_K_factor = limit_paddle_vel_factor(paddle2_vel_K_factor+1)
    elif key==simplegui.KEY_MAP[paddle2_decvel_key]:
        paddle2_vel_K_factor = limit_paddle_vel_factor(paddle2_vel_K_factor-1)

#-------------------------------------------------------------------------------
        
def keydown_paddle1_handler(key):
    global paddle1_vel, paddle1_up_key_pressed, paddle1_down_key_pressed
    global paddle1_vel_K_factor, paddle2_vel_K_factor
    
    if (paddle1_up_key_pressed and key==simplegui.KEY_MAP[paddle1_down_key]):
        return
    if (paddle1_down_key_pressed and key==simplegui.KEY_MAP[paddle1_up_key]):
        return
    
    if key==simplegui.KEY_MAP[paddle1_up_key]:
        paddle1_up_key_pressed = True
        paddle1_vel[1] = -PADDLE_DEFAULT_VERT_VELOCITY * paddle1_vel_K_factor
    elif key==simplegui.KEY_MAP[paddle1_down_key]:
        paddle1_down_key_pressed = True
        paddle1_vel[1] = PADDLE_DEFAULT_VERT_VELOCITY * paddle1_vel_K_factor

#-------------------------------------------------------------------------------

def keydown_paddle2_handler(key):
    global paddle2_vel, paddle2_up_key_pressed, paddle2_down_key_pressed
    global paddle1_vel_K_factor, paddle2_vel_K_factor

    if (paddle2_up_key_pressed and key==simplegui.KEY_MAP[paddle2_down_key]):
        return
    if (paddle2_down_key_pressed and key==simplegui.KEY_MAP[paddle2_up_key]):
        return
    
    if key==simplegui.KEY_MAP[paddle2_up_key]:
        paddle2_up_key_pressed = True
        paddle2_vel[1] = -PADDLE_DEFAULT_VERT_VELOCITY  * paddle2_vel_K_factor
    elif key==simplegui.KEY_MAP[paddle2_down_key]:
        paddle2_down_key_pressed = True
        paddle2_vel[1] = PADDLE_DEFAULT_VERT_VELOCITY * paddle2_vel_K_factor
                    
#-------------------------------------------------------------------------------

def keyup(key):
    """Paddle movement: A player instantaneously stops (velocity=0) its current
    up/down movement by releasing the up/down key currently pressed.
    """

    if (key==simplegui.KEY_MAP[paddle1_up_key] or \
        key==simplegui.KEY_MAP[paddle1_down_key]):
        keyup_paddle1_handler(key)
    if (key==simplegui.KEY_MAP[paddle2_up_key] or \
        key==simplegui.KEY_MAP[paddle2_down_key]):
        keyup_paddle2_handler(key)

#-------------------------------------------------------------------------------

def keyup_paddle1_handler(key):
    global paddle1_vel, paddle1_up_key_pressed, paddle1_down_key_pressed

    if (paddle1_up_key_pressed and key==simplegui.KEY_MAP[paddle1_down_key]):
        return
    if (paddle1_down_key_pressed and key==simplegui.KEY_MAP[paddle1_up_key]):
        return
    
    if key==simplegui.KEY_MAP[paddle1_up_key]:
        paddle1_up_key_pressed = False
        paddle1_vel[1] = 0
    elif key==simplegui.KEY_MAP[paddle1_down_key]:
        paddle1_down_key_pressed = False
        paddle1_vel[1] = 0

#-------------------------------------------------------------------------------

def keyup_paddle2_handler(key):
    global paddle2_vel, paddle2_up_key_pressed, paddle2_down_key_pressed

    if (paddle2_up_key_pressed and key==simplegui.KEY_MAP[paddle2_down_key]):
        return
    if (paddle2_down_key_pressed and key==simplegui.KEY_MAP[paddle2_up_key]):
        return
    
    if key==simplegui.KEY_MAP[paddle2_up_key]:
        paddle2_up_key_pressed = False
        paddle2_vel[1] = 0
    elif key==simplegui.KEY_MAP[paddle2_down_key]:
        paddle2_down_key_pressed = False
        paddle2_vel[1] = 0

#-------------------------------------------------------------------------------

def test_pause_button_handler():
    global test_paused
    test_paused = not test_paused

#-------------------------------------------------------------------------------

def reset_button_handler():
    """ calls new_game to reset the score and relaunch the ball. """
    new_game()

    
#===============================================================================
# iii) create Frame & Event Handlers (timer, ...)
#===============================================================================

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('Restart', reset_button_handler, 80)
# frame.add_button('TEST_PAUSE', test_pause_button_handler)

# create event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


#===============================================================================
# iv)  start Frame & Event Handlers
#===============================================================================

# start frame
new_game()
frame.start()


#EOFILE
