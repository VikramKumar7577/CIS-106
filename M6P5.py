last_name = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
job_level = int(input("Enter job level: "))

if job_level >= 10:
    bonus_rate = 0.25
else:
    if job_level >= 5:
        bonus_rate = 0.20
    else:
        bonus_rate = 0.10

bonus = salary * bonus_rate

print("Employee:", last_name)
print("Bonus:", bonus)
