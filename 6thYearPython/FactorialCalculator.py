def main(): #Defines the main function
    n = UserInput() #Calls UserInput and returns n to n
    striNg = NumString(n) #Calls NumString and returns striNg to striNg
    print(striNg+"! =", NFactorial(n)) #Prints n!
def UserInput(): #Takes user input and returns input
    n = int(input("Input number to find factorial value: ")) #Asks user for number input
    return n
def NumString(n): #Creates a string version of n
    striNg = str(n) #Creates a string version of the number
    return striNg
def NFactorial(n): #Calculates factorial value
    if n == 1 or n == 0: #Checks if n is equal to 1 or 0
        return 1 #Return 1
    elif n > 1: #Checks if n is greater than 1
        return n * NFactorial(n-1) #Returns n!
while True:
    main() #Calls main function