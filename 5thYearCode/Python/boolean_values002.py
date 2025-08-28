from random import randint
answer = randint(1, 100)

def guess():  
    number = int(input("choose a number between 1 and 100 "))
    if number < answer:
        print("too low")
        guess()
    if number == answer:
        print("correct")
    if number > answer:
        print("too high")
        guess()

guess() 