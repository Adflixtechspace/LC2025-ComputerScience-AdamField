import random #Imports "random" file
Player1 = 0 #Player1 starts at 0, the beginning
Player2 = 0 #so does Player2
Winning_Space = 20

print("Welcome to Pythons and ladders! In this game, you roll a dice to progress through the map.")
#print("Landing on the head of a python brings you back and landing on the feet of a ladder brings you forward")
print("Your goal is to reach the winning space of", Winning_Space, "Before any other players do.")
print("If you overshoot the winning space, you will have to redo your go on the next turn.")
print("")
PlayersInGame = input("Will it be 2 Players or 1 Player with a computer? (1 or 2)")

def P1Roll():
    global Player1 #Knows that Player1 is located outside loop
    print("PLAYER 1")
    input("Press Enter to roll.")
    die_roll = random.randint(1,6) #the die rolls
    print("Rolls a", die_roll) #the number is shown
    if Player1 + die_roll <= Winning_Space: #Checks to see if Player won't overshoot the winning space
        Player1 += die_roll #Player 1 will move forward
        print("Player 1 has moved to",Player1) #Displays new position of Player 1
    else:
        print("Player 1 overshot winning space of", Winning_Space)
        print("Player 1 remains on",Player1) #Displays previous position of Player 1
    print("")

def P2Roll():
    global Player2 #Knows that Player2 is located outside loop
    print("PLAYER 2")
    input("Press Enter to roll.")
    die_roll = random.randint(1,6) #the die rolls
    print("Rolls a", die_roll) #the number is shown
    if Player2 + die_roll <= Winning_Space: #Checks to see if Player won't overshoot the winning space
        Player2 += die_roll #Player 2 will move forward
        print("Player 2 has moved to",Player2) #Displays new position of Player 2
    else:
        print("Player 2 overshot winning space of", Winning_Space)
        print("Player 2 remains on",Player2) #Displays previous position of Player 2
    print("")
    
def C2Roll():
    global Player2 #Knows that Computer is located outside loop
    print("Computer")
    die_roll = random.randint(1,6) #the die rolls
    print("Rolls a", die_roll) #the number is shown
    if Player2 + die_roll <= Winning_Space: #Checks to see if Player won't overshoot the winning space
        Player2 += die_roll #Player 2 will move forward
        print("Computer has moved to",Player2) #Displays new position of Computer
    else:
        print("Computer overshot winning space of", Winning_Space)
        print("Computer remains on",Player2) #Displays previous position of Computer
    print("")
    
if PlayersInGame == "1": #1 Player game with computer
    while True:
        P1Roll()
        if Player1 == Winning_Space: #Checks to see if Player 1 has reached the Winning Space
            print("Player 1 Wins")
            break #While loop ends and the game is over
        C2Roll()
        if Player2 == Winning_Space: #Checks to see if Computer has reached the Winning Space
            print("Computer Wins")
            break

elif PlayersInGame == "2": #2 Player game
    while True:
        P1Roll()
        if Player1 == Winning_Space: #Checks to see if Player 1 has reached the Winning Space
            print("Player 1 Wins")
            break
        P2Roll()
        if Player2 == Winning_Space: #Checks to see if Player 2 has reached the Winning Space
            print("Player 2 Wins")
            break