from random import *
from statistics import mean
scores = []
def volumedata():
    volume = int(input("How much is to be washed? (1-10KG)"))
    if volume > 10:
        print("Can't go over 10")
        volume = volumedata()
    if volume < 1:
        print("Can't go under 1")
        volume = volumedata()
    else:
        return volume
volume = volumedata()
for j in range(100):
    start = 480*volume
    counter = 0
    for i in range(10000):
        start = start + randint(-50, 50)
        if start < 0:
            start = 0
        if int(start) > 6120*0.9:
            start = 3060
            counter = counter + 1
    scores.append(counter)
print(scores)
print(mean(scores))