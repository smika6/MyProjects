# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:25:44 2019

@author: Jacob
"""


def concatenated_product(value, products):
    concatenated_product = ''
    for product in products:
        new_product = value * product
        concatenated_product = concatenated_product + str(new_product)
    return concatenated_product

def test_pandigital(possible_pandigital):
    if not len(possible_pandigital) == 9:
        return False
    
    pandigital = '123456789'
    for needed_value in pandigital:
        if needed_value not in possible_pandigital:
            return False
    
    return True

# =============================================================================
# print(   concatenated_product(192,[1,2,3])   )
# print(  test_pandigital(    concatenated_product(192,[1,2,3])   )  )
# 
# print(   concatenated_product(9,[1,2,3,4,5])   )
# print(  test_pandigital(    concatenated_product(9,[1,2,3,4,5])   )  )
# 
# print(   concatenated_product(17,[1,2,3])   )
# print(  test_pandigital(    concatenated_product(17,[1,2,3])   )  )
# =============================================================================

tested = 0
max_pandigital = 0
for n in range(1,9877):
    test_products = [1,2]
    new_term = 2
    
# =============================================================================
        #used to find the official end condition
#     if(int(concatenated_product(n,[1,2])) > 987_654_321):
#         print('max n:' + str(n))
#         break
# =============================================================================
    
    while(987_654_321 >= int(concatenated_product(n,test_products))):
        tested = tested + 1
        #print('testing: ', n, ' *+ ', test_products, '->', concatenated_product(n,test_products), '?', test_pandigital( concatenated_product(n,test_products))  )
        if int(concatenated_product(n,test_products)) > max_pandigital:
            max_pandigital = int(concatenated_product(n,test_products))
        new_term = new_term + 1
        test_products.append(new_term)

print('max found: ', max_pandigital)
print('found in ' + str(tested) + ' tested values')
        

        
