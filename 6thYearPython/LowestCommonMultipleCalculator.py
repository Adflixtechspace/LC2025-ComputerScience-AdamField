#LCM of two numbers
def LCMcalculator(numa, numb): # function that takes two numbers in
    numaList = [] # empty list to store all numa values up to guarantee
    numbList = [] # empty list to store all numb values up to guarantee
    guarantee = numa*numb # guarantee ensures the LCM is definitely accounted for
    for x in range(numb):
        numaList.append((x+1)*numa) # appends all numa values up to guarantee to numaList
    for y in range(numa):
        numbList.append((y+1)*numb) # appends all numa values up to guarantee to numaList
    #print(numaList,numbList)
    for i in range(len(numaList)):
        #print(numaList[i])
        for j in range(len(numbList)):
            if numbList[j] == numaList[i]:
                return numbList[j]

print(LCMcalculator(6,8))