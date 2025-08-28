f = open("henry.csv", "r")

lines = f.readlines()

print(lines[5])

f.close()