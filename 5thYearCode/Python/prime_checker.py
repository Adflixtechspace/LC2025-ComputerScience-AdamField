num = int(input("Pick a number to test if it's prime or not! "))
counter = 0
for i in range(num):
    if num % (i+1) == 0:
        counter = counter + 1
if counter > 2:
    print(num, "is not prime")
else:
    print(num,"is prime")