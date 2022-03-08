# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 22:29:48 2022

@author: zahra tavakoli
program 1
"""

import random
sum_select=0
computre_number=random.randint(0,10)
while True:
    user_number=int(input("enter your number: "))
    sum_select+=1
    if  user_number==computre_number:
        print("your are win")
        break
    elif user_number< computre_number :
        print("chosse a number bigger than this number")
    elif  user_number> computre_number:
         print("chosse a number smaller than this number")
    
print("count of your chosee :",sum_select)  
print("THE END")  