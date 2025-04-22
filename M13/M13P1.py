students = {}
answer = input("Add student grade? (y/n): ").lower()

while answer == "y":
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students[name] = grade
    answer = input("Add another? (y/n): ").lower()

print("\nStudent Name\tGrade")
print("-------------------------")
for name, grade in students.items():
    print(name, "\t", grade)
class_avg = sum(students.values()) / len(students)
print("\nClass Average:\t", round(class_avg, 2))