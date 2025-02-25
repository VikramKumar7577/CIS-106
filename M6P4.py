quantity = int(input("Enter number of tickets: "))

if quantity >= 25:
    price_per_ticket = 50
else:
    if quantity >= 10:
        price_per_ticket = 60
    else:
        if quantity >= 5:
            price_per_ticket = 70
        else:
            price_per_ticket = 75

total_cost = quantity * price_per_ticket

print("Price per Ticket:", price_per_ticket)
print("Total Cost:", total_cost)