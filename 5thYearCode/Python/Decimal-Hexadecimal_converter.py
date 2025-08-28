def hextodec():
    a = 0
    answer = 0
    decimal = str(input("Input a decimal number to be converted to hexadeciaml "))
    for i in range(len(decimal)): #round 1 i = 0. round 2 i = 1. round 3 i = 2
        val = (decimal[-(i+1)]) #i = 0, 1 is added and the sign is changed
        if val == a:
            val = 10
        digit = val*(16**(i))
        answer = answer + int(digit)
    print("answer:",answer)
hextodec()