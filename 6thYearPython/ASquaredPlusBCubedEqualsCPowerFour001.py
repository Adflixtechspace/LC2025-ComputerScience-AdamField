def main(): # Contains all function of the program
    min, max = getRange()
    np1, np2, np3, np4 = generateList(min, max)
    compare(np1, np2, np3, np4)
def getRange(): # Gets user to input mininmum and maximum values to check
    min = int(input("Please input the minimum value to check for: ")) # User inputs minimum value
    max = int(input("Please input the maximum value to check for: ")) # User inputs maximum value
    return min, max
#print(getRange())
def generateList(min, max): # Creates lists and appends all values into the respective list, this will be used in compare()
    n1 = [] # Creates n^1 list
    n2 = [] # Creates n^2 list
    n3 = [] # Creates n^3 list
    n4 = [] # Creates n^4 list
    for i in range(min, max+1): # i = every value between minimum and maximum, including minimum and maximum
        n1.append(i) # Appends n to n1 list
        n2.append(i**2) # Appends n^2 to n2 list
        n3.append(i**3) # Appends n^3 to n3 list
        n4.append(i**4) # Appends n^4 to n4 list
    return n1, n2, n3, n4
def compare(n1, n2, n3, n4): # Checks if any value in n2 + any value in n3 = any value in n4 (a^2 + b^3 = c^4)
    for a in range(len(n1)): # Each item in n2 is checked
        for b in range(len(n1)): # Each item in n3 is checked
            for c in range(len(n1)): # Each item in n4 is checked
                if (n2[a] + n3[b]) == n4[c]: # Checks if a^2 + b^3 = c^4
                    print(str(n1[a])+"^2 +",str(n1[b])+"^3 =",str(n1[c])+"^4") # Prints statement
                    print(n2[a],"+",n3[b],"=",n4[c]) # Prints statement multiplied out
                    print("") # Creates a space for ease of reading
main() # Calls main to run program