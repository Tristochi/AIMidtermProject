import numpy as np

def simulate_race(players):
    # Sort players based on their speed
    sorted_players = sorted(players, key=lambda x: x[1], reverse=True)
    # Return the top 5 fastest players
    return sorted_players[:5]

def find_top_3_fastest(players):
    while len(players) > 5:
        # Divide players into groups of 5 for each round of testing
        groups = [players[i:i+5] for i in range(0, len(players), 5)]
        # Simulate races for each group and select the top 5 fastest from each
        winners = [simulate_race(group) for group in groups]
        # Flatten the list of winners
        players = [player for group in winners for player in group]
        # Keep only the top 5 players overall
        players = players[:5]
    # After finding the top 5 players, sort and return the top 3 fastest
    top_3 = sorted(players, key=lambda x: x[1], reverse=True)[:3]
    return top_3

# Test with 25 players
players = [(i, np.random.rand()) for i in range(25)]
top_3_fastest = find_top_3_fastest(players)
print("Top 3 fastest players:")
for i, player in enumerate(top_3_fastest, 1):
    print(f"{i}. Player {player[0]} with speed {player[1]}")