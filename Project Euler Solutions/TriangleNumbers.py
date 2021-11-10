# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:15:37 2019

@author: Jacob
"""
from functools import reduce

def time(origional_function):
    """This function takes in another function and times how long it took to run"""
    import time
    
    def wrapper(*args, **kargs):
        t1 = time.time()
        result = origional_function(*args, **kargs)
        t2 = time.time() - t1
        print( "{} ran in: {} seconds.".format( origional_function.__name__, round(t2,5) ) )
        return result
    return wrapper

def getTriangleNumber(n):
    return sum(range(1,n+1))

#https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def showTriangleSeries(n):
    s = "[ "
    for i in range(1, n+1):
        s = s + str ( getTriangleNumber(i) )
        if i < n: 
            s = s + ", "
    print(s + " ]")

@time
def valueOfFirstXDivisiors(x):
    n = 0
    while True:
        n = n + 1
        if len(factors(getTriangleNumber(n))) > x:
            return getTriangleNumber(n)
        
print( valueOfFirstXDivisiors(500) )