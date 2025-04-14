last_names = ["Sal", "Johnson", "Williams", "Jones", "Brown",
              "Davis", "Miller", "Dora", "Boots", "Diego"]


def display_names(names):
    print("Names in order:")
    for i in range(len(names)):
        print(names[i])


def display_names_reverse(names):
    print("\nNames in reverse order:")
    for i in range(len(names)-1, -1, -1):
        print(names[i])


display_names(last_names)
display_names_reverse(last_names)