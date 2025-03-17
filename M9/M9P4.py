last = input("Enter employee’s last name: ")
job = input("Enter job code (L/A/J): ")
hours = int(input("Enter hours worked: "))

if job == "L":
    rate = 25
elif job == "A":
    rate = 30
elif job == "J":
    rate = 50
else:
    rate = 0
if hours > 40:
    gross = 40 * rate + (hours - 40) * rate * 3 // 2
else:
    gross = hours * rate

print("Employee:", last)
print("Gross Pay =", gross)