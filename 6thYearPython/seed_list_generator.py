from random import randint
from random import seed
seed(5)
myList = []
for i in range(0,6):
    myList.append(randint(0,100))
print(myList)