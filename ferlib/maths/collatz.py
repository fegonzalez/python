# The Collatz conjecture
#
# Given any initial natural number, 
#consider the sequence of numbers generated by repeatedly 
#following the rule:
#
#divide by two if the number is even or
#multiply by 3 and add 1 if the number is odd.
#The Collatz conjecture states that this sequence always 
#terminates at 1. For example, the sequence generated by 23 is:
# 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1

import simplegui

# global state

result = 1
iteration = 0
max_iterations = 160

# helper functions

def init(start):
    """Initializes n."""
    global the_n, result
    the_n = start
    print "Input is", the_n
    result = the_n
    
def get_next(current):
    if (current%2==0):
        print "par", current/2
        return current/2
    else:
        print "impar", (3.0 * current) + 1
        return (3.0 * current) + 1

# timer callback

def update():
    global iteration, result
    iteration += 1
    # Stop iterating after max_iterations
    if iteration >= max_iterations:
        timer.stop()
        print "Output is", result
    else:
        result = get_next(result)
        print result

# register event handlers

timer = simplegui.create_timer(1, update)

# start program
init(23)
timer.start()