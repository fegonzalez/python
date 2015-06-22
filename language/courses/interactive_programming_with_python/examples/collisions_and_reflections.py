import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-400.0 / 60.0,  30.0 / 60.0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left-right hand side of canvas
    if ((ball_pos[0] <= BALL_RADIUS)\
        or (WIDTH-ball_pos[0] <= BALL_RADIUS)):
        vel[0] = - vel[0]
      
    # collide and reflect off of top-bottom hand side of canvas
    if ((ball_pos[1] <= BALL_RADIUS)\
        or (HEIGHT-ball_pos[1] <= BALL_RADIUS)):
        vel[1] = - vel[1]        

    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

