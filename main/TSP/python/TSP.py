from itertools import permutations
from input import distance_input

def TSP(n, distance = None):
    shortest = None
    mincost = None
    if distance is None: distance = distance_input(n)
    for i in permutations(range(n), n):  #Permutation the number so we can get all the path
        if i[0] != 0: continue  #Since we start at 0, so if the starting point is not 0, we skip
        s = 0
        for j in i:
            if j == 0:
                k = j
                continue
            if k > j: s += distance[(j,k)] #Just sum up the distance, you might know the rest of it
            else: s += distance[(k,j)]
            k = j
        if shortest is None: shortest = i
        if mincost is None: mincost = s
        if mincost > s:
            shortest = i
            mincost = s
    return mincost, shortest