def bowling_scores(score1, score2, score3, handicap):
    average = (score1 + score2 + score3) / 3
    average_with_handicap = average + handicap
    return average, average_with_handicap

last_name = input("Enter bowler's last name: ")
score1 = int(input("Enter first game score: "))
score2 = int(input("Enter second game score: "))
score3 = int(input("Enter third game score: "))
handicap = int(input("Enter handicap: "))

average, average_with_handicap = bowling_scores(score1, score2, score3, handicap)

print("Bowler Last Name:", last_name)
print("Average Score:", average)
print("Average Score with Handicap:", average_with_handicap)