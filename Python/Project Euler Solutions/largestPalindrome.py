# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:54:26 2019

@author: Jacob
"""

def timedLogger(origional_function):
    """This function takes in another function and times how long it took to run"""
    import time
    import logging
    logging.basicConfig(filename = '{}.log'.format(origional_function.__name__), level= logging.INFO)
    
    def wrapper(*args, **kargs):
        logging.info('Ran with args: {}, and kargs: {}'.format(args,kargs))
        t1 = time.time()
        result = origional_function(*args, **kargs)
        t2 = time.time() - t1
        print('{} ran in: {}'.format(origional_function.__name__, t2))
        return result
    return wrapper


def palindrome(n):
    strN = str(n)
    lstN = list(strN)
    start = 0
    stop = len(lstN)-1
    while(start <= stop):
        if(lstN[start] != lstN[stop]):
            return False
        start+=1
        stop-=1
    return True;

@timedLogger
def productPalindromesUnder(n):
    palindromes = []
    start = "9"
    for i in range(1, n-1):
        start = start + "9"
    stop = start + "9"
    start = int(start) + 1
    stop = int(stop)
    for a in range(start, stop+1):
        for b in range(start,stop+1):
            ab = a * b
            #print(a, b, ab)
            if(palindrome(ab)):
                palindromes.append(ab)
    return palindromes
        

print(max(productPalindromesUnder(3)))