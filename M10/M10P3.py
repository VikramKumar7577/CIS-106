total_msrp = 0
total_sales = 0
repeat = input("Do you want to calculate the out-the-door price for an automobile? (Yes or No): ")
while repeat.lower() == "yes":
    make = input("Enter make: ")
    model = input("Enter model: ")
    ev_code = input("Is it an electric vehicle? (Y or N): ")
    msrp = int(input("Enter MSRP: "))

    if ev_code.lower() == "y":
            discount_percent = 30
    elif make.lower() == "honda" and model.lower() == "accord":
            discount_percent = 10
    elif make.lower() == "toyota" and model.lower() == "rav4":
            discount_percent = 15
    else:
            discount_percent = 5

    discount_amount = msrp * discount_percent // 100
    new_msrp = msrp - discount_amount
    total_price = new_msrp * 107 // 100 

    total_msrp += msrp
    total_sales += total_price

    print("Out-the-door price for this automobile is:", total_price)
    print()
    repeat = input("Do you want to calculate the out-the-door price for an automobile? (Yes or No): ")

    print("Total MSRP of all automobiles is:", total_msrp)
    print("Total sales price of all automobiles is:", total_sales)