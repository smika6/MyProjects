# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:38:34 2020

@author: Jacob
"""

def list_to_string(List):
    return "".join(List)

 
def collect_permutations(string):
    collection = []
    collect_permute(list(string), 0, len(string)-1, collection)
    return collection


def collect_permute(string, start, stop, collection):
    if start == stop:
        collection.append(list_to_string(string))
    else:
        for i in range(start,stop+1):
            string[start], string[i] = string[i], string[start]
            collect_permute(string, start+1, stop, collection)
            string[start], string[i] = string[i], string[start]


#https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def test_prime(n):
    #False if 1
    if n <= 1:
        return False
    
    #True if 2 or 3
    if n <= 3:
        return True
    
    #False if it is even or divisible by 3
    #So that the loop of 6k + 1 series checks correctly
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while( i*i <= n):
        if n%i == 0 or n%(i + 2) == 0:
            return False
        i = i + 6
    
    return True

string = "0123456789"
max_pan = -1
while len(string) > 0:
    pandigital_numbers = collect_permutations(string)
    print(pandigital_numbers)
# =============================================================================
#     for pandigital in pandigital_numbers:
#         number = int(pandigital)
#         print(number, test_prime(number))
#         if test_prime(number):
#             if max_pan < number:
#                 max_pan = number
# =============================================================================
    string = string[:-1]

print(max_pan)