part_number = input("Enter part number: ")
quantity = int(input("Enter quantity: "))

if part_number == "10" or part_number == "55":
    cost_per_unit = 1.00
else:
    if part_number == "99":
        cost_per_unit = 2.00
    else:
        if part_number == "80" or part_number == "70":
            cost_per_unit = 3.00
        else:
            cost_per_unit = 5.00

total_cost = quantity * cost_per_unit

print("Cost per unit:", cost_per_unit)
print("Total cost:", total_cost)