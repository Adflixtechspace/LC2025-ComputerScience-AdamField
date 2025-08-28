import random

gameboard = ["_", "_", "_"]
num_of_turns = 0

wordsheet = ["cat", "men", "egg", "git"]
wordChosen = random.randint(0,len(wordsheet)-1)
answer = wordsheet[wordChosen]
answer_inlist = [answer[0], answer[1], answer[2]]

def one_guess():
    guess = input("Guess a letter. ")
    for i in range(len(answer_inlist)):
        if guess == answer_inlist[i]:
            gameboard[i] = guess
        i = i+1
    print(gameboard)

while (gameboard != answer_inlist) and (num_of_turns < 10):
    one_guess()
print("CONGRATS!!! :D")
