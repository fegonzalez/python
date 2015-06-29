

# change the globals below to TRUE to have the computer play as player 1
# and/or player 2 (which was very useful to debug the program)

PLAYER1_IS_COMPUTER = False
PLAYER2_IS_COMPUTER = False

#---------------------------------------------------------------------------

if PLAYER1_IS_COMPUTER:
        # player 1 is a computer
        paddle1_pos = computer_paddle(RIGHT, paddle1_pos)
    else:
        # player 1 is a human; use the velocity set by the user
        paddle1_pos += paddle1_vel

#---------------------------------------------------------------------------

def computer_paddle(side, paddle_pos):
    """computer plays player 1 or player 2"""

    # the ball goes towards the player: computer tries to follow it
    if ((side == RIGHT) and (ball_vel[0] < 0)) or ((side == LEFT) and (ball_vel[0] > 0)):
        if abs(paddle_pos - ball_pos[1]) <= HALF_PAD_HEIGHT:
            pass
        elif paddle_pos < ball_pos[1]:
            paddle_pos += PADDLE_VEL
        elif paddle_pos > ball_pos[1]:
            paddle_pos -= PADDLE_VEL

    # the ball goes away from the player: computer goes toward the center
    elif ((side == RIGHT) and (ball_vel[0] > 0)) or ((side == LEFT) and (ball_vel[0] < 0)):
        if abs(paddle_pos - HEIGHT / 2) <= HALF_PAD_HEIGHT:
            pass
        elif paddle_pos < HEIGHT / 2:
            paddle_pos += PADDLE_VEL
        elif paddle_pos > HEIGHT / 2:
            paddle_pos -= PADDLE_VEL

    return paddle_pos

#---------------------------------------------------------------------------

