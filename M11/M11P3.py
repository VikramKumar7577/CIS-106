def sales_info(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
    next_year_target = sales * 1.05  
    return commission, next_year_target


last_name = input("Enter salesperson's last name: ")
sales = float(input("Enter sales amount: "))

commission, next_year_target = sales_info(sales)

print("Salesperson Last Name:", last_name)
print("Commission: $", commission)
print("Next Year's Target: $", next_year_target)