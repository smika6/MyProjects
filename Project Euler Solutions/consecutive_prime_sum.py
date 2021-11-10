# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:38:38 2019

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


primes = []

for n in range(1,1000):
    if test_prime(n):
        primes.append(n)

print(primes)
