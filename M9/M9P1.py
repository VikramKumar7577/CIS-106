qty = int(input("Enter quantity: "))
price = int(input("Enter unit price: "))

extprice = qty * price

if extprice > 10000:
    extprice = extprice * 0.9

print("Qty =", qty)
print("Unit Price =", price)
print("Extended Price =", int(extprice))