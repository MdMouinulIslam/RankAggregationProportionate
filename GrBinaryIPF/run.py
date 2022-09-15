import pandas as pd
import os
import pandas as pd
from GrBinaryIPF import GrBinaryIPF

cpath = os.getcwd()
 for i in range(0, 1):
    parent_directory = os.path.split(cpath)[0]
fpath = os.path.join(parent_directory, "data/top25_dfs.pickle")    
object = pd.read_pickle(fpath)
data = object[1]
num_of_player = 30
data = data[0:num_of_player]
data = data.transpose()
players = data.keys()
itemList = data.keys()
G1 = []
G2 = []
row = data.iloc[25, :]
for i in range(0,num_of_player):
    if(row[i] == 0):
        G1.append(players[i])
    else:
        G2.append(players[i])


p1 = len(G1)/len(itemList)
p2 = len(G2)/len(itemList)

rank = data.iloc[1, :]
ranktup = []
j = 0
for i in rank:
    ranktup.append((i,j))
    j = j + 1
ranktup.sort()
rank = []
for i,j in ranktup:
    rank.append(j)   
tup = []
for i in range(0,len(rank)):
    tup.append((rank[i],i))
rank = []
tup.sort()
for i,j in tup:
    rank.append(j)
    
    
rankOut = GrBinaryIPF(rank,group)

