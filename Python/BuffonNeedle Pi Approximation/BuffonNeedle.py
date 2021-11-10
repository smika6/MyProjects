#Jacob Hopkins
#7/18/2017
#approximate pie using buffons needle experiment
#BuffonNeedle
#Assignment 2
from __future__ import division
import random
import math
import turtle
def BuffonNeedle(numNeedles):
    #set up screen
    wn = turtle.Screen()
    drawingT = turtle.Turtle()
    wn.setworldcoordinates(0,0,200,200)
    for l in range(5):
        drawingT.up()
        drawingT.goto(50*l,0)
        drawingT.down()
        drawingT.goto(50*l,200)
    #accumlation variable
    intercept_count = 0

    #loop for drawing lines and checking them
    for i in range(numNeedles):
        x = 200*random.random()
        y = 200*random.random()
        angle = 360*random.random()
        
        drawingT.up()
        drawingT.setx(x)
        drawingT.sety(y)
        drawingT.right(angle)
        drawingT.down()
        for r in range(42):
            if((math.floor(drawingT.xcor())==0) or (math.floor(drawingT.xcor())==50) or (math.floor(drawingT.xcor())==100) or (math.floor(drawingT.xcor())==150) or (math.floor(drawingT.xcor())==200)):
                intercept_count = intercept_count + 1
                drawingT.forward(1)
            else:
                drawingT.forward(1)
    #closing statements and approximation
    if(intercept_count==0) or ((intercept_count/numNeedles)==0):
        print("divide by 0 error")
        pi = 'error'
        print((intercept_count),(numNeedles))
    else:
        pi = (2*42)/(50*(intercept_count/numNeedles))
    wn.exitonclick()
    return pi
                    

#Python v2.7.6
#IDLE v2.7.6
#Windows 10
#No additional libraries
