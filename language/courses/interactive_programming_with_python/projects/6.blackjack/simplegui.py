# -*- coding: utf-8 -*-

# Dummy file to declare simplegui objects that can be locally imported.



def load_image(url=""):
    print "load_image: " ,  url


def create_frame(name, he, wi):
    print "create_frame ", he, ", ", wi
    return Frame(name, he, wi)
   

class Frame:

    def __init__(self, name, he, wi):
        self.name=name
        self.he=he
        self.wi=wi

    def set_canvas_background(self, color):
        pass

    def add_button(self, name, functor, wi):
        pass

    def set_draw_handler(self, draw):
        pass

    def start(self):
        pass

