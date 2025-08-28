#TAKE DOWN IN NOTES!!
import turtle as t #better use for clarity
c = t.clone()
t.pencolor("blue")
c.pencolor("green")

t.begin_fill()
c.begin_fill()
t.fillcolor("red")
c.fillcolor("yellow")
c.goto(-100,100)
for i in range(4):
    t.forward(100)
    t.left(90)
    c.forward(100)
    c.left(90)
t.end_fill()
    
    
c.end_fill()