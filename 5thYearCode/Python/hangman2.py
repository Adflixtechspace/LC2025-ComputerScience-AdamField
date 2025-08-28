import random


wordsheet = ['cat']
wordChosen = random.randint(0,len(wordsheet)-1)
answer = wordsheet[wordChosen]
answer_inlist = []

for j in range(len(answer)):
    answer_inlist.append(answer[j])
gameboard = []

for k in range(len(answer)):
    gameboard.append("_")
print(gameboard)
num_of_turns = 0

def one_guess(num_of_turns):
    print("")
    guess = input("Guess a letter. ")
    flag = "up"
    for i in range(len(answer_inlist)):
        if (guess == answer_inlist[i]) & (flag == "up"):
            gameboard[i] = guess
            flag = "down"
            num_of_turns = num_of_turns-1
        elif (guess == answer_inlist[i]) & (flag == "down"):
            gameboard[i] = guess
            flag = "down"
    num_of_turns = num_of_turns + 1
    print(gameboard)
    print(10-num_of_turns, "guesses left")
    return num_of_turns

while (gameboard != answer_inlist) and (num_of_turns < 10):
    num_of_turns = one_guess(num_of_turns)
if gameboard == answer_inlist:
    print("")
    print("You Win!!")
if num_of_turns >= 10:
    print("")
    print("You Lose")
