fizzbuzzCount = 0
fizzCount = 0
buzzCount = 0

minVal = 1
maxVal = 100

fizzVal = 2
buzzVal = 4
for i in range(minVal, maxVal+1): # For loop where i is every value from 1 to 100
    if i%(fizzVal*buzzVal) == 0: # 3X5 = the product of fizzVal and buzzVal, so if the remainder of i divide by 15 is 0, it prints "FizzBuzz" to the shell
        print("FizzBuzz")
        fizzbuzzCount += 1
    elif i%fizzVal == 0: # Else if the remainder of i divide by fizzVal is 0, it prints "Fizz" to the shell
        print("Fizz")
        fizzCount += 1
    elif i%buzzVal == 0: # Else if the remainder of i divide by buzzVal is 0, it prints "Buzz" to the shell
        print("Buzz")
        buzzCount += 1
    else: # Else if none of the conditions are met, it prints the original number
        print(i)
        
print("There were", fizzbuzzCount, "FizzBuzz's in between", minVal, "and", maxVal, "\nThere were", fizzCount, "Fizz's in between", minVal, "and", maxVal, "\nThere were", buzzCount, "Buzz's in between", minVal, "and", maxVal)
# Statistics for the program