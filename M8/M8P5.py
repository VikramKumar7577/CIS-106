with open("students.txt", "r") as file:
  lines = file.readlines()

total_tuition = 0
student_count = 0

print("Student\tCredits\tTuition Owed")

for i in range(0, len(lines), 3):
  name = lines[i].strip()
  district = lines[i + 1].strip()
  credits = int(lines[i + 2].strip())

  rate = 250 if district == 'I' else 500
  tuition = credits * rate

  print(f"{name}\t{credits}\t${tuition}")
  total_tuition += tuition
  student_count += 1

print(f"Total tuition: ${total_tuition}, Number of students: {student_count}")
