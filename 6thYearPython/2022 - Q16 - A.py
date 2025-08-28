# Question 16(a) 
# Examination Number: 663
from random import randint 
 
#print("Dice simulation program") 
print("Dice simulation and analysis program")
results = [] 
frequencies = [0, 0, 0, 0, 0, 0] 
 
# Loop 100 times 
for i in range (100): 
    throw_result = randint(1,6) # store a random value between 1 and 6 
    results.append(throw_result) # append each value to results 
 
     # Start to build up a list of frequencies for each value thrown 
    if throw_result == 1: 
        frequencies[0] = frequencies[0] + 1 
    elif throw_result == 2: 
        frequencies[1] = frequencies[1] + 1 
    elif throw_result == 3: 
        frequencies[2] = frequencies[2] + 1 
    elif throw_result == 4: 
        frequencies[3] = frequencies[3] + 1 
    elif throw_result == 5: 
        frequencies[4] = frequencies[4] + 1 
    elif throw_result == 6: 
        frequencies[5] = frequencies[5] + 1 
 
print() 
#print("Results:", results)
print("Frequencies:",frequencies)
print("Dice Frequency\n---- ---------")
for i in range(6):
    print(i+1, "   ", frequencies[i])
maximum = frequencies.index(max(frequencies))
print("")
print(maximum+1, "was rolled the most often ("+str(frequencies[maximum]),"times)")

for j in range(6):
    print("*"*frequencies[j])