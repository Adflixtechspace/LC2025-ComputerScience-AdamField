UserInput = int(input("Put in number to find factorial: "))
ListOfNumbers = []
for UI in range(UserInput):
    ListOfNumbers.append(UI + 1)

product = 1
for i in range(len(ListOfNumbers)):
    product = product * ListOfNumbers[i]
print(product)