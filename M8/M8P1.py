principal_amount = int(input("Enter principle amount: "))
interest_rate = float(input("Enter interest rate: "))

total_interest = 0


print("\nYear\tBeginning Balance\tEnding Balance")


for year in range(1, 6):
    interest = int(principal_amount * interest_rate)
    ending_balance = principal_amount + interest
    print(f"{year}\t${principal_amount:,.2f}\t${ending_balance:,.2f}")
    total_interest += interest
    principal_amount = ending_balance


print(f"\nTotal interest earned: ${total_interest:,.2f}")
