# Implementation of classic arcade game Pong

import simplegui
import random

#
# INFO Units
#
# position: [pixels]
# speed: [pixels/second]
# acceleration: [pixels / (second*second)]


#===============================================================================
# Init globals
#===============================================================================



#-------------------------------------------------------------------------------
# constants
#-------------------------------------------------------------------------------

# Canvas refresh rate is around 60 frames/sec
_CANVAS_REFRESH_RATE = 60.0


# table
WIDTH  = 600   # pixels
HEIGHT = 400       

# ball+ [:]
BALL_RADIUS = 20 # pixels
BALL_INIT_POSITION = [WIDTH / 2, HEIGHT / 2]

# INFO Initial speed
#
# Design decision:
# Horizontal velocity: ball takes 2 sec. to go from left to right of the table
# thus, (table width / 2 ) pixels in 1 second,
# thus, (table width / 2 ) per 60 frames
#
# Vertical velocity: ball takes 20 sec. to go from top to bottom.
BALL_INIT_VELOCITY = [ (WIDTH/2.0) / _CANVAS_REFRESH_RATE,  \
                      (HEIGHT/20.0) / _CANVAS_REFRESH_RATE]
BALL_INIT_ACCELERATION = [0.0, 0.0]

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
paddle1_pos = [0.0, 0.0]
paddle2_pos = [0.0, 0.0]
paddle1_vel = [0.0, 0.0]
paddle2_vel = [0.0, 0.0]

# motion
score1, score2 = 0, 0  # these are ints


#===============================================================================
# define helper functions
#===============================================================================


#-------------------------------------------------------------------------------
# ball
#-------------------------------------------------------------------------------

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel, ball_acc

    ball_pos = BALL_INIT_POSITION[:]    # these are vectors stored as lists
    ball_vel = BALL_INIT_VELOCITY[:]
    if direction is LEFT:
        ball_vel[0] = - ball_vel[0]
    ball_acc = BALL_INIT_ACCELERATION[:]

    
#-------------------------------------------------------------------------------

# todo: variable acceleration.
def update_ball_acceleration():
    """ return cte acceleration = BALL_INIT_ACCELERATION = [0.0, 0.0]
    """
    global ball_acc
    return ball_acc

#-------------------------------------------------------------------------------

# todo: variable velocity
def update_ball_velocity():
    """ return cte velocity = BALL_INIT_VELOCITY = [0.0, 0.0]
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
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]


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

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], \
                     [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    update_ball()        

    # draw ball
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


#===============================================================================
# iii) create Frame & Event Handlers (timer, ...)
#===============================================================================

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# create event handlers


#===============================================================================
# iv)  start Frame & Event Handlers
#===============================================================================

# start framen
new_game()
frame.start()

