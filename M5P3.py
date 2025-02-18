num_books = int(input("Enter number of books: "))
cost_per_book = float(input("Enter cost per book: $"))
order_total = num_books * cost_per_book

if order_total > 50.00:
    shipping_charge = 0.00
else:
    shipping_charge = 25.00

print(f"Order Total: ${order_total:.2f}")
print(f"Shipping Charge: ${shipping_charge:.2f}")



















