def main():
    userInputs()
    findMax(userNames, userGrades)
userNames = []
userGrades = []
def userInputs():
    studentName = ""
    while studentName != "n":
        studentName = input("Please enter student's name (input n to stop): ")
        if studentName != "n":
            userNames.append(studentName)
            studentGrade = int(input("Please enter student's grade (0-100): "))
            if studentGrade >= 0 and studentGrade <= 100:
                userGrades.append(studentGrade)
            else:
                print("Invalid input. Number needs to be between 0 and 100")
                studentName = "n"

def findMax(names, grades):
    print(names, grades)
    maximum = max(grades)
    print(maximum)
    for i in range(len(grades)):
        if grades[i] == maximum:
            print(names[i], "scored the highest score at", grades[i], "%")
main() 