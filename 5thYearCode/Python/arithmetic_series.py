num1 = int(input("pick a number "))
num2 = int(input("pick another number "))
difference = (num2 - num1)
ans = 0
jmp = int(input("how many numbers will in jump in between? "))
for i in range(int((difference)/jmp)+1):
    ans = ans+num1+i*jmp
    print (ans)