import random

counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
counter8 = 0
counter9 = 0
counter10 = 0
counter11 = 0
counter12 =0

for i in range(240):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    score = die1 + die2
    #print(score)
    if score == 2:
        counter2 = counter2 + 1
    elif score == 3:
        counter3 = counter3 + 1  
    elif score == 4:
        counter4 = counter4 + 1
    elif score == 5:
        counter5 = counter5 + 1
    elif score == 6:
        counter6 = counter6 + 1
    elif score == 7:
        counter7 = counter7 + 1  
    elif score == 8:
        counter8 = counter8 + 1
    elif score == 9:
        counter9 = counter9 + 1
    elif score == 10:
        counter10 = counter10 + 1
    elif score == 11:
        counter11 = counter11 + 1  
    elif score == 12:
        counter12 = counter12 + 1
    
print(counter2,counter3,counter4,counter5,counter6,
      counter7,counter8,counter9,counter10,counter11,counter12)