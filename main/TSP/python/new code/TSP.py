from input import distance_input
from RNG import *

class TSP:
    def __init__(self,n, distance = None):
        self.n = n
        self.x = 0
        self.x_prev = 0
        self.distance = distance


    def world_tour_gen(self):
        map=[[0]]
        a = [True]
        for i in range(1,self.n):
            a.append(False)
        map.append(a)
        return map
    
    def min_out_Heuristic(self):
        s = 0
        m= self.world_tour_gen()
        x = 0 #current city
        while m[1].count(True)<self.n:
            d=[[],[]] #open node
            for i in range(1,self.n):
                if i == x or m[1][i] == True: continue
                if i > x: d[1].append(self.distance[i][x])
                else: d[1].append(self.distance[x][i])
                d[0].append(i)
            print("Current node:",x,"\tExpanded node:",d[0])
            s += min(d[1])
            x = d[0][d[1].index(min(d[1]))]
            m[0].append(x)
            m[1][x] = True
        return s,m[0]
