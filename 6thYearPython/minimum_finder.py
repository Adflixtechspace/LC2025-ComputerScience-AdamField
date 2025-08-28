myList = [7,2,3,8,6,5,4,2]
def Min_Finder(myList):
    

    length = len(myList)
    minval = myList[0]
    for a in range(length):
        if myList[a] < minval:
            minval = myList[a]
    return minval
    
print(Min_Finder(myList))
