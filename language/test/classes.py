#!/usr/bin/env python3

# Testing (basic) Classes in Python

##==============================================================================


class MyComplex:

    the_class_attr = "I am a 'Class variable', thus I am shared by all the object instances of this class"

    def __init__(self, realpart=0.0, imagpart=0.0):    # c012 
        self.the_real = realpart
        self.the_imag = imagpart
    
        
    # WARNING Function overloading not valid in Python. If more than one are
    # written, all but the last one are ignored by the interpreter.

    # def class_method(self, mas_param):
    #     print("two arguments required))

    def class_method(self):
        print(self.the_real)
        print("Calling a class variable inside a method:", self.the_class_attr);
    
        

##==============================================================================

class MyClass:
    """A simple example class: Includes 'self' use example"""
    i = 12345;

    def f1(self):
        return 'hello world'        

    def f2(antonio):
        print("self OR antonio, it doesn't matters")

    ## TypeError: f3() takes 0 positional arguments but 1 was given
    # def f3(): 
    #     return 'hello world'        

        
##==============================================================================

def f1(self, x, y): # Function defined outside the class
    return min(x, x+y)

class FuncTest:
    f = f1
    def g(self):
        return 'hello world'
    h = g

# Example of use.-     
#
# >>> fo=classes.FuncTest()    
#
# >>> classes.f1(fo, 1,2)
# 1
# >>> classes.f1(fo, 1,2)
# 1
#
# >>> fo.f(3,4)
# 3
# >>> fo.g()
# 'hello world'
# >>> fo.h()
# 'hello world'



##------------------------------------------------------------------------------
