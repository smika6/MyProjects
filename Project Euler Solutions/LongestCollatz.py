# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:09:51 2019

@author: Jacob
"""
from functools import lru_cache

@lru_cache(maxsize = None)
def collatz(n):
    if(n <= 1):
        return 1
    elif(n%2==0):
        return 1 + collatz(int(n/2))
    else:
        return 1 + collatz(3*n + 1)

biggest, val = 0, 0
for i in range(1,1000000):
    current = collatz(i)
    if(biggest < current):
        biggest, val = current, i
        print("Length:",current,"Started at:",i)
print(val, biggest)