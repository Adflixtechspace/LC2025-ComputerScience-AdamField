decimal = int(input("Input a number to convert from decimal to binary "))
K = 0
while 2**K<=decimal:
    K=K+1
dividers = []

for j in range(K):
    dividers.append(2**j)
predecimal = 0
result = ""
decimalr = 0

for i in range(K):
    predecimal = decimal
    K = K-1
    decimal = decimal%dividers[K]
    if predecimal != decimal:
        result = result+"1"
    else:
        result = result+"0"
print(result)