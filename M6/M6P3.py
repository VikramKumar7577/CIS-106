principle = int(input("Enter principle amount: "))
years = int(input("Enter years to maturity: "))

if principle > 100000:
    if years == 5:
        rate = 0.06
else:
    if principle >= 50000:
        if years == 10:
            rate = 0.05
        else:
            if years == 5:
                rate = 0.04
    else:
        rate = 0.02

interest = principle * rate

print("Interest Rate:", rate * 100, "%")
print("Interest Amount for First Year:", interest)
