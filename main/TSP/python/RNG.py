from nottext2dec import *
from TSP import *
import os
import time

class RNG:
    def __init__(self, a=nottext2dec().sumtext(), c=0, m=2**31-1, seed = None):
        self.a = a
        self.c = c
        self.m = m
        if seed: self.x0 = seed
        else: self.x0 = int(os.getpid()+time.time())
        self.x_prev = (self.a * self.x0 + self.c) % self.m
    def PRNG(self, numrange=None):
        self.x_prev = (self.a * self.x_prev + self.c) % self.m
        if numrange:
            return int((self.x_prev / (self.m - 1)) * (numrange[1] - numrange [0]) + numrange[0])
        else:
            return self.x_prev
    def distance(self, n):
        distance = {}
        for i in range(n):
            for j in range(i+1,n):
                distance[(i,j)] = self.PRNG([1,100])
        return distance