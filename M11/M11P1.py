def compute_discount(qty, price, discount_rate):
  total_cost = float(qty) * float(price)
  discount_amount = total_cost * float(discount_rate)
  discounted_price = total_cost - discount_amount
  return discount_amount, discounted_price

qty = float(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate (e.g., 0.1 for 10%): "))
disc_amt, disc_price = compute_discount(qty, price, discount_rate)
print("Discount Amount:", disc_amt)
print("Discounted Price:", disc_price)
