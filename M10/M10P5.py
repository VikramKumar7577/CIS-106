total_market_value = 0
total_assessed_value = 0
repeat = input("Do you want to calculate the assessed value of a home? (Yes or No): ")
while repeat.lower() == "yes":
    county = input("Enter county: ")
    market_value = int(input("Enter market value: "))

    county_lower = county.lower()
    if county_lower == "cook":
        assessed_percent = 90
    elif county_lower == "dupage":
        assessed_percent = 80
    elif county_lower == "mchenry":
        assessed_percent = 75
    elif county_lower == "kane":
        assessed_percent = 60
    else:
        assessed_percent = 70

    assessed_value = market_value * assessed_percent // 100

    total_market_value += market_value
    total_assessed_value += assessed_value

    print("Assessed value for the home in", county, "is:", assessed_value)
    print()
    repeat = input("Do you want to calculate the assessed value of a home? (Yes or No): ")

print("Total market value of all homes is:", total_market_value)
print("Total assessed value of all homes is:", total_assessed_value)

print("\nAll tasks completed!")