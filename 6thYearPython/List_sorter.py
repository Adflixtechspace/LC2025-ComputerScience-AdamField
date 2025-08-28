def main():
    myList = list_identifier()
    sorter(myList)
    display_in_console(myList)

def list_identifier():
    myList = [184, 542, 358, 693, 144, 850, 178, 533, 331, 536, 268, 527, 266, 501, 178, 52, 238, 721, 367, 19, 585, 97, 760, 437, 673, 225, 307, 371, 2, 109, 362, 818, 441, 758, 310, 975, 228, 999, 369, 646, 670, 629, 816, 348, 697, 431, 776, 763, 349, 617, 289, 270, 295, 87, 914, 925, 793, 37, 914, 227, 835, 683, 982, 708, 530, 863, 918, 856, 931, 858, 928, 42, 229, 784, 89, 102, 12, 594, 888, 509, 930, 881, 66, 42, 457, 535, 541, 54, 948, 461, 707, 261, 386, 463, 409, 736, 591, 793, 491, 148]
    return myList


def sorter(myList):
    swap_number = 0
    for j in range(len(myList)):
        for i in range(len(myList)-1):
            if myList[i] > myList[i+1]:
                swap_number = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = swap_number

def display_in_console(myList):
    print(myList)

main()