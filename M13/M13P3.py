players = {}

try:
    f = open("players.txt", "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 2:
            name = parts[0]              
            avg = float(parts[1])        
            players[name] = avg
except:
    print("Could not load players.txt")


def print_players(player_dict):
    print("Player\t\tAverage")
    print("-------------------------")
    for name in player_dict:
        print(name, "\t", player_dict[name])


print_players(players)