from FairILP import FairIlp
import os
import pandas as pd



cpath = os.getcwd()
for i in range(0, 1):
parent_directory = os.path.split(cpath)[0]
fpath = os.path.join(parent_directory, "data/top25_dfs.pickle")    
object = pd.read_pickle(fpath)


data = object[1]
num_of_player = 15
data = data[0:num_of_player]
data = data.transpose()
players = data.keys()



##randomize
i = 0

for index in data.index:
    if index == 'Division':
        break
    j = 0
    for player in players:
       # print(i,j)
        data.loc[index,player] = data[i][j]
        j = j + 1
    i = i + 1

nrow = len(data)
ncol = int(data.size/len(data))
#print(nrow,ncol)
return (data,players,nrow,ncol)
    
    
def KendallTau(P,Q):
    combinations = [p for p in itertools.product(players, repeat=2)]
    distance = 0
    for tup in combinations:
        if P[tup[0]] < P[tup[1]] and  Q[tup[1]] < Q[tup[0]]:
            distance = distance + 1
    return distance
    
    
data,players,nrow,ncol = genData()
avgfair = FairIlp(data,players,nrow,ncol)