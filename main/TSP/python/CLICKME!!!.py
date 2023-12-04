from TSP import *
from RNG import *

n = int(input("Number of cities: "))
seed = seed_input()
if seed: d = RNG(seed).distance(n)
else: d = RNG().distance(n)
tsp = TSP(n, d)
print("Distance of the cities:",d,"\nShortest way is:",tsp[1],"with the distance of:",tsp[0])
