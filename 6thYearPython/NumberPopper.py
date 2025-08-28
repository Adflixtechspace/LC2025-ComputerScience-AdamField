JacksList = [2,3,4,8,6,9]

poppedNum = JacksList.pop(4)
i = 0
while i < len(JacksList) - 1:
    if poppedNum < JacksList[i]:
        position = i
        print(poppedNum, "Should go into position", i)
        i = i + len(JacksList)
    i = i + 1