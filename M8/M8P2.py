a, b = 1, 1
print("Fibonacci Sequence:")
for _ in range(20):
    print(a, end=" ")
    a, b = b, a + b
print()