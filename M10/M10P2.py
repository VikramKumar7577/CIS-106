repeat = input("Do you want to calculate paint needed for a room? (Yes or No): ")
while repeat.lower() == "yes":
    length = int(input("Enter length of room: "))
    width = int(input("Enter width of room: "))
    height = int(input("Enter height of room: "))

    wall_area = 2 * (length * height) + 2 * (width * height)
    gallons = wall_area // 50

    print("Wall area is:", wall_area, "square feet")
    print("Gallons of paint needed for walls:", gallons)
    print()  

    repeat = input("Do you want to calculate paint needed for a room? (Yes or No): ")