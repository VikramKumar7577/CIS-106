appliance_name = input("Enter appliance name: ")
appliance_cost = float(input("Enter cost: $"))

if appliance_cost > 1000:
    warranty_rate = 0.10
else:
    warranty_rate = 0.05

warranty_cost = appliance_cost * warranty_rate
total_cost = appliance_cost + warranty_cost

print(f"Appliance: {appliance_name}")
print(f"Cost: ${appliance_cost:.2f}")
print(f"Warranty Cost: ${warranty_cost:.2f}")
print(f"Total: ${total_cost:.2f}")


















