import matplotlib.pyplot as plt
import numpy as np
from random import randint
from statistics import mean

# Data for plotting
t = []
scores = []
#volume = int(input("How much is to be washed? (1-10KG)"))
for j in range(100):
    start = 480*5
    counter = 0
    for i in range(10000):
        #print (start)
        start = start + randint(-50, 50)
        if start < 0:
            start = 0
        if int(start) > 6120*0.9:
            start = 3060
            counter = counter + 1
    scores.append(counter)
    t.append(counter)
    
print(mean(scores))

fig, ax = plt.subplots()
ax.plot(t)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
