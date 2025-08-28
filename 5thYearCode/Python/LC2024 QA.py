# Question 16 (a)
# Examination Number: 69
from random import choice

fruits = ['apple', 'cherry', 'orange']
random_fruit_1 = choice(fruits)
print("Random Fruit 1:", random_fruit_1)
random_fruit_2 = choice(fruits)
print("Random Fruit 2:", random_fruit_2)
random_fruit_3 = choice(fruits)
print("Random Fruit 3:", random_fruit_3)
print("")

if random_fruit_1 == 'cherry':
    print("First fruit is cherry")
if random_fruit_1 == random_fruit_2:
    print("First pair match")
if random_fruit_1 == 'cherry' and random_fruit_2 == 'cherry':
    print("First pair are cherries")
if random_fruit_1 == random_fruit_2 or random_fruit_2 == random_fruit_3 or random_fruit_1 == random_fruit_3:
    print("Matching pair")
apples = 0
oranges = 0
cherries = 0
for i in range(100):
    fruit = choice(fruits)
    if fruit == 'apple':
        apples += 1
    elif fruit == 'orange':
        oranges += 1
    else:
        cherries += 1
print("")
print("apple", apples)
print("orange", oranges)
print("cherry", cherries)