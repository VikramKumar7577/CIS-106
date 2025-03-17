last = input("Enter student’s last name: ")
hours = int(input("Enter credit hours: "))
code = input("Enter district code (I/O): ")

if code == "I":
    tuition = hours * 250
elif code == "O":
    tuition = hours * 550
else:
    tuition = 0

print("Student:", last)
print("Tuition Owed =", tuition)