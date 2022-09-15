import networkx as nx
import networkx as nx
from networkx.algorithms import bipartite
import random
import math


def ApproxMultiValuedIPF(rank,group):
    rankGrp = {}
    for i in range(0,len(rank)):
        rankGrp[rank[i]] = group[i]

    grpCount = {}
    for i in group:
        grpCount[i] = 0

    rankGrpPos = {}
    for i in rank:
        grpCount[rankGrp[i]] = grpCount[rankGrp[i]] + 1
        rankGrpPos[i] = grpCount[rankGrp[i]]

    rankRange = {}
    for item in rank:
        i = rankGrpPos[item]
        n = numberOfItem
        fp = grpCount[rankGrp[item]]
        r1 = math.floor(i*n/fp)
        r2 = math.ceil((i+1)*n/fp) - 1
        if r2 > numberOfItem:
            r2 = numberOfItem
        rankRange[item] = (r1,r2)


    B = nx.Graph()
    top_nodes = []
    bottom_nodes = []

    for i in rank:
        top_nodes.append(i)
        bottom_nodes.append(str(i))
    B.add_nodes_from(top_nodes, bipartite=0)
    B.add_nodes_from(bottom_nodes, bipartite=1)

    for i in rank:
        r1,r2 = rankRange[i]
        #print(r1,r2)
        for j in range(1,numberOfItem+1):
            if j >= r1 and j <= r2:
                print(i,j)
                B.add_edge(i, str(j), weight = abs(i-j))
            else:
                B.add_edge(i, str(j), weight=1000000000)
                print(i,j)

    my_matching = nx.algorithms.bipartite.minimum_weight_full_matching(B, top_nodes, "weight")

    print(my_matching)