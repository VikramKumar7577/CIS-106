item = input("Enter item: ")
quantity = int(input("Enter quantity: "))

if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

extended_price = quantity * unit_price

print(f"Item: {item}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")


















