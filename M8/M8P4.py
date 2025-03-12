with open("orders.txt", "r") as file:
  lines = file.readlines()

total_cost = 0
order_count = 0

print("Item\tQuantity\tPrice\tExtended Price")

for i in range(0, len(lines), 3):
  item = lines[i].strip()
  quantity = int(lines[i + 1].strip())
  price = int(lines[i + 2].strip())
  extended_price = quantity * price

  print(f"{item}\t{quantity}\t${price}\t${extended_price}")
  total_cost += extended_price
  order_count += 1

average_order = total_cost // order_count if order_count else 0
print(f"Total cost: ${total_cost}, Number of orders: {order_count}, Average order: ${average_order}")
