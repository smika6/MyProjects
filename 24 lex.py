# -*- coding: utf-8 -*-
"""
Created on Sun May 12 07:51:51 2019

@author: Jacob
"""

def lexicographic(n):
    pass

def permutation(string):
    permutations('', string)
    
def permutations(pre, string):
    vals = list(string)
    n = len(vals)
    if n == 0:
        print(pre)
    else:
        for i in range(n):
            permutations(pre + string[i], string[0:i] + string[i+1:n])
            
permutation('012')