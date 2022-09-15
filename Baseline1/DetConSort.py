
#DetConstSort implementation
#input: S = scores, A = groups, P = portions, kmax 
#output: ranked item list, scores of each item

def DetConstSort(S,A,P,kmax):
    counts = {}
    minCounts = {}
    for ai in A:
        counts[ai] = 0
        minCounts[ai] = 0
    
    rankedAttList = {}
    rankedScoreList = {}
    maxIndices = {}
    lastEmpty = 0
    k = 0
    
    while lastEmpty <= kmax:
        k = k + 1
        tempMinCounts = {}
        for ai in A:
            tempMinCounts[ai] = math.floor(k * P[ai])
        changedMins = []
        for ai in A:
            if minCounts[ai ] < tempMinCounts[ai]:
                changedMins.append((S[ai][counts[ai]],ai))
        if len(changedMins) != 0 :
            changedMins.sort(reverse=True)
            #ordChangedMins = changedMins
        for sai,ai in  changedMins:
            rankedAttList[lastEmpty] = ai
            
            rankedScoreList[lastEmpty] = S[ai][counts[ai]]
            maxIndices[lastEmpty] = k
            start = lastEmpty
            while start > 0 and maxIndices[start - 1] >= start and rankedScoreList[start-1] < rankedScoreList[start]:
                swap(maxIndices,start - 1,start)
                swap(rankedAttList,start - 1, start)
                swap(rankedScoreList,start - 1, start)
                start = start - 1
            counts[ai] = counts[ai] + 1 
            lastEmpty = lastEmpty + 1
        minCounts = tempMinCounts
    return (rankedAttList, rankedScoreList)
    
    

#example input set for DetConstSort
S={}
for a in A:
    size = random.randint(20, 200)
    scoreList = []
    for i in range(0,size):
        score = random.randint(0, 10000)/10000
        scoreList.append(score)
    scoreList.sort(reverse=True)
    #print(scoreList)
    S[a] = scoreList
P = {'a1':0.20,'a2':0.35,'a3':0.10,'a4':0.15,'a5':0.05,'a6':0.15}
kmax = 10

rankedAttList, rankedScoreList = DetConstSort(S,A,P,kmax)