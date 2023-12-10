from TSP import *
from RNG import *
from input import *
import time

n = number_input("cities")
seed = seed_input()

start_time = time.time() #Start the execution
if seed: d = RNG(seed).distance(n)
else: d = RNG().distance(n)
method3 = TSP(n, d).Dijkstra()
end_time = time.time() #Ends the execution

counted_time = end_time - start_time
not_input(n,d,method3,counted_time)