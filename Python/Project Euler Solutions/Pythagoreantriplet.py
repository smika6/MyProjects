# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:11:46 2019

@author: Jacob
"""

def findTripplet():
    for a in range(1,1000):
        for b in range(1,1000):
            for c in range(1,1000):
                if(a+b+c==1000):
                    if(a**2 + b**2 == c**2):
                        return a, b, c
                    
#print(findTripplet())

                
print(200*375*425)