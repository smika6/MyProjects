# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:43:20 2019

@author: Jacob
"""

from functools import lru_cache


def factors(n):
    factors = []
    for i in range(1,n+1):
        if(n%i==0):
            factors.append(i)
    return factors

@lru_cache(maxsize = None)
def nOfTriangleSeries(n):
    if(n<=1):
        return 1
    return n + nOfTriangleSeries(n-1)
   
def nOfTriangleSeries2(n):  
    for i in range(1,n):
        n+=i
    return n

n = 0
for i in range(10000):#5984
    x = nOfTriangleSeries(i)
    l = len(factors(x))
    if(l>n):
        n = l
        print('Factor Count: ' + str(n), 'Index: ' + str(i), 'Number of Sequence: ', x)
    if(l> 500):
        print('Found!', n, i, x)
        break
else:
    print('nope')
    
print('done')