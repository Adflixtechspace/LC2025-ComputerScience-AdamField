myList = [7,2,3,1,6,5,4,2]
i = 0
while i < len(myList)-1:
    selection = myList[i]
    rest = myList[i+1:] #the colon here means continue to the end of the list
    minimumRest = min(rest) #locates smallest in rest

    if selection > minimumRest:
        minIndex = rest.index(minimumRest)
        myList[i] = minimumRest
        myList[i + 1 + minIndex] = selection # 2 lists + 1 = selection
    i = i + 1
    print(myList)