#Modular Functional Programming
#i.e. Prime Checker

def main():
    number = UserInput()
    perf_division = Checker(number)
    Display(perf_division)

def UserInput():
    number = int(input("Choose a number to check: "))
    return number

def Checker(number):
    perf_division = 0
    for i in range(number):
        divider = number % (i+1)
        if divider == 0:
            perf_division += 1
    return perf_division
    
def Display(perf_division):
    if perf_division == 2:
        print("This is a Prime Number")
    else:
        print("This is a Composite Number")

main()