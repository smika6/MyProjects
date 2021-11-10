# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:54:14 2019

@author: Jacob
"""

def sumPrimesUnderN(n):
    total = 0
    i = 0
    with open('primes1.txt', 'r') as f:
        wait = 2
        fLines = f.readlines()
        sumP = 0
        for x in fLines:
            if wait <= 0:
                line = []
                #print(x.split(' '))
                for l in x.split(' '):
                    if(l != ''and l != '\r' and l != '\n' and int(l) < n):
                        i+=1
                        line.append(int(l))
                        #print(i,l)
                sumP += sum(line)
            else:
                wait -= 1
        #print(sumP)
        total += sumP
        
    with open('primes2.txt', 'r') as f:
        wait = 2
        fLines = f.readlines()
        sumP = 0
        for x in fLines:
            if wait <= 0:
                line = []
                #print(x.split(' '))
                for l in x.split(' '):
                    if(l != ''and l != '\r' and l != '\n' and int(l) < n):
                        i+=1
                        line.append(int(l))
                        #print(i,l)
                sumP += sum(line)
            else:
                wait -= 1
        #print(sumP)
        total += sumP
        
    print('Final Total:', total)
    return total

sumPrimesUnderN(2000000)
    #for line in fLines:
        #print(line)

#with open('primes1.txt', 'r') as f:
#    wait = 2
#    fLines = f.readlines()
#    sumP = 0
#    for x in fLines:
#        if wait <= 0:
#            line = []
#            for l in x:
#                if(l != ' 'and l != '\r' and l != '\n'):
#                    line.append(int(l))
#                    print(l)
#            sumP += sum(line)
#        else:
#            wait -= 1
#    print(sumP)
#    #for line in fLines:
#        #print(line)
    