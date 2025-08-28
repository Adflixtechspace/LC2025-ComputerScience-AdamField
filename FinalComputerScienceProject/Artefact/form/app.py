from flask import Flask, request, render_template_string
import csv
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    with open('example003.html', 'r') as file:
        return render_template_string(file.read())

@app.route('/submit', methods=['POST'])
def submit_form():
    
    subs = [] #subjects
    levels = [] #levels H or O
    grades = [] #grade numbers 

    for i in range(6):
        subs.append(request.form.get('subject'+str(i+1)))
        levels.append(request.form.get('sub'+str(i+1)))
        grades.append(request.form.get('grade'+str(i+1)))
    
    with open('subjectData.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        for i in range(6):
            writer.writerow([subs[i], levels[i], grades[i]])

    
    data = pd.read_csv('subjectData.csv',header = None)
    grades = []
    for i in range(6):
        grade = data[1][i] + str(data[2][i])
        grades.append(grade)
    data["grades"] = grades
    score = 0
    for i in range(6):
        if data["grades"][i] == "True1":
            score = score + 100
        elif data["grades"][i] == "True2":
            score = score + 88
        elif data["grades"][i] == "True3":
            score = score + 77
        elif data["grades"][i] == "True4":
            score = score + 66
        elif data["grades"][i] == "True5":
            score = score + 56
        elif data["grades"][i] == "True6":
            score = score + 46
        elif data["grades"][i] == "True7":
            score = score + 37
        elif data["grades"][i] == "False1":
            score = score + 56
        elif data["grades"][i] == "False2":
            score = score + 46
        elif data["grades"][i] == "False3":
            score = score + 37
        elif data["grades"][i] == "False4":
            score = score + 28
        elif data["grades"][i] == "False5":
            score = score + 20
        elif data["grades"][i] == "False6":
            score = score + 12
            
    print(score) 

    mean2024 = 418
    
    if mean2024 >= score:
        direction = "below "
        difference = str(mean2024 - score)
        sentiment = "Recommendation: You need to start nuckling down boyohh!"
    
    elif mean2024 < score:
        direction = "above "
        difference = str(score - mean2024)
        sentiment = "Recommendation: You can start slacking in class, everything is going to be perfect"

    
    return "Your Points score will be "+str(score)+", this is "+difference+" "+direction+"the 2024 Mean. "+ sentiment

if __name__ == '__main__':
    app.run(debug=True)
