from turtle import *
def ask1():
    shape_type = int(input("One or two unique sides? "))
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
howmany = ask1()
if howmany == 1:
    sides = askSq()
    turn = 360/sides
    sidelong = askSq2()
    for i in range(sides):
        forward(sidelong)
        left(turn)
if howmany == 2:
    isitrllyarectangle = askRek1()
    maybenotarectangle = 360/isitrllyarectangle
    rectangleX = askRek2()
    rectangleY = askRek3()
    print (isitrllyarectangle)
    for i in range(isitrllyarectangle):
        forward(rectangleX)
        left(maybenotarectangle)
        forward(rectangleY)
        left(maybenotarectangle)
if howmany >2:
    print ("wait till patch 1.1 to add more unique sides, maybe")
if howmany <0:
    print ("These shapes will be impossible to see as they can only be viewed in negative space, get your ticket to negative space today at www.becomenegative.com.org.net.com.com")
if howmany == 0:
    print ("Hah, in your dreams")