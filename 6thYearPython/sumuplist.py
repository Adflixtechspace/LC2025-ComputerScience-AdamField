import random
myList = []
for i in range(20):
    num = random.randint(1,32)
    myList.append(num)
s = (sum(myList))//32
print(s)