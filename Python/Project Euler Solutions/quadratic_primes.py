# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:46:08 2019

@author: Jacob
"""
#https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def test_prime(n):
    #False if 1
    if n <= 1:
        return False
    
    #True if 2 or 3
    if n <= 3:
        return True
    
    #False if it is even or divisible by 3
    #So that the loop of 6k + 1 series checks correctly
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while( i*i <= n):
        if n%i == 0 or n%(i + 2) == 0:
            return False
        i = i + 6
    
    return True
    
    

def euler_quadratic(n, a, b):
    return n*n + a * n + b

def range_of_euler_quadratic(a, b):
    radius = 0
    test = 0
    
    while test_prime(   euler_quadratic(test, a, b) ):
            radius = radius + 1
            test = test + 1
    return radius-2

def longest_quadratic(target):
    maxA = -1
    maxB = -1
    maxRange = -1
    for a in range(0, target):
        for b in range(0, target+1):
            testa = range_of_euler_quadratic(a,b)
            testb = range_of_euler_quadratic(-a,b)
            testc = range_of_euler_quadratic(a,-b)
            testd = range_of_euler_quadratic(-a,-b)
            
            test_max = max(testa,testb,testc,testd)
            
            if test_max == testb:
                a = -a
            if test_max == testc:
                b = -b
            if test_max == testd:
                a,b = -a,-b
            
            if test_max > maxRange:
                maxRange = test_max
                maxA = a
                maxB = b
                print((maxA,maxB, (0,maxRange)))
    return (maxA,maxB, (0,maxRange))
    

print( "Conclusion:", longest_quadratic(1000) )