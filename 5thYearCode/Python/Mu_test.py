# Write your code here :-)
from microbit import *
genders = 2

while genders == 2:
    print(int(temperature()*10))
    display.scroll(temperature())

