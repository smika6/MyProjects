# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:13:50 2019

@author: smika
"""

#O(n^2)
def numOfRightTrianglesForPerimeter(p):
    solutions = []
    
    for a in range(1,p):
        for b in range(1,p):
            c = round(a**2 + b**2)**0.5 #gimme a c that works
            if a+b+c == p : #kinda sloppy imo, but works
                test = [a,b,int(c)] #fix it when needed
                test.sort()
                if test not in solutions:
                    solutions.append([a,b,c])
                    #print(test)
    return len(solutions)

#O(n^2)
def testMaxSolutionsInRange(s=1,r):
    maxSolutions = 0
    value = 0
    
    for p in range(s,r+1):
        test = numOfRightTrianglesForPerimeter(p)
        if test > 0:
            print("p: {} \t# Of Solutions: {}".format(p, test))
        if test > maxSolutions:
            maxSolutions = test
            value = p
    print(    "Value: {} \n# Of Solutions:{} \n".format(value, maxSolutions)   )
    return [value, maxSolutions]

answer = testMaxSolutionsInRange(1000)





















# =============================================================================
# 
# # O(n^3)
# def numOfRightTrianglesForPerimeterLegacy(p):
#     solutions = []
#     
#     for a in range(1,p):
#         for b in range(1,p):
#             for c in range(1,p):
#                 if a+b+c == p:
#                     if a**2 + b**2 == c**2 :
#                             test = [a,b,c]
#                             test.sort()
#                             if test not in solutions:
#                                 solutions.append([a,b,c])
#                                 #print(test)
#     return len(solutions)
# =============================================================================
