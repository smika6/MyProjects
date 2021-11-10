# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:26:17 2019

@author: Jacob
"""

val = 2**1000
lst_val = list(str(val))

total = 0
for x in lst_val:
    total += int(x)

print(total)