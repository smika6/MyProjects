# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:52:14 2019

@author: Jacob
"""

def show(matrix):
    for array in matrix:
        print(array)
    print()
    
def test(range):
    for test in range(1,range+1):
        s = spiral(test)
        
        if s != None:
            show(s)

def spiral(size):
    
    #size validation
    if size < 1 or size%2 == 0:
        return
    
    #generate my empty 2d array
    spiral = [[0 for n in range(1,size+1)] for n in range(1,size+1)]
    
    # find the venter
    x = int(round((size-1)/2))
    y = int(round((size-1)/2))
    
    #start the value counter, later i would like to turn this into an iterator counter class
    value = 1
    
    #assugn the center
    spiral[y][x] = value
    
    #get to the next value to place
    value = value + 1
    
    #to know when were due for a turn and to update to ensure circling ourselves
    til_turn = 0
    
    #keep track of cardinal directions for clean and easy code reading
    direction = 'e'
    
    #since value increases everytime we place it on the spiral, 
    #we know were done when they value is the square of the size since that will be the biggest value at top right
    while value <= size*size:
    
        #this is east movement
        if direction == 'e':
            #check if were on the final bend and dont need to increase til_turn since were not wrapping anymore
            if value-1 != spiral[0][0]:
                til_turn = til_turn + 1
            
            #get a current version of til_turn
            temp = til_turn
            
            #ensure were sill not due for a turn
            while temp > 0:
                #east increases the x
                x = x + 1

                #place the value on the map
                spiral[y][x] = value
                
                #increase value and decrease to get us closer to turning
                value = value + 1
                temp = temp - 1
            #ready for a turn so declare the next direction. using this we could reverse it too xD so
            direction = 's'
        
        if value == spiral[0][size-1] + 1:
            break
                
            
        if direction == 's':
            temp = til_turn
            while temp > 0:
                y = y + 1
                spiral[y][x] = value
                value = value + 1
                temp = temp - 1
            direction = 'w'
         
        if direction == 'w':
            til_turn = til_turn + 1
            temp = til_turn
            while temp > 0:
                x = x - 1
                spiral[y][x] = value
                value = value + 1
                temp = temp - 1
            direction = 'n'
        
        if direction == 'n':
            temp = til_turn
            while temp > 0:
                y = y - 1
                spiral[y][x] = value
                value = value + 1
                temp = temp - 1
            direction = 'e'
    
    return spiral

def sumDiagonals(spiral):
    size = len(spiral)
    total = -1 #accounts for center being added twice, since its always 1 anyways
    for a in range(0,size):
        total = total + spiral[a][a]
    
    for b in range(size-1, -1, -1):
        total = total + spiral[size-1-b][b]
        
    return total

#print(   sumDiagonals(spiral(1001))   )
show(spiral(501))

# =============================================================================
# ring = 1
# remain = size - ring
# taken = 1
# 
# direction = 'e'
# 
# while 0 < remain:
#     
#     if direction == 'e':
#         while taken < ring:
#             print('e')
#             x = x + taken
#             spiral[y][x] = value
#             value = value + 1
#             taken = taken + 1
#         direction = 's'
#         taken = 1
#     
#     if direction == 's':
#         while taken < ring: 
#             print('s')
#             y = y + taken
#             spiral[y][x] = value
#             value = value + 1
#             taken = taken + 1
#         direction = 'w'
#         taken = 1
#     
# 
#     if direction == 'w':
#         while taken < ring: 
#             print('w')
#             x = x - taken
#             spiral[y][x] = value
#             value = value + 1
#             taken = taken + 1
#         direction = 'n'
#         taken = 1
#         
#     if direction == 'n':
#         while taken < ring:
#             print('n')
#             y = y - taken
#             spiral[y][x] = value
#             value = value + 1
#             taken = taken + 1
#         direction = 'e'
#         taken = 1
#     
#     ring = ring + 1
#     remain = size - ring
# =============================================================================