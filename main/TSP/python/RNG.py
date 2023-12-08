from nottext2dec import *
from TSP import *
import os
import time

class RNG:
    def __init__(self, a=nottext2dec().sumtext(), c=0, m=2**31-1, seed = None): #Random number generation that I found on wiki
        self.a = a  #using linear congruential generator algorithm, a values has many values base on which program languages and
        self.c = c  #libraries we use, so I came up with my own value. No, don't dig in, honestly...
        self.m = m
        if seed: self.x0 = seed
        else: self.x0 = int(os.getpid()+time.time())
        self.x_prev = (self.a * self.x0 + self.c) % self.m
    def PRNG(self, numrange=None): #this function return values, if there's no numrange, it return itself, if there is...
        self.x_prev = (self.a * self.x_prev + self.c) % self.m 
        if numrange:
            return int((self.x_prev / (self.m - 1)) * (numrange[1] - numrange [0]) + numrange[0]) #uhm... there's the... math
        else:
            return self.x_prev
    def distance(self, n): #random the distance
        distance = {}
        for i in range(n):
            for j in range(i+1,n):
                distance[(i,j)] = self.PRNG([1,100])
        return distance