import random

def main():
    sortedList = list_maker()
    jack = list_sorter(sortedList)
    display(jack)
def Min_Finder(sample_list):
    

    length = len(sample_list)
    minval = sample_list[0]
    for a in range(length):
        if sample_list[a] < minval:
            minval = sample_list[a]
    return minval
def list_maker():
    myList = []
    for i in range(20):
        num = random.randint(1,32)
        myList.append(num)
    
    return myList
def list_sorter(sortedList):
    i = 0
    while i < len(sortedList)-1:
        selection = sortedList[i]
        rest = sortedList[i+1:] #the colon here means continue to the end of the list
        minimumRest = Min_Finder(rest) #locates smallest in rest
        if selection > minimumRest:
            minIndex = rest.index(minimumRest)
            sortedList[i] = minimumRest
            sortedList[i + 1 + minIndex] = selection # 2 lists + 1 = selection
        i = i + 1
    return sortedList

def display(jack):
    print(jack)
    
main()