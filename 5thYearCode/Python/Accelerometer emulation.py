from random import *
from statistics import mean 
scores = []
for j in range(200):
    start = 3060
    counter = 0
    for i in range(10000):
        #print (start)
        start = start + randint(-50, 50)
        if start < 0:
            start = 0
        if int(start) > 6120*0.9:
            #print("Warning, Washing Machine is ready to blastoff, keep your distance")
            start = 3060
            counter = counter + 1
            #print(counter)
    scores.append(counter)
#print(scores)
print(mean(scores))

    