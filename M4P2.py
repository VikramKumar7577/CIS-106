shares=input("Enter the amount of shares you own:")
cost_share_purchased=input("Enter the cost per share when purchased:")
cost_share_current=input("Enter the current cost per share:")
calc_profit=float(cost_share_purchased)-float(cost_share_current)*float(shares)
print("The profit is:", calc_profit)