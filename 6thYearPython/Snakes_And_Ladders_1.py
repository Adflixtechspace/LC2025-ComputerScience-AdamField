import random #Imports "random" file
Player1 = 0 #Player1 starts at 0, the beginning
Player2 = 0 #so does Player2
Winning_Space = 20

def P1Roll(): #function that calls the virtual die to roll
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

while True:
    P1Roll()
    if Player1 >= Winning_Space:
        print("Player 1 Wins")
        break
    P2Roll()
    if Player2 >= Winning_Space:
        print("Player 2 Wins")
        break