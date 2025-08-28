def binToDec():
    answer = 0
    binaryString = str(input("Input a number to convert from binary to decimal "))
    for i in range(len(binaryString)): #round 1 i = 0. round 2 i = 1. round 3 i = 2
        val = int(binaryString[-(i+1)]) #i = 0, 1 is added and the sign is changed
        digit = val*(2**(i))
        answer = answer + digit
    print("answer:",answer)
binToDec()