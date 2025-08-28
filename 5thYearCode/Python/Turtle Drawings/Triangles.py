import turtle as t
X = 250
t.forward(X)
t.left(120)
t.forward(X)
t.left(120)
t.forward(X)

X=X/2

t.back(X)
t.left(120)
def upsidedown():
    t.forward(X)
    t.right(120)
    t.forward(X)
    t.right(120)
    t.forward(X)
upsidedown()

X=X/2

t.right(60)
t.forward(X)
t.right(60)

upsidedown()

t.left(120)
t.forward(X*2)
t.left(120)

upsidedown()

t.right(120)
t.forward(X)
t.right(60)
t.forward(X)
t.left(60)
t.forward(X)
t.left(120)

upsidedown()