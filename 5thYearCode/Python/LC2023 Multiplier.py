print("*"*20)
print("Times Table program")
print("*"*20)
num = int(input("what is your first number? "))
num2 = int(input("how far? "))

if num >=0:
    print("Multiplications of", num)
else:
    print("error")

for i in range(num2+1):
    if num >=0:
        print(num, "x", i, "=", num*i)