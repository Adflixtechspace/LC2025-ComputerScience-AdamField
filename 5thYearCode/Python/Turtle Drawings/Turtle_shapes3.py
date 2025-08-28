from turtle import *
def gotohere():
    up()
    goto(xbegin,ybegin)
    down()
def ask1():
    shape_type = int(input("Do you want the shape to have one, two or three unique sides? "))
    return shape_type
def askSq():
    side_count = int(input("How many sides to be drawn? "))
    return side_count
def askSq2():
    side_length = int(input("How long, in pixels, will each side on this shape be? "))
    return side_length
def askRek1():
    side_count = int(input("How many sides to be drawn? "))
    return side_count
def askRek2():
    rekLengthX = int(input("How long, in pixels, will side 1 on this shape be? "))
    return rekLengthX
def askRek3():
    rekLengthY = int(input("How long, in pixels, will side 2 on this shape be? "))
    return rekLengthY
def askTri1():
    side_count = int(input("How many sides to be drawn? (note any value X3(+2) will give one less line)"))
    return side_count
def askTri2():
    TriLength1 = int(input("How long, in pixels, will side 1/3 on this shape be? "))
    return TriLength1
def askTri3():
    TriLength2 = int(input("How long, in pixels, will side 2/3 on this shape be? "))
    return TriLength2
def askTri4():
    TriLength3 = int(input("How long, in pixels, will side 3/3 on this shape be? "))
    return TriLength3
xbegin = int(input("Where shall the curser begin in pixels on the X axis? "))
ybegin = int(input("Where shall the curser begin in pixels on the Y axis? "))
howmany = ask1()
if howmany == 1:
    sides = askSq()
    turn = 360/sides
    sidelong = askSq2()
    gotohere()
    for i in range(sides):
        forward(sidelong)
        left(turn)
if howmany == 2:
    isitrllyarectangle = askRek1()
    maybenotarectangle = 360/isitrllyarectangle
    rectangleX = askRek2()
    rectangleY = askRek3()
    gotohere()
    for i in range(int(isitrllyarectangle/2)):
        forward(rectangleX)
        left(maybenotarectangle)
        forward(rectangleY)
        left(maybenotarectangle)
    goto(xbegin,ybegin)
if howmany == 3:
    isitrllyarectangle = askRek1()
    maybenotarectangle = 360/isitrllyarectangle
    triple1 = askTri2()
    triple2 = askTri3()
    triple3 = askTri4()
    gotohere()
    for i in range(int(isitrllyarectangle/3)):
        forward(triple1)
        left(maybenotarectangle)
        forward(triple2)
        left(maybenotarectangle)
        forward(triple3)
        left(maybenotarectangle)
    goto(xbegin,ybegin)
if howmany >3:
    print ("wait till patch 1.2 to add more unique sides, maybe")
if howmany <0:
    print ("These shapes will be impossible to see as they can only be viewed in negative space, get your ticket to negative space today at www.becomenegative.com.org.net.com.com")
if howmany == 0:
    print ("Hah, in your dreams")