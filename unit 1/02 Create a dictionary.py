
players = {}

n = int(input("Enter number of players: "))


for i in range(n):
    name = input("Enter player name: ")
    score = int(input("Enter score: "))
    players[name] = score

print("\nPlayers and Scores:")
print(players)

search_name = input("\nEnter player name to find score: ")


if search_name in players:
    print(search_name, "scored", players[search_name], "runs.")
else:
    print("Player not found.")
