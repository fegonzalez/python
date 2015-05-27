#!/usr/bin/env python3

# ==============================================================================

# Checking namespace __name__

# RESULTS:

# a) Shell execution: python3 -m namespaces
#
#    Off any function. __name__ :  __main__
#    within main. __name__ :  __main__
#    withih a local_function. __name__ :  __main__   # called inside __main__

# ==============================================================================


# __name__ = namespaces (the module's name)
print("Off any function. __name__ : ", __name__) 


# ------------------------------------------------------------------------------


# __name__ = local_function  (a local function's name)
def local_function():
    print("withih a local_function. __name__ : ", __name__) 

    
# ------------------------------------------------------------------------------


# __name__ = __main__
if __name__ == '__main__':
    print("within main. __name__ : ", __name__) # result = __main__
    local_function()

    
# ------------------------------------------------------------------------------

#EOFILE
