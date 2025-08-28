from random import randint

def main():
    UserChoice = "NA"
    while UserChoice == "NA":
        UserChoice = UserInput()
    ComputerChoice = ComputerInput()
    result = Comparer(UserChoice, ComputerChoice)
    DisplayResult(result)

def UserInput():
    UserChoice = input("ROCK, PAPER, SCISSORS, SHOOT!:")
    UserChoice = UserChoice.upper()
    if UserChoice == "ROCK":
        return UserChoice
    elif UserChoice == "PAPER":
        return UserChoice
    elif UserChoice == "SCISSORS":
        return UserChoice
    else:
        print("Invalid User Input")
        return "NA"

def ComputerInput():
    ComputerNumChoice = randint(0, 2)
    if ComputerNumChoice == 0:
        ComputerChoice = "ROCK"
    elif ComputerNumChoice == 1:
        ComputerChoice = "PAPER"
    elif ComputerNumChoice == 2:
        ComputerChoice = "SCISSORS"
    return ComputerChoice

def Comparer(UserChoice, ComputerChoice):
    if UserChoice == "ROCK":
        print("You chose", UserChoice)
        if ComputerChoice == "ROCK":
            print("Computer Chose", ComputerChoice)
            return "Draw"
        elif ComputerChoice == "PAPER":
            print("Computer Chose", ComputerChoice)
            return "Computer"
        elif ComputerChoice == "SCISSORS":
            print("Computer Chose", ComputerChoice)
            return "User"
    if UserChoice == "PAPER":
        print("You chose", UserChoice)
        if ComputerChoice == "ROCK":
            print("Computer Chose", ComputerChoice)
            return "User"
        elif ComputerChoice == "PAPER":
            print("Computer Chose", ComputerChoice)
            return "Draw"
        elif ComputerChoice == "SCISSORS":
            print("Computer Chose", ComputerChoice)
            return "Computer"
    if UserChoice == "SCISSORS":
        print("You chose", UserChoice)
        if ComputerChoice == "ROCK":
            print("Computer Chose", ComputerChoice)
            return "Computer"
        elif ComputerChoice == "PAPER":
            print("Computer Chose", ComputerChoice)
            return "User"
        elif ComputerChoice == "SCISSORS":
            print("Computer Chose", ComputerChoice)
            return "Draw"
        
def DisplayResult(result):
    if result == "User":
        print("*User Wins*")
    elif result == "Computer":
        print("*Computer Wins*")
    elif result == "Draw":
        print("*Tie*")

main()