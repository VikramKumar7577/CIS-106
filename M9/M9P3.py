trips = 0

while True:
    city = input("Enter destination city (or 'quit' to end): ")
    if city.lower() == 'quit':
        break
        
    miles = int(input("Enter miles traveled: "))
    gallons = int(input("Enter gallons used: "))

    if gallons > 0:
        mpg = miles / gallons
    else:
        mpg = 0

    print("Destination City:", city)
    print("Miles =", miles)
    print("MPG =", mpg)
    trips += 1

print("\nTotal trips taken:", trips)
