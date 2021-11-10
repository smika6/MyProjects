# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:49:09 2020

@author: smika
"""

import turtle

width, height = 500, 500

s = turtle.getscreen()

s.setup(width, height)

t = turtle.getturtle()

t.sety(height)

t.speed(5)

def equal_polygon(s,d):
    for _ in range(s):
        t.forward(d)
        a = 360/s
        t.left(a)
        
for n in range(3,100):
    equal_polygon(n,100)

# =============================================================================
# equal_polygon(3,50) # triangle
# equal_polygon(4,50) # square
# equal_polygon(5,50) # pentagon
# equal_polygon(6,50) # hexagon
# equal_polygon(7,50) # heptigon
# equal_polygon(8,50) # octogon
# =============================================================================

turtle.done()