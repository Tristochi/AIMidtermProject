import numpy as np

class RaceSim:
    def __init__(self):
        self.rounds = 0

    def create_matrices(self, players):
        remainder = 0
        the_end = []
        if len(players) % 25 != 0:
            remainder = len(players) % 25
            the_end = players[-remainder:]
            players = players[:-remainder]


        matrices =[]
        tmp = []
        if len(players) > 0:
            for i in range(0, len(players), 5):
                tmp.append(players[i:i+5])
                #print(len(tmp))
                if len(tmp) % 5 == 0:
                    matrices.append(tmp)
                    tmp = []

        tmp = []
        matrix = []
        if len(the_end) > 0:
            for j in range(len(the_end)):
                if len(tmp) <= 5:
                    tmp.append(the_end[j])
                    
                if len(tmp) == 5 or j == len(the_end)-1:
                    matrix.append(tmp)
                    tmp = []
                
                if j==len(the_end)-1:
                    matrices.append(matrix)

        return matrices


    def simulate_races(self, players):
        if len(players) <= 5:
            #Base case. Return fastest three runners
            players.sort(key=lambda racer: racer[1], reverse=False)
            self.rounds+=1
            return [players[0], players[1], players[2]]
        
        #Break players down into a list of 5x5 matrices
        the_matrices = self.create_matrices(players)
        winners = []

        #Do the initial sorting 
        for matrix in the_matrices:
            for list in matrix:
                list.sort(key=lambda racer: racer[1], reverse=False)
                self.rounds += 1
            
            #Gather all the winners into new matrices
            #Check if necessary for 7th test
            if len(matrix) == 5:
                tmp = [matrix[0][0], matrix[0][1], matrix[0][2]]

            for i in range(len(matrix)):
                if (len(the_matrices) == 2 and len(matrix)) == 5:
                    for j in range(3):
                        if i < 2:
                            if matrix[i][j] < tmp[0]:
                                #print(str(matrix[i][j]) + ' < ' + str(tmp[0]))
                                tmp[0] = matrix[i][j]
                            elif matrix[i][j] < tmp[1]:
                                #print(str(matrix[i][j]) + ' < ' + str(tmp[1]))
                                tmp[1] = matrix[i][j]
                            elif matrix[i][j] < tmp[2]:
                                #print(str(matrix[i][j]) + ' < ' + str(tmp[2]))
                                tmp[2] = matrix[i][j]
                    if i>2:
                        tmp.append(matrix[i][0])
                elif (len(the_matrices) == 2 and len(matrix) < 5):
                    tmp.append(matrix[i][0])
                    if i == len(matrix)-1:
                        return self.simulate_races(tmp)

                if len(the_matrices) == 1:
                    #Look for 7th check on final matrix of 25 racers
                    for j in range(3):
                        if i < 2:
                            if matrix[i][j] < tmp[0]:
                                #print(str(matrix[i][j]) + ' < ' + str(tmp[0]))
                                tmp[0] = matrix[i][j]
                            elif matrix[i][j] < tmp[1]:
                                #print(str(matrix[i][j]) + ' < ' + str(tmp[1]))
                                tmp[1] = matrix[i][j]
                            elif matrix[i][j] < tmp[2]:
                                #print(str(matrix[i][j]) + ' < ' + str(tmp[2]))
                                tmp[2] = matrix[i][j]
                    if i>2:
                        tmp.append(matrix[i][0])
                else:
                    #This is the normal case
                    winners.append(matrix[i][0])
            if len(tmp) > 3:
                tmp.sort(key=lambda racer:racer[1], reverse=False)
                self.rounds+=1
                
                return self.simulate_races(tmp)

        return self.simulate_races(winners)

n = 2000
total_rounds = 0
sample_size = 999
for i in range(n):
    players = [(i, np.random.rand()) for i in range(sample_size)]
    sim = RaceSim()
    top_three = sim.simulate_races(players)
    rounds = sim.rounds
    total_rounds += rounds

average_rounds = total_rounds/n 
print('n is: ' + str(n))
print('Sample size is: ' + str(sample_size))
print('Average Rounds: ' + str(average_rounds))
print('Top three racers: ')
print(top_three)

