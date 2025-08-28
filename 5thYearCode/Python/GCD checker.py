numA = int(input("Please pick the first number. "))
numB = int(input("Please pick the second number. "))
divisorA = []
divisorB = []

for a in range(numA):
    if (numA)%(a+1) == 0:
        divisorA.append((numA)/(a+1))
print(divisorA)

for b in range(numB):
    if (numB)%(b+1) == 0:
        divisorB.append((numB)/(b+1))
print(divisorB)