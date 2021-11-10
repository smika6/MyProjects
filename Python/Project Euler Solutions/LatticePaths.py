# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:58:17 2019

@author: Jacob
"""
def time(origional_function):
    """This function takes in another function and times how long it took to run"""
    import time
    
    def wrapper(*args, **kargs):
        t1 = time.time()
        result = origional_function(*args, **kargs)
        t2 = time.time() - t1
        print('{} ran in: {}'.format(origional_function.__name__, t2))
        return result
    return wrapper

def veriticiesEven(r):
    return veriticies(r,r)

def veriticies(r,w):
    return ((r+1)*(w+1))

def getGrid(size = 2):
    length = int(round(veriticiesEven(size)**0.5))
    grid = [ [' '] * length for i in range(length) ]
    grid[0][0] = '*'
    return grid

def inPlaceAssignPaths(grid):
    for i in range(0,len(grid)):
        grid[i][len(grid)-1] = grid[len(grid)-1][i] = str(1)
    
    for r in range(len(grid)-2,-1, -1):
        for c in range(len(grid)-2,-1, -1):
            grid[r][c] = str(int(grid[r+1][c]) + int(grid[r][c+1]))

def showGrid(grid):
    for g in grid:
        print(g)
    
    
grid = getGrid(20)
inPlaceAssignPaths(grid)
#showGrid(grid)
print("\n\nTotal Paths: {}".format(grid[0][0]))