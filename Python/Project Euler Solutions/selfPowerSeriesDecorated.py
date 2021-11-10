# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:15:31 2019

@author: Jacob
"""


def time(origional_function):
    """This function takes in another function and times how long it took to run"""
    import time
    
    def wrapper(*args, **kargs):
        t1 = time.time()
        result = origional_function(*args, **kargs)
        t2 = time.time() - t1
        print('{} ran in: {}'.format(origional_function.__name__, t2))
        return result
    return wrapper

@time
def sumSelfPowerSeries(n):
    """This function will raise values starting at 1 to n to their own respective power and sum them all to be returned"""
    sumVals = 0
    for i in range(1,n+1):
        sumVals += i**i
    return sumVals


print(sumSelfPowerSeries(1000))