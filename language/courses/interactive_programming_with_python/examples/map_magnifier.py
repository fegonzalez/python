# Demonstration of a magnifier on a map

import simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scaling factor
SCALE = 3

# Canvas size
CAN_WIDTH = MAP_WIDTH // SCALE
CAN_HEIGHT = MAP_HEIGHT // SCALE

# Size of magnifier pane and initial center
DEFAULT_MAG_SIZE = 120
MIN_MAG_SIZE = 100
MAX_MAG_SIZE = 200
mag_size = DEFAULT_MAG_SIZE
mag_pos = [CAN_WIDTH // 2, CAN_HEIGHT // 2]


# Event handlers

def scale_handler(text_input):
    global mag_size      
    old_mag_size = mag_size
    try:
        mag_size = int(text_input)
        if mag_size < MIN_MAG_SIZE:
            mag_size = MIN_MAG_SIZE
        elif  mag_size > MAX_MAG_SIZE:
            mag_size = MAX_MAG_SIZE
    except:
        mag_size = old_mag_size
    
# Move magnifier to clicked position
def click(pos):
    global mag_pos
    mag_pos = list(pos)
    
# Move magnifier to dragged position
def drag(pos):
    global mag_pos
    mag_pos = list(pos)
    

# Draw map and magnified region
def draw(canvas):
    # Draw map
    canvas.draw_image(image, 
            [MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT], 
            [CAN_WIDTH // 2, CAN_HEIGHT // 2], [CAN_WIDTH, CAN_HEIGHT])

    # Draw magnifier    
    map_center = [SCALE * mag_pos[0], SCALE * mag_pos[1]]
    map_rectangle = [mag_size, mag_size]
    mag_center = mag_pos
    mag_rectangle = [mag_size, mag_size]
    canvas.draw_image(image, map_center, map_rectangle, \
                      mag_center, mag_rectangle)
            
# Create frame for scaled map
frame = simplegui.create_frame("Map magnifier", CAN_WIDTH, CAN_HEIGHT)

# register even handlers
frame.set_mouseclick_handler(click)    
frame.set_draw_handler(draw)
frame.set_mousedrag_handler(drag)

frame.add_input('Set Scale', scale_handler, 50)

# Start frame
frame.start()

