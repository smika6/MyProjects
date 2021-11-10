# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:42:42 2020

@author: Jacob
"""


def list_to_string(List):
    return "".join(List)




def print_permutations(string):
    print_permute(list(string), 0, len(string)-1)

def print_permute(string, start, stop):
    if start == stop:
        print(list_to_string(string))
    else:
        for i in range(start,stop+1):
            string[start], string[i] = string[i], string[start]
            print_permute(string, start+1, stop)
            string[start], string[i] = string[i], string[start]



    
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


# =============================================================================
# pandigital_numbers = collect_permutations("0123456789")
#  
# print(pandigital_numbers)
#  
# with open('pandigital_numbers0-9.txt', 'w') as file:
#     for number in pandigital_numbers:
#         file.write('%s\n' % number)
# =============================================================================
          
#test = "12345"
#print(test[1:4])
#"""
pandigital_numbers = []
passed = []

with open('pandigital_numbers0-9.txt', 'r') as file:
    for line in file:
        data = line[:-1]
        pandigital_numbers.append(data)

for pandigital in pandigital_numbers:
    #print(pandigital)
    #print(pandigital[1:4])
    if(int(pandigital[1:4])%2==0):
        #print(pandigital[2:5])
        if(int(pandigital[2:5])%3==0):
            #print(pandigital[3:6])
            if(int(pandigital[3:6])%5==0):
                #print(pandigital[4:7])
                if(int(pandigital[4:7])%7==0):
                    #print(pandigital[5:8])
                    if(int(pandigital[5:8])%11==0):
                        #print(pandigital[6:9])
                        if(int(pandigital[6:9])%13==0):
                            #print(pandigital[7:10])
                            if(int(pandigital[7:10])%17==0):
                                passed.append(int(pandigital))
                                #print(pandigital)

print(passed)
print(sum(passed))
                                
#"""