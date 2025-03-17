count = 0
last = input("Enter player’s last name: ")
hits = int(input("Enter hits: "))
at_bats = int(input("Enter at bats: "))

if at_bats > 0:
    avg = hits / at_bats
else:
    avg = 0

print("Player:", last)
print("Batting Average =", avg)
count = count + 1
print("Total players entered =", count)