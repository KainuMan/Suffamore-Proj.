from itertools import permutations
from input import distance_input

def TSP(n, distance = None):
    shortest = None
    mincost = None
    if distance is None: distance = distance_input(n)
    for i in permutations(range(1,n), n-1):  #Permutation the number so we can get all the path
        for j in i:
            if j == i[0]: s = distance[i[0]][0]
            elif k > j: s += distance[k][j] #Just sum up the distance, you might know the rest of it
            else: s += distance[j][k]
            if mincost:
                if s > mincost: break
            k = j
        if not mincost: mincost = s
        if mincost > s:
            shortest = i
            mincost = s
    return mincost, shortest