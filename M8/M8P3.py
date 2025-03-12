with open("employees.txt", "r") as file:
  lines = file.readlines()

total_bonus = 0
print("Employee\tSalary\tBonus")

for i in range(0, len(lines), 2):
  name = lines[i].strip()
  salary = int(lines[i + 1].strip())

  if salary >= 100000:
      rate = 20
  elif salary >= 50000:
      rate = 15
  else:
      rate = 10

  bonus = (salary * rate) // 100
  total_bonus += bonus

  print(f"{name}\t${salary}\t${bonus}")

print(f"Total bonuses paid: ${total_bonus}")