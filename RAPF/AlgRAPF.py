import pandas as pd
import random
import math
from timeit import default_timer as timer

import os
import pandas as pd



cpath = os.getcwd()
for i in range(0, 1):
parent_directory = os.path.split(cpath)[0]
fpath1 = os.path.join(parent_directory, "data/rn_10k_n_1k.csv")    
df1 = pd.read_pickle(fpath)
fpath2 = os.path.join(parent_directory, "data/1k_attribute.csv")    
df2 = pd.read_pickle(fpath)

fpath2 = os.path.join(parent_directory, "data/top25_dfs.pickle")    
df = pd.read_pickle(fpath)


numRank = 10000
numItem = 1000


rankArray = {}
for i in range(0,numRank):
    rankArray[i] = []

for  i in range(0,numItem):
    rArr = df1[str(i)]
    for j in range(0,numRank):
        rankArray[j].append(rArr[j])


rank = rankArray[0]
group = df2['protected attribute']



def GrBinaryIPFDelta(rank,group):
    Rho0 = []
    Rho1 = []
    for i in rank:
        if group[i] == 1:
            Rho0.append(i)
        else:
            Rho1.append(i)

    j = 1
    rankDic = {}
    for itm in rank:
        rankDic[itm] = j
        j = j + 1

    urgent = []
    Rout = []
    P1count = 0
    P0count = 0

    Fp0 = len(Rho0)/len(rank)
    Fp1 = len(Rho1)/len(rank)

    i = 1
    while len(Rho0) != 0 or len(Rho1) != 0:
        if P1count >= len(Rho1):
            Rout.extend(Rho0[P0count:len(Rho0)])
            return Rout
        if P1count >= len(Rho0):
            Rout.extend(Rho1[P1count:len(Rho1)])
            return Rout

        if P1count < len(Rho1) and  P0count < len(Rho0):

            if len(urgent) == 0:
                if rankDic[Rho1[P1count]] < rankDic[Rho0[P0count]]:
                    Rout.append(Rho1[P1count])
                    P1count = P1count + 1
                else:
                    Rout.append(Rho0[P0count])
                    P0count = P0count + 1
            else:
                if urgent[0] == 'P1':
                    Rout.append(Rho1[P1count])
                    P1count = P1count + 1
                else:
                    Rout.append(Rho0[P0count])
                    P0count = P0count + 1
                urgent = []
        else:
            break
        # update urgent
        delta = 4

        if Fp1 * (i + 1) - P1count >= delta:
            urgent.append('P1')

        if Fp0 * (i + 1) - P0count >= delta:
            urgent.append('P0')
        i = i + 1
        #print(i)

    return  Rout

import timeit


def kendalTau(P,Q):
    qInv = {}
    pInv = {}
    for key in P:
        #print(key, P[key])
        val = P[key]
        pInv[val] = key
    for key in Q:
        #print(key, Q[key])
        val = Q[key]
        qInv[val] = key

    qTrans = {}
    #qTransInv = {}
    for key in Q:
        #print(key, Q[key])
        value = Q[key]
        newVal = pInv[value]
        qTrans[key] = newVal
        #qTransInv[newVal] = key

    dis = 0
    for key in qTrans:
        dis = dis + abs(key - qTrans[key])

    return dis


start = timeit.default_timer()

timeRequired = 0
numRun = 1

Pin = []
Qin = []
outRank = []
for v in range(0,numRun):
    fairRanks = []
    minDistance = 100000000
    for u in range(0,len(rankArray)):

        rank = rankArray[u]

        Rout = GrBinaryIPFDelta(rank,group)

        Pin= rank
        Qin = Rout
        P = {}
        Q = {}
        for i in range(0, len(Rout)):
            P[i] = Pin[i]
            Q[i] = Qin[i]
        distance = kendalTau(P,Q)
        if distance < minDistance:
            minDistance = distance
            outRank = Rout
        fairRanks.append(Rout)

    #outRank = fairRanks[random.randint(0,len(fairRanks) - 1)]
    #print(outRank)

end = timeit.default_timer()
timeRequired = timeRequired + end - start
print('time required = ', timeRequired/numRun)


#print(outRank)






