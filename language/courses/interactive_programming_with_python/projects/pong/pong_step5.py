# Implementation of classic arcade game Pong


# version 5: Mini-project development process steps 1-5
# http://www.codeskulptor.org/#user40_DxZ2UgqghVUKSvV_5.py

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
paddle1_pos = [0, 0]
paddle2_pos = [0, 0]
paddle1_vel = [0, 0]
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

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel, ball_acc

    ball_pos = BALL_INIT_POSITION[:]
    ball_vel = init_ball_vel(direction)
    ball_acc = BALL_INIT_ACCELERATION[:]
    print "TEST: (ball_vel)", ball_vel
    
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
    global ball_pos, ball_vel, ball_acc

    # init
    goal_right_player = False
    goal_left_player = False

    # update ball position 
    update_ball_acceleration()
    update_ball_velocity()
    ball_pos[0] += pixel2canvasrate(ball_vel[0])
    ball_pos[1] += pixel2canvasrate(ball_vel[1])
    # ball_pos[0] += ball_vel[0]
    # ball_pos[1] += ball_vel[1]
    print "TEST (update_ball): (ball_vel)", ball_vel
    
    # collide and reflect off of left-right hand side of canvas
    if ((ball_pos[0] <= BALL_RADIUS)\
        or (WIDTH-ball_pos[0] <= BALL_RADIUS)):
        handle_goal_or_paddle()
        
    # collide and reflect off of top-bottom hand side of canvas
    elif ((ball_pos[1] <= BALL_RADIUS)\
        or (HEIGHT-ball_pos[1] <= BALL_RADIUS)):
        handle_reflect_top_bottom()

#-------------------------------------------------------------------------------

def handle_reflect_top_bottom():
    ball_vel[1] = - ball_vel[1]
        
#-------------------------------------------------------------------------------

def handle_goal_or_paddle():
    
    # Case: ball surpass gutter => ball off the table (=> player scores)
    # Case: ball surpass left gutter ("right" player scores)
    if (ball_pos[0] <= BALL_RADIUS):
        # goal_right_player = True
        spawn_ball(RIGHT)
        # ball_vel[0] = - ball_vel[0]

        # case: ball surpass right gutter ("left" player scores)
    elif (WIDTH-ball_pos[0] <= BALL_RADIUS):
        # goal_left_player = True
        spawn_ball(LEFT)
        # ball_vel[0] = - ball_vel[0]

    
#-------------------------------------------------------------------------------

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # numbers
    global score1, score2  # these are ints

    spawn_ball(random.randrange(LEFT, RIGHT+1))

    

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
        
    # update ball
    update_ball()        

    # draw ball
    # WARNING Canvas refresh rate is around 60 frames/sec
    #draw_value = [pixel2canvasrate(ball_pos[0]), pixel2canvasrate(ball_pos[1])]
    # canvas.draw_circle(draw_value, BALL_RADIUS, 2, "Red", "White")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # determine whether paddle and ball collide
    
    # draw scores
    
    

    
#-------------------------------------------------------------------------------


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

frame.add_button('TEST_PAUSE', test_pause_button_handler)
frame.add_button('reset', reset_button_handler)


# create event handlers


#===============================================================================
# iv)  start Frame & Event Handlers
#===============================================================================

# start framen
new_game()
frame.start()


