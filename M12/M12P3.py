students_lastname = []
students_score = []

try:
    
    with open("students.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            students_lastname.append(parts[0])
            students_score.append(float(parts[1]))
except FileNotFoundError:
    print("\nFile students.txt not found!")

def find_highest_score(names, scores):
    high_score = 0
    high_index = 0
    for i in range(len(scores)):
        if scores[i] > high_score:
            high_score = scores[i]
            high_index = i
    print("\nHighest Score:")
    print(names[high_index], "-", high_score)

def find_lowest_score(names, scores):
    low_score = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] < low_score:
            low_score = scores[i]
            low_index = i
    print("\nLowest Score:")
    print(names[low_index], "-", low_score)

if students_lastname and students_score:
    find_highest_score(students_lastname, students_score)
    find_lowest_score(students_lastname, students_score)