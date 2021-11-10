# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:32:36 2019

@author: Jacob
"""
from functools import lru_cache

@lru_cache(maxsize = None)
def fact(n):
    if(n<=1):
        return 1
    return n * fact(n-1)

number = fact(100)

lst_number = list(str(number))
total = 0
for x in lst_number:
    total += int(x)
print(total)