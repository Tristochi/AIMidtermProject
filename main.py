import numpy as np

def simulate_race(players):
    players.sort(key=lambda x: x[1], reverse=True)

    players = players[:-2]
    return players 

def find_top_3_players(players):
    rounds = 0
    #Break players down into a list of 5x5 matrices
    remainder = 0
    if len(players) % 25 != 0:
        remainder = len(players) % 25
    


    
    return rounds

n = 2000
total_rounds = 0

#for i in range(n):        
#    players = [(i, np.random.rand()) for i in range(125)]
#    rounds = find_top_3_players(players)
#    total_rounds += rounds 

#average_rounds = total_rounds / n 
#print(average_rounds)

players = [(i, np.random.rand()) for i in range(126)]
print('Before slice: ')
print(len(players))

remainder = 0
if len(players) % 25 != 0:
    remainder = len(players) % 25
    the_end = players[-remainder:]
    print(len(the_end))

players = players[:-remainder]
print('After slice: ')
print(len(players))


matrices =[]
tmp = []
for i in range(0, len(players), 5):
    tmp.append(players[i:i+5])
    #print(len(tmp))
    if len(tmp) % 5 == 0:
        matrices.append(tmp)
        tmp = []

for matrix in matrices:
    print(matrix)
    print('\n')