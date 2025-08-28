from random import randint
words=["cat","hat","run","sit","top"]

#answer_index = randint(0,4)
answer_index = 4
answer = words[answer_index]
answer_list = [answer[0], answer[1], answer[2]]

record=["_","_","_"]

for turn in range(3):
    guess = input("Please choose a 3 letter word ")
    print(guess)
    guess_list=[guess[0], guess[1], guess[2]]
    print(guess_list)
    for i in range(3):
        if answer_list[i] == guess_list[i]
            record = "Y"
        if answer_list[i] == guess_list[i]:
            record[i] = "X"
    print(record)