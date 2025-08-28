def Min_Finder(sample_list):
    

    length = len(sample_list)
    minval = sample_list[0]
    for a in range(length):
        if sample_list[a] < minval:
            minval = sample_list[a]
    return minval

myList = [7,2,3,1,6,5,4,2]
i = 0
while i < len(myList)-1:
    selection = myList[i]
    rest = myList[i+1:] #the colon here means continue to the end of the list
    minimumRest = Min_Finder(rest) #locates smallest in rest

    if selection > minimumRest:
        minIndex = rest.index(minimumRest)
        myList[i] = minimumRest
        myList[i + 1 + minIndex] = selection # 2 lists + 1 = selection
    i = i + 1
    print(myList)