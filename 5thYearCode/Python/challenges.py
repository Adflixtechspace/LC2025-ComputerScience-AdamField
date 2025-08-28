def arithmetic(num1, num2):
    print("when they add =", num1 + num2)
    print("when they subtract =", num1 - num2)
    print("when they multiply =", num1 * num2)
    print("when they divide =", num1 // num2) #foor division rounds down
    print("remainder =", num1 % num2) #mod division gives remainder

num1 = int(input("choose your first number? "))
num2 = int(input("choose your second number? "))
arithmetic(num1, num2)