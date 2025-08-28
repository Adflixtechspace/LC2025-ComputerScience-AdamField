# Write your code here :-)
from microbit import *
import time

while True:
    time.sleep(0.1)
    print(int(temperature()*10))
