def compute_scores(score1, score2, score3):
  total_points = float(score1) + float(score2) + float(score3)
  average = total_points / 3
  return total_points, average

student_last_name = input("Enter student's last name: ")
score1 = float(input("Enter exam score 1: "))
score2 = float(input("Enter exam score 2: "))
score3 = float(input("Enter exam score 3: "))
total_points, avg_score = compute_scores(score1, score2, score3)
print("Student Last Name:", student_last_name)
print("Total Points:", total_points)
print("Average Score:", avg_score)
