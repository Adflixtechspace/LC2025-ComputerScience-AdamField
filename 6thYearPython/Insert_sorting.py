JohnsList = [2,1,4,3,7]

poppedNum = JohnsList.pop(0)
i = 0
while i < len(JohnsList)-1:
    if poppedNum < JohnsList[i]:
        JohnsList.insert(JohnsList[i], poppedNum)
        print(JohnsList)
    i = i+1