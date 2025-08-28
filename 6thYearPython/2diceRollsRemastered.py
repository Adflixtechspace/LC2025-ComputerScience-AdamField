import random #imports random file

counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #creates counter

for i in range(240): #dice roll runs 240 times
    die1 = random.randint(1,6) #die1 rolls
    die2 = random.randint(1,6) #die2 rolls
    score = die1 + die2 #dice are added together
    for j in range (len(counter)): #score checker checks for each position
        if score == j+2: #checks if the score is equal to a particlar position 
            counter[j] = counter[j] + 1 #adds one to position in counter
            
print(counter) #prints the counter list

for x in range(len(counter)): #runs for each point in counter
    print (x+2, "=", "X" * counter[x]) #creates a bar chart using X's