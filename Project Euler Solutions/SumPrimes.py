# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:38:44 2019

@author: Jacob
"""

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

def sumPrimes(n):
    x = 2
    sumP = 0
    for i in range(n+1):
        if(x < n):
            sumP += x
            x = nextPrime(x)
        else:
            break
    return sumP

print("Result:",sumPrimes(2000000))