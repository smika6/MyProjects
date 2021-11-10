# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:14:33 2019

@author: Jacob
"""
from decimal import *

# =============================================================================
# #Basic count through
# def countFractions(n):
#     for i in range(2,n+1):
#         s = str(1/i)
#         print(s)        
# countFractions(10)
# =============================================================================


#minor steralization of data and the test for acceptable datatypes, basic removal
#test = str(1/3)
#print(  DecimalSeqModSeq(test,'3')   )
def DecimalSeqModSeq(sec,div):
        sec = str(sec[2:])
        if len(sec) == len(div) and sec.strip(div) == '':
            return -1
        if sec.strip(div) == '':
            return 0
        if sec.strip(div) != '':
            return 1

#check for recurring cycle
def testFractionsForLengthOfRecurringCycleDenom2toN(n):
    #loop through denominators 2 through n
    for i in range(2,n+1):
        #get string of the fraction
        frac = str(1/i)
        
        #make the variable for the recurring cycle
        recur = ''
        
        #get string of the fraction into a list and steralize it for the sequence after the decimal
        fracL = list(frac)
        fracL.remove('.')
        fracL = fracL[1:]
        
        #var for longest found
        maxRecur = 0
        
        #eat the frac and test for length
        for c in fracL:
            recur = str(recur + c)
            print("\nFraction: {} \nTesting For Reccuring Cycle: {}".format(frac,recur))
            print( "Test Results: {}".format(DecimalSeqModSeq(frac,recur))   )
            if DecimalSeqModSeq(frac,recur) == 0:
                if len(recur) > maxRecur:
                    maxRecur = len(recur)
                    print( "Max Recurring Cycle: {}".format(maxRecur)   )
                    break
            print( "Max Recurring Cycle: {}".format(maxRecur)   )

testFractionsForLengthOfRecurringCycleDenom2toN(6)