quantity = int(input("Enter quantity of widgets: "))

if quantity > 10000:
    price = 10
else:
    if quantity >= 5000:
        price = 20
    else:
        price = 30

extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

print("Extended Price:", extended_price)
print("Tax Amount:", tax)
print("Total:", total)
