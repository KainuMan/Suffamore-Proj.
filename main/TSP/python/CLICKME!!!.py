from TSP import *
from RNG import *
import time

n = int(input("Number of cities: "))
seed = seed_input()

start_time = time.time() #Start the execution
if seed: d = RNG(seed).distance(n)
else: d = RNG().distance(n)
tsp = TSP(n, d)
print("Distance of the cities:",d,"\nShortest way is:",tsp[1],"with the distance of:",tsp[0])
end_time = time.time() #Ends the execution

counted_time = end_time - start_time
print(f"Calculation time: {counted_time} seconds.")
