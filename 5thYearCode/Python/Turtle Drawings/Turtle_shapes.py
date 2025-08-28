from turtle import *
def asky():
    shape = input("Which shape would you like to draw? Square, Rectangle or Octagon? ")
    return shape

def draw_square():
    SL = int(input("How big, in pixels, will each side of this square be? "))
    for i in range(4):
        forward(SL)
        left(90)
    
def draw_rectangle():
    RL1 = int(input("How big, in pixels, will rectabngle side X axis be? "))
    RL2 = int(input("How big, in pixels, will rectabngle side Y axis be? "))
    for i in range(2):
        forward(RL1)
        left(90)
        forward(RL2)
        left(90)
    
def draw_hexagon():
    HL = int(input("How long, in pixel, will each side of this haxagon be? "))
    for i in range(6):
        forward(HL)
        left(60)
    
def draw_octagon():
    OL = int(input("How long, in pixels, will each side of this octagon be? "))
    for i in range(8):
        forward(OL)
        left(45)
    
shape = asky()
    
if (shape == "square") or (shape == "Square"):
    draw_square()
elif shape == "rectangle":
    draw_rectangle()
if shape == "hexagon":
    draw_hexagon()
elif shape == "octagon":
    draw_octagon()
else:
    print("User input invalid")
    asky()
    