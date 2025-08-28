fruits = ['apple', 'cherry', 'orange', 'kiwi']
flag = "up"
def nominate():
    nomination = input("Nominate your winning fruit: ")
    if nomination in fruits:
        print("good")
        flag = "down"
    else:
        print("Error")
        flag = "up"
    return flag
while flag == "up":
    flag = nominate()
    
