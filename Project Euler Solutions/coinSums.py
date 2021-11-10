# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:20:21 2019

@author: Jacob
"""
def compare(origional_functionA, origional_functionB,runs = 50):
    """This function takes in another function and times how long it took to run"""
    import time
    
    def wrapper(*args, **kargs):
        avgA = 0
        avgB = 0
        difference = 0
        for run in range(runs):
            t1A = time.time()
            resultA = origional_functionA(*args, **kargs)
            t2A = time.time() - t1A
            
            t1B = time.time()
            resultB = origional_functionB(*args, **kargs)
            t2B = time.time() - t1B
            
            avgA = avgA + t2A
            avgB = avgB + t2B
            
        avgA = avgA / runs
        avgB = avgB / runs
        difference = (avgB-avgA)/avgB * 100.0
        #print('{} ran in: {} seconds'.format(origional_function.__name__, t2))
        return ( (avgA, avgB, difference) , (resultA, resultB))
    return wrapper


def time(origional_function):
    """This function takes in another function and times how long it took to run"""
    import time
    
    def wrapper(*args, **kargs):
        t1 = time.time()
        result = origional_function(*args, **kargs)
        t2 = time.time() - t1
        #print('{} ran in: {} seconds'.format(origional_function.__name__, t2))
        return (result, t2)
    return wrapper

#O()
@time
def coin_sums_bruteforce(pence_value):
    solutions = 0
    for two_pound in range(pence_value, -1, -200):
         for one_pound in range(two_pound, -1, -100):
             for fifty_pence in range(one_pound, -1, -50):
                 for twenty_pence in range(fifty_pence, -1, -20):
                     for ten_pence in range(twenty_pence, -1, -10):
                         for five_pence in range(ten_pence, -1, -5):
                             for two_pence in range(five_pence, -1, -2):
                                     solutions = solutions + 1
    #print(  "Solutions Generated for {}: {}".format(  pence_value, solutions   ) )
    return solutions

#O(n * coins) so O(n)
@time
def coin_sums_dynamic(pence_value):
    coins = [ 1, 2, 5, 10, 20, 50, 100, 200]
    solutions = [0 for n in range(pence_value+1)]
    solutions[0] = 1
    for coin in coins:
        for j in range(coin, pence_value+1):
            solutions[j] = solutions[j] + solutions[ j - coin ]
    #print(  "Solutions Generated for {}: {}".format(  pence_value, solutions   ) )
    return solutions[len(solutions)-1]


test = 200 #pence
#print(  "Solutions Generated for {}: {}\n".format(  test, coin_sums_bruteforce(test)   ) )
print(  "Solutions Generated for {}: {}\n".format(  test, coin_sums_dynamic(test)   ) )

c = compare(coin_sums_bruteforce(test), coin_sums_dynamic(test))
print(c)

# =============================================================================
# 
# runs = 100
# avgBrute = 0
# avgDynamic = 0
# difference = 0
# for n in range(runs):
#     brute = coin_sums_bruteforce(test)
#     dynamic = coin_sums_dynamic(test)
#     avgBrute = avgBrute + brute[1]
#     avgDynamic = avgDynamic + dynamic[1]
# 
# avgBrute = avgBrute / runs
# avgDynamic = avgDynamic / runs
# difference = (avgDynamic-avgBrute)/avgDynamic * 100.0
# 
# 
# print(avgBrute, avgDynamic, difference)
# =============================================================================
# =============================================================================
# 
# @time
# def coin_sums(pence_value):
#     ways = 0
#     for two_pound in range(0,int(pence_value/2)+1):
#         for one_pound in range(0,round(pence_value-(two_pound*2.0))+1):
#             for fifty_pence in range(0,int(round(pence_value-(one_pound*1.0))/0.5)+1):
#                 for twenty_pence in range(0,int(round(pence_value-(fifty_pence*0.5))/0.2)+1):
#                     for ten_pence in range(0,int(round(pence_value-(twenty_pence*0.2))/0.1)+1):
#                         for five_pence in range(0,int(round(pence_value-(ten_pence*0.1))/0.05)+1):
#                             for two_pence in range(0,int(round(pence_value-(five_pence*0.05))/0.02)+1):
#                                 for one_pence in range(0,int(round(pence_value-(two_pence*0.02))/0.01)+1):
#                                     totala = 2.0*two_pound + 1.0*one_pound + 0.5*fifty_pence
#                                     totalb = 0.2*twenty_pence + 0.1*ten_pence + 0.05*five_pence
#                                     totalc = 0.02*two_pence + 0.01*one_pence
#                                     total = totala + totalb + totalc
#                                     if total == pence_value:
#                                         ways = ways + 1
#                                        # print("{}x£2 + {}×£1 + {}×50p + {}×20p + {}×5p + {}×2p + {}×1p".format(two_pound, one_pound, fifty_pence, twenty_pence, ten_pence, five_pence, two_pence, one_pence))
#     print(ways)    
# =============================================================================
