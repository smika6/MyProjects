# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:23:56 2019

@author: Jacob
"""
from datetime import datetime

named = {
    0:"",
    
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine",
    10:"Ten",
    
    11:"Eleven",
    12:"Twelve",
    13:"Thirteen",
    14:"Fourteen",
    15:"Fifteen",
    16:"Sixteen",
    17:"Seventeen",
    18:"Eighteen",
    19:"Nineteen",
    
    20:"Twenty",
    30:"Thirty",
    40:"Forty",
    50:"Fifty",
    60:"Sixty",
    70:"Seventy",
    80:"Eighty",
    90:"Ninety"
    }

descriptors = {
        3:" Hundred",
        4:" Thousand",
        7:" Million",
        10:" Billion",
        13:" Trillion",
        16:" Quadrillion",
        19:" Quintillion",
        22:" Sextillion",
        25:" Septillion",
        28:" Octillion",
        31:" Nonillion",
        34:" Decillion",
        37:" Undecillion",
        40:" Duodecillion",
        43:" Tredecillion",
        46:" Quattuordecillion",
        49:" Quindecillion",
        52:" Sexdecillion",
        55:" Septemdecillion",
        58:" Octodecillion",
        61:" Novemdecillion",
        64:" Vigintillion",
        67:" Unvigintillion",
        70:" Duovigintillion",
        73:" Trevigintillion",
        76:" Quattuorvigintillion",
        79:" Quinvigintillion",
        82:" Sexvigintillion",
        85:" Septvigintillion",
        88:" Octvigintillion",
        91:" Nonvigintillion",
        94:" Trigintillion",
        97:" Untrigintillion",
        100:" DuoTrigintillion",
        103:" Something"
        }

#O(n)
def getNameOfNumberUnder100(n):
    if(n < 100):
        if(n < 20):#get from memorized list
            return named.get(n, str(n) + " was not Found.");
        elif(n < 100):  # 1 2
            #get size of digit, cut it down to smaller parts, and digest it
            num_str = str(n)
            tens = named.get(int(num_str[:1])*10, str(int(num_str[:1])*10) + " was not Found.")
            ones = named.get(int(num_str[1:]), str(int(num_str[1:])) + " was not Found.")
            return tens + ("-" + ones if ones != "" else "") 
    return str(n) + " was not Found!"

#O(n^2) worst case
def getNameOfNumber(n):
    if(n < 100):
        return getNameOfNumberUnder100(n)
    else:
        #get size of digit
        #cut it down to smaller parts and digest it
        num_str = str(n)
        upper = len(str(n))
        lower = upper%3 
        descriptor = ""
        
        #O(n)
        test = upper
        for key, val in descriptors.items():
            if(int(test) == int(key)):
                descriptor = val
                break
                     
        #O(n^2)
        if descriptor == "":
            notfound = True
            while test > 0 and notfound:
                test = test - 1
                for key, val in descriptors.items():
                    if(int(test) == int(key)):
                        descriptor = val
                        notfound = False                        
                        
        if upper == 3:
            front = named.get(int(num_str[:1]), str(int(num_str[:1])) + " was not Found.")
            tail = getNameOfNumber(int(num_str[1:upper]))
            return front + descriptor + ( (" and " if upper==3 else "") + tail if tail != "" else "")
        elif upper%3>0:
            head = getNameOfNumber(int(num_str[:lower]))
            tail = " " + getNameOfNumber(int(num_str[lower:upper]))
            return head + descriptor + tail 
        else:
            head = getNameOfNumber(int(num_str[:3]))
            tail = " " + getNameOfNumber(int(num_str[3:upper]))
            return head + descriptor + tail 
        
        
def charactersInRange(start, stop):
    total = ""
    for x in range(start,stop+1):
        total = total + getNameOfNumber(x)

    total = total.replace(" ", "")
    total = total.replace("-", "")

    print("Total Characters: " + str(len(total)))
    return len(total)

def showNameRanged(start, stop, mutate=1):
    change = 1
    if(stop < start):
        change = -1
    print("Showing Named Range [" + str(start) + "," + str(stop) + "] by " + str(abs(mutate)*change) +" :")
    x = start
    while x != stop + change:
        print("{}: {} -> {}".format( abs(x - start)+1,  f'{x:,}',  getNameOfNumber(x)) )
        x = x + change * abs(mutate)
    print("Finished Showing Named Range [" + str(start) + "," + str(stop) + "]")
    
def writeNumberDictionary(filename, start=1, stop = 10, mutate = 1, updates = 10):
    updates = round((stop-start)/updates)
    begin = datetime.now()
    elapsed = 0
    with open(filename, 'w') as file:
        change = 1
        if(stop < start):
            change = -1
        x = start
        while x != stop + change:
            if x % updates == 0:
                progress = round(float(float(x)/float(stop))*100.0 , 2)
                check = datetime.now()
                elapsed = elapsed + float(str((check-begin).seconds) + "." + str((check-begin).microseconds))
                estimated = (elapsed/float(x))*(stop-x)
                print("Progress: {}% \nElapsed: {} seconds \nETA: {} seconds\n".format(progress, round(elapsed,2), round(estimated,2) ))
            file.write("{}:{}\n".format( x,  getNameOfNumber(x) ) )
            x = x + change * abs(mutate)
    print("{} had the range [{},{}] written by {}, in {} seconds".format(filename, start, stop, abs(mutate)*change, round(elapsed,2)))
    






print( getNameOfNumber(1561560812321859123168541613) )
