myList = [7,2,3,1,6,5,4,2]
i = 0
while i < len(myList)-1:
    selection = myList[i]
    rest = myList[i+1:] #the colon here means continue to the end of the list
    minval = myList[i]
    for a in range(len(rest)):
        if rest[a] < minval:
            minval = rest[a]

    if selection > minval:
        minIndex = rest.index(minval)
        myList[i] = minval
        myList[i + 1 + minIndex] = selection # 2 lists + 1 = selection
    i = i + 1
    print(myList)
