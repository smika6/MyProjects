# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:54:21 2020

@author: smika
"""

import random



def order_1_cross_over(parent1, parent2):
    
    child = [0,0,0,0,0,0,0,0,0]
    
    # Copy randomly selected set from first parent
    
    random_crossover_start_point = random.randint(0, len(parent1)) #random start index
    
    random_crossover_end_point = random.randint(0, len(parent1))   #random stop index
    
    if random_crossover_start_point > random_crossover_end_point:  #reversing them if start is greater
        random_crossover_start_point, random_crossover_end_point = random_crossover_end_point, random_crossover_start_point #tuple unpacking

    for i in range(random_crossover_start_point, random_crossover_end_point):    
        child[i] = parent1[i]
    
    # Copy rest from second parent in order
    
    unused = [] 
    
    #loop for length of parent2
    for a in range(len(parent2)):
        
        #index is the end point of currently copied chromosome + the next interation
        index = random_crossover_end_point + a
        
        #if index reaches the end of the chromosome make it wrap around
        if index >= len(child):
            index -= len(child)
        
        #check if it is in the child or not and if not save it
        if parent2[index] not in child:
            unused.append(parent2[index])
        
    #the stop minus the start is the length of the range
    size_of_copied_set = random_crossover_end_point - random_crossover_start_point
    
    #the size of the chromosome minus whats already placed
    ammount_of_items_left = len(child) - size_of_copied_set
    
    #loop the ammount of items unplaced
    for b in range(ammount_of_items_left):
        
        #index is the end point of currently copied chromosome + the next interation
        index = random_crossover_end_point + b
        
        #if index reaches the end of the chromosome make it wrap around
        if index >= len(child):
            index -= len(child)
        
        #child at the index unplaced is assigned the next value in the list of unused ones
        child[index] = unused[b]
    
    #return the rebuilt child
    return child

p1 = [1,2,3,4,5,6,7,8,9]
p2 = [9,3,7,8,2,6,5,1,4]

print("parent 1: ", p1)
print("parent 2: ", p2)
print("child:    ", order_1_cross_over(p1,p2) )

