players = {}

f = open("players.txt", "r")
lines = f.readlines()
f.close()

for line in lines:
    parts = line.strip().split(",")
    if len(parts) == 2:
        name = parts[0]
        avg = float(parts[1])
        players[name] = avg

def print_players(player_dict):
    print("Player\t\tAverage")
    print("-------------------------")
    for name in player_dict:
        print(name, "\t", player_dict[name])

print_players(players)

print("\nProblem 4: Look Up Player\n")
answer = input("Look up a player? (y/n): ").lower()
while answer == "y":
    name = input("Enter player name: ")
    if name in players:
        print(name, "'s average is", players[name])
    else:
        print("Player not found.")
    answer = input("Look up another? (y/n): ").lower()