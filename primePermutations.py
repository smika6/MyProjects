# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 01:11:23 2019

@author: Jacob
"""

perms = []

def isPrime(n):
    for i in range(2, n):
        if(n%i==0):
            return False
    return True

#https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

def toString(List): 
    return ''.join(List)

def permute(a, l, r):
    if l==r: 
        #print(toString(a))
        perms.append(toString(a))
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]

def permutations(s):
    perms.clear()
    a = list(s)
    l = len(s)
    permute(a, 0, l-1)
    return perms

def strip(ns):
    stripped = []
    for n in ns:
        if n in ns:
            stripped.append(n)
    return stripped

def find_prime_permutation(n):
    allN = permutations(str(n))
    allN = strip(allN)
    
    for i, aN in enumerate(allN):
        if isPrime(int(aN)):
            print(i, aN)

find_prime_permutation(1487)
    