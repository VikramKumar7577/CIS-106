last_name = input("Enter last name: ")
num_dependents = int(input("Enter number of dependents: "))
gross_income = float(input("Enter gross income: $"))

adjusted_gross = gross_income - (num_dependents * 12000)

if adjusted_gross > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

income_tax = adjusted_gross * tax_rate

if income_tax < 0:
    income_tax = 100.00

print(f"Last Name: {last_name}")
print(f"Gross Income: ${gross_income:.2f}")
print(f"Dependents: {num_dependents}")
print(f"Adjusted Gross Income: ${adjusted_gross:.2f}")
print(f"Income Tax: ${income_tax:.2f}")

















