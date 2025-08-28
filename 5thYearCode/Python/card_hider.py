card_number = input("Input your 16 digit credit card number")
lastfour = []
print("Last four digits of your card =")
for i in range(4):
    print(card_number[i+12])
    i += 1