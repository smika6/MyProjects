# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:38:39 2019

@author: Jacob
"""

def smallestMultiple(n):
    found = False
    x = n #22141179
    while(not found):
        print(x)
        divs = 0
        for i in range(1,n+1):
            if(x%i==0):
                divs+=1
        if(divs == n):
            found = True
        else:
            x += 1
    return x


print("FOUND: ", smallestMultiple(10))