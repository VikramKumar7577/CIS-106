last_names = ["Sal", "Johnson", "Williams", "Jones", "Brown",
      "Davis", "Miller", "Dora", "Boots", "Diego"]

exam_scores = [85, 92, 78, 88, 90, 84, 95, 76, 89, 91]

def display_names_and_scores(names, scores):
    print("\nNames and Exam Scores in order:")
    for i in range(len(names)):
        print(names[i], "-", scores[i])


def display_names_and_scores_reverse(names, scores):
    print("\nNames and Exam Scores in reverse order:")
    for i in range(len(names)-1, -1, -1):
        print(names[i], "-", scores[i])

display_names_and_scores(last_names, exam_scores)
display_names_and_scores_reverse(last_names, exam_scores)