def get_area():
    room = input("Enter room name: ")
    length = float(input("Length: "))
    width = float(input("Width: "))
    height = float(input("Height: "))
    wall_area = 2 * (length * height + width * height)
    return room, wall_area


paint_dict = {}

answer = input("Add a room? (y/n): ").lower()
while answer == "y":
    room, area = get_area()
    gallons = -(-area // 50)  
    paint_dict[room] = gallons
    answer = input("Add another room? (y/n): ").lower()


print("\nRoom\t\tGallons")
print("-------------------------")
for room in paint_dict:
    print(room, "\t", paint_dict[room])