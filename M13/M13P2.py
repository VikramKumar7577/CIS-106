students_grades = {}
answer = input("Add student with 3 grades? (y/n): ").lower()
while answer == "y":
    name = input("Enter student name: ")
    grades = []
    grades.append(float(input("Enter grade 1: ")))
    grades.append(float(input("Enter grade 2: ")))
    grades.append(float(input("Enter grade 3: ")))
    students_grades[name] = grades
    answer = input("Add another student? (y/n): ").lower()

print("\nStudent\t\tAverage")
print("-------------------------")
for name in students_grades:
    avg = round(sum(students_grades[name]) / 3, 2)
    print(name, "\t", avg)

g1 = 0
g2 = 0
g3 = 0
for name in students_grades:
    g1 += students_grades[name][0]
    g2 += students_grades[name][1]
    g3 += students_grades[name][2]

count = len(students_grades)
print("\nClass Avg Grade 1:\t", round(g1 / count, 2))
print("Class Avg Grade 2:\t", round(g2 / count, 2))
print("Class Avg Grade 3:\t", round(g3 / count, 2))