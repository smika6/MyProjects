# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:22:01 2019

@author: smika
"""
sundays = 0
dayOfWeek = 2
mLen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for y in range(1901, 2000+1):
    for m in range(1,12+1):
        lengthOfMonth = mLen[m-1]
        if m == 2 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            lengthOfMonth = lengthOfMonth + 1
        for d in range(1,lengthOfMonth):
            #print( "{}/{}/{}: {}".format(m, d, y, dayOfWeek ) )
            if d == 1 and dayOfWeek == 1:
                sundays = sundays + 1
                #print( "{}/{}/{}: {}".format(m, d, y, dayOfWeek ) )
            if dayOfWeek == 7:
                dayOfWeek = 1
            else:
                dayOfWeek = dayOfWeek + 1


print(sundays)









# =============================================================================
# 
# day = 1
# month = 1
# year = 1901
# weekday = 2
# monthLength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# sundays = 0
# while year <= 2000:
#     print( "{}/{}/{}: {}".format(month, day, year, ("Sunday" if weekday == 1 else "") ) )
#     if weekday == 1 and day == 1:
#         #print( "{}/{}/{}: {}".format(month, day, year, ("Sunday" if weekday == 1 else "") ) )   
#         sundays = sundays + 1
#     
#     lengthOfMonth = monthLength[month-1]
#     
#     if month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             lengthOfMonth = lengthOfMonth + 1
#         
#     if day == lengthOfMonth and month < 12:
#         day = 0
#         month = month + 1
#         
#     if month == 12 and day == lengthOfMonth:
#         year = year + 1
#         month = 1
#         day = 0
#     
#     if weekday == 7:
#         weekday = 0
#         
#     day = day + 1
#     
#     weekday = weekday + 1
#     
# print(sundays)
# =============================================================================
