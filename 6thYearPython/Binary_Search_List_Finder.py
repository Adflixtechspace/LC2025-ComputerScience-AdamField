def main():
    myList = list_sorter()
    key = Input()
    finder(myList, key)
def list_sorter():
    myList = [516, 8, 42, 327, 743, 901, 206, 959, 397, 701, 485, 149, 5, 39, 243, 501, 411, 860, 584, 368, 669, 631, 742, 922, 208, 333, 250, 316, 803, 152, 586, 956, 300, 204, 181, 562, 781, 942, 886, 576, 467, 490, 501, 76, 572, 630, 574, 428, 221, 723, 497, 514, 770, 391, 91, 871, 594, 521, 402, 883, 712, 283, 443, 653, 14, 738, 922, 95, 312, 530, 92, 910, 811, 444, 528, 454, 647, 967, 467, 940, 371, 990, 704, 257, 964, 250, 94, 456, 867, 876, 36, 655, 593, 571, 817, 742, 828, 78, 348, 95]
    myList.sort()
    print(myList)
    return myList

def Input():
    key = int(input("Enter a number: "))
    return key
def finder(myList, key):
    flag = "down"
    lower_number = 0
    higher_number = len(myList) - 1
    if key in myList:
        while lower_number <= higher_number and flag == "down":
            middle_number = (lower_number + higher_number) // 2
            if myList[middle_number] == key:
                print("Found in list at position", middle_number)
                flag = "up"
            elif myList[middle_number] < key:
                lower_number = middle_number + 1
            elif myList[middle_number] > key:
                higher_number = middle_number - 1
    else:
        print("Number not found in list.")
main()
print("10Q for using the app ")