from random import randint
def henry(x, power):
    return pow(x, power)

x = randint(1,10)
y = randint(1,10)

print(x,"^",y,"=")
print(henry(x,y))