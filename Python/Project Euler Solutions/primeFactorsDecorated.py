# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:56:47 2019

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


def isPrime(n):
    for i in range(2, n):
        if(n%i==0):
            return False
    return True


def nextPrime(n):
    found = False
    while(not found):
        n = n  + 1
        if(isPrime(n)):
            found = True
    print("Prime Found: {}".format(n))
    return n

@time
def primefactors(n):
    left = n
    factors = []
    d = 2
    while(not isPrime(left) and d < n):
        if(left%d==0):
            left = int(round(left/d))
            factors.append(d)
            print("Factor Found: {}".format(d))
        else:
            d = nextPrime(d)
    factors.append(left)
    return factors
        
        
print(primefactors(600851475143))
            