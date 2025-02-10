meal_cost = input("Enter the cost of the meal: ")
meal_cost = float(meal_cost)
tip_fifteen = meal_cost * 0.15
tip_eighteen = meal_cost * 0.18
tip_twenty = meal_cost * 0.20
total_fifteen = meal_cost + tip_fifteen
total_eighteen = meal_cost + tip_eighteen
total_twenty = meal_cost + tip_twenty
print()
print("With 15% tip: ")
print("Total: ".ljust(15), "{:10.2f}".format(meal_cost))
print("Tip: ".ljust(15), "{:10.2f}".format(tip_fifteen))
print("Total with tip ".ljust(15), "{:10.2f}".format(total_fifteen))
print()  


print("With 18% tip: ")
print("Total: ".ljust(15), "{:10.2f}".format(meal_cost))
print("Tip: ".ljust(15), "{:10.2f}".format(tip_eighteen))
print("Total with tip ".ljust(15), "{:10.2f}".format(total_eighteen))
print()  


print("With 20% tip: ")
print("Total: ".ljust(15), "{:10.2f}".format(meal_cost))
print("Tip: ".ljust(15), "{:10.2f}".format(tip_twenty))
print("Total with tip ".ljust(15), "{:10.2f}".format(total_twenty))



















