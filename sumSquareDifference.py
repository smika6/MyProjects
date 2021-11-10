# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:35:39 2019

@author: Jacob
"""

def sumOfSquaredSeries(n):
    """This function will raise values starting at 1 to n to their own respective power and sum them all to be returned"""
    sumVals = 0
    for i in range(1,n+1):
        sumVals += i**2
    return sumVals

def sumSquaredSeries(n):
    sumVals = 0
    for i in range(1,n+1):
        sumVals += i
    return sumVals**2

def diffOfSquaredAndSumSquared(n):
    return sumSquaredSeries(n) - sumOfSquaredSeries(n)

print(diffOfSquaredAndSumSquared(100))