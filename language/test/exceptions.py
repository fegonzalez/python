#!/usr/bin/env python3

# Testing Exceptions in Python

import sys

##------------------------------------------------------------------------------

def assertions():
    """ assertException
    """
    retval = 1

    assert(False)
            
    print("se imrime esto???????????????????????")
    
    try:
        print("dentro del try....................")

    except:
        print("cazada la exception", sys.exc_info()[0])

    return retval


def call_assertions():

    return assertions()
    
##------------------------------------------------------------------------------

def value_error():
    """ simple exception 
    """
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
##------------------------------------------------------------------------------

def all_errors():
    """ multiple exception catcher example.
    """
    total=0

    try:
        local_file = open("exceptions_all_errors_dummy.txt", "w")
        local_file.write("Empezamos: \n")
        
        while True:

            #-------- INNER try clause - begin ------
            try:
                x = int(input("Please enter a number (CTRL-C to abort): "))
                total+=x;
                local_file.write(str(x))
                # break

            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

            # """ exceptions name (with arguments) clause """
            except KeyboardInterrupt as err: 
                print(" \n...Program interrupted by the user. {0}".format(err))
                print(" ...Exception arguments: {0}".format(err.args))
                break

            # """ tuple clause """
            except (RuntimeError, TypeError, NameError):
                pass

            # """ catch-all clause """
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise

            else: # executed iff no exception raised
                print("(else clause) Sum of loaded values = {0}".format(total))
                local_file.write("\n")

            #-------- INNER try clause - end ------
  
    # """ catch-all clause """
    except:
        print("Unexpected error (openning file):", sys.exc_info()[0])
        print("...Exception arguments:", sys.exc_info()[1])
        return;
           
    finally:
        print("Finally: release external resources")
        local_file.close();
        print("Total sum = ", total)


##------------------------------------------------------------------------------


# EOFile
