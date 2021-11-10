# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:39:14 2019

@author: Jacob
"""

names = []
with open('names.txt', 'r') as f:
    fLines = f.readlines()
    fSplit = fLines[0].split(',')
    for x in fSplit:
        name = x.split('"')
        names.append(name[1])

total = 0
names.sort()
print(names[937])

for i, name in enumerate(names):
    #s = ''
    nameValue = 0
    for letter in name:
        #s += str(ord(letter)-64) + " "
        value = ord(letter)-64
        nameValue += value
    #print(i, name, nameValue * i, s)
    total += (nameValue * (i+1))

print(total)