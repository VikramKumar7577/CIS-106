player_names = []
batting_averages = []

try:
    with open("players.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            player_names.append(parts[0])
            batting_averages.append(float(parts[1]))
except FileNotFoundError:
    print("\nFile players.txt not found!")


def display_players(names, averages):
    print("\nPlayer Names and Batting Averages:")
    for i in range(len(names)):
        print(names[i], "-", averages[i])


def search_player(names, averages, search_name):
    found = False
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print("\nPlayer Found:")
            print(names[i], "-", averages[i])
            found = True
            break
    if not found:
        print("\nName not found.")  # <-- This line Problem 5

if player_names and batting_averages:
    display_players(player_names, batting_averages)

    answer = "y"
    while answer == "y":
        search_name = input("\nEnter a player last name to search: ")
        search_player(player_names, batting_averages, search_name)
        answer = input("\nSearch for another player? (y/n): ").lower()