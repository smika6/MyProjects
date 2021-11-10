# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:26:51 2019

@author: Jacob
"""
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def properDivisors(n):
    ls = list(factors(n))
    ls.sort()
    ls.remove(n)
    return ls
    #print( ls )

def abundantNumbersList(n):
    found = 0
    i = 12
    abundants = []
    while found <= n:
        divs = properDivisors(i)
        if divs != None and i < sum(divs):
            #print("Abundant Number {}: {}".format(i, divs))
            abundants.append(i)
            found = found + 1
        i = i + 1
    return abundants

als = abundantNumbersList(7000)
#print(als)
print(factors(12))


def sumOfTwoAbundantNumbers(n):
   for a in als:
        if (a > n):
            return False
        for b in als:
            if (b > n) or (a+b > n):
                return False
            if a + b == n:
                return True


total = 0
for i in range(28123+1):
    if not sumOfTwoAbundantNumbers(i):
        #print(i)
        total = total + i
print("Total: {}".format(total))



   
"""
for i in range(1,50):
    divs = properDivisors(i)
    #print(divs)
    if divs != None and i == sum(divs):
        print("Perfect Number {}: {}".format(i, divs))
    if divs != None and i < sum(divs):
        print("Abundant Number {}: {}".format(i, divs))
    if divs != None and i > sum(divs):
        print("Deficient Number {}: {}".format(i, divs))
    """

