from itertools import permutations 

def dainput():
    asking = input("Import your seed? (y/n) ")
    if (asking == "y" or asking == "Y"):
        seed = int(input("Seed: "))
    else:
        seed = None
        if (asking == "n" or asking == "N"):
            print("Well, you choose randomized then")
        else:
            print ("GO TO HELL!")
    return seed

def inputdistance(n):
    distance = {}
    for i in range(n):
        for j in range(i+1,n):
            distance[(i,j)] = int(input("Distance of city " + str(i) + " and city " + str(j) + " is: "))
    return distance

def TSP(n, distance = None):
    shortest = None
    mincost = None
    if distance is None: distance = inputdistance(n)
    for i in permutations(range(n), n):
        if i[0] != 0: continue
        s = 0
        for j in i:
            if j == 0:
                k = j
                continue
            if k > j: s += distance[(j,k)]
            else:
                s += distance[(k,j)]
            k = j
        if shortest is None: shortest = i
        if mincost is None : mincost = s
        if mincost > s:
            shortest = i
            mincost = s
    return mincost, shortest