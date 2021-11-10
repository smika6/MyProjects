# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:44:49 2019

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
    return n

def nInPrimeSeries(n):
    prime = 1
    for i in range(n):
        prime = nextPrime(prime)
        print(i)
    return prime

n=10001
print('{}th Prime Value: {}'.format(n, nInPrimeSeries(n)))