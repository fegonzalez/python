# Implementation of classic arcade game Pong


# version 6: Pong Mini-project development process steps 1-6
# http://www.codeskulptor.org/#user40_DxZ2UgqghVUKSvV_5.py
# http://www.codeskulptor.org/#user40_vjMEj9l5ti4HDLX.py


# version 8: Pong Mini-project development process steps 1-8 & 10
# http://www.codeskulptor.org/#user40_dzJg5RxM4SrUMAM.py

import simplegui
import random


#===============================================================================
# Init globals
#===============================================================================

#
# INFO Units (unless otherwise specified)
#
# position: [pixels]
# velocity: [pixels/second] 
# acceleration: [pixels/second**2] 
# 


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
BALL_INIT_ACCELERATION = [0, 0]
BALL_MIN_INIT_X_VEL = 120
BALL_MAX_INIT_X_VEL = 240
BALL_MIN_INIT_Y_VEL = 60
BALL_MAX_INIT_Y_VEL= 180


# paddles
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT_PADDLE_HORIZ_POSITION = HALF_PAD_WIDTH
RIGHT_PADDLE_HORIZ_POSITION= WIDTH - HALF_PAD_WIDTH
PADDLE_X_VEL = 0
# keep paddles on the screen
PADDLE_TOP_POS = HALF_PAD_HEIGHT
PADDLE_BOTTOM_POS = HEIGHT - HALF_PAD_HEIGHT

        
# motion
LEFT = False
RIGHT = True


#-------------------------------------------------------------------------------
# variables 
#-------------------------------------------------------------------------------

# table

# ball
ball_pos = BALL_INIT_POSITION[:]    # these are vectors stored as lists
ball_vel = BALL_INIT_VELOCITY[:]
ball_acc = BALL_INIT_ACCELERATION[:]

# paddles
# pos and vel encode vertical info for paddles
paddle1_pos = [0, 0] # vertical distance of left paddle from top
paddle2_pos = [0, 0]
paddle1_vel = [0, 0] # vertical velocity of left paddle
paddle2_vel = [0, 0]

# motion
score1, score2 = 0, 0  # these are ints

# test purpose
test_paused = False

#===============================================================================
# define helper functions
#===============================================================================


def pixel2canvasrate(value):
    """Update a position updated in pixels/second to the canvas refresh rate
    (around 60 frames/sec)
    """
    assert (isinstance(value, (int, float)))
    return value / _CANVAS_REFRESH_RATE



#-------------------------------------------------------------------------------
# ball
#-------------------------------------------------------------------------------
        
#-------------------------------------------------------------------------------

def init_ball_vel(direction):
    """ return velocity vector to init a new play. 
    In the range:
    Horizontal velocity: 120 - 240 pixels per second
    Vertical velocity:  60 - 180 pixels per second
    """
    # global ball_acc

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
            random.randrange(BALL_MIN_INIT_X_VEL, BALL_MAX_INIT_X_VEL+1) \
            * K_VERT]

#-------------------------------------------------------------------------------

# todo: variable acceleration.
def update_ball_acceleration():
    """ return cte acceleration = BALL_INIT_ACCELERATION = [0, 0]
    """
    global ball_acc
    return ball_acc

#-------------------------------------------------------------------------------

# todo: variable velocity
def update_ball_velocity():
    """ return cte velocity = BALL_INIT_VELOCITY = [0, 0]
    """
    global ball_acc, ball_vel
    return ball_vel

#-------------------------------------------------------------------------------

def update_ball(): 
    """ Update ball position according to the canvas refresh rate (60
    frames/sec) """

    global ball_pos, ball_vel, ball_acc

    # update ball position
    update_ball_acceleration()
    update_ball_velocity()
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
    global ball_pos, ball_vel, ball_acc

    ball_pos = BALL_INIT_POSITION[:]
    ball_vel = init_ball_vel(direction)
    ball_acc = BALL_INIT_ACCELERATION[:]
    #print "TEST: spawn_ball: pos, vel: ", ball_pos, ball_vel

#-------------------------------------------------------------------------------

def init_paddles():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # numbers

    paddle1_pos = [LEFT_PADDLE_HORIZ_POSITION, HEIGHT / 2]
    paddle2_pos = [RIGHT_PADDLE_HORIZ_POSITION , HEIGHT / 2]
    paddle1_vel = [PADDLE_X_VEL, 0] # vertical velocity of left paddle
    paddle2_vel = [PADDLE_X_VEL, 0]

#-------------------------------------------------------------------------------

# todo: variable velocity
def update_paddles_velocity():
    """ return cte velocity = BALL_INIT_VELOCITY = [0, 0]
    """

    global paddle1_vel, paddle2_vel

    paddle1_vel[1] = 0 # todo: FIXME make variable
    paddle2_vel[1] = 0
    

#-------------------------------------------------------------------------------

def update_paddles():
    """ Update paddle's vertical position according to the canvas refresh rate
    (60 frames/sec) and keeping paddles on the screen"""

    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel

# paddle1_pos = [0, 0] # vertical distance of left paddle from top
# paddle2_pos = [0, 0]
# paddle1_vel = [0, 0] # vertical velocity of left paddle
# paddle2_vel = [0, 0]

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

    #todo handel goal
    goal_right_player = False
    goal_left_player = False
    
    # Case: ball surpass gutter => ball off the table (=> player scores)
    # Case: ball surpass left gutter ("right" player scores)
    if (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)):
        # goal_right_player = True
        new_play(RIGHT)
        # ball_vel[0] = - ball_vel[0]

        # case: ball surpass right gutter ("left" player scores)
    elif (WIDTH-ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)):
        # goal_left_player = True
        new_play(LEFT)
        # ball_vel[0] = - ball_vel[0]
        
#-------------------------------------------------------------------------------

def new_play(direction):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # numbers
    global score1, score2  # these are ints

    init_paddles()        
    spawn_ball(direction)

#-------------------------------------------------------------------------------

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # numbers
    global score1, score2  # these are ints

    new_play(random.randrange(LEFT, RIGHT+1))


    


        

#===============================================================================
# define event handlers
#===============================================================================


#-------------------------------------------------------------------------------
# draw
#-------------------------------------------------------------------------------


def draw(canvas):

    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    if(test_paused):
        return
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], \
                     [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update & draw ball
    update_ball()        
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update & draw paddles
    update_paddles()
    draw_paddles(canvas)
    
    # determine whether paddle and ball collide
    handle_goal_or_paddle()    

    # draw scores
    
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
# keyboard
#-------------------------------------------------------------------------------
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    pass

#-------------------------------------------------------------------------------

def keyup(key):
    global paddle1_vel, paddle2_vel
    pass

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
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button('Restart', reset_button_handler, 80)
frame.add_button('TEST_PAUSE', test_pause_button_handler)



# create event handlers


#===============================================================================
# iv)  start Frame & Event Handlers
#===============================================================================

# start framen
new_game()
frame.start()

