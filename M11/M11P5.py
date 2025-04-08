total = 0
tax = 0

def compute_total_tax(quantity, unit_price):
    global total, tax
    total = quantity * unit_price
    tax = total * 0.07

quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

compute_total_tax(quantity, unit_price)

print("Total: $", total)
print("Tax: $", tax)