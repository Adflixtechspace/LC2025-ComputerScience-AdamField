num1 = int(input("Please pick the first number. "))
num2 = int(input("Please pick the second number. "))

while num1 > 1:
    num1 = num1/num2
    
if num1 == 1:
    print("yes")

if num1 < 1:
    print("no")