# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 22:52:16 2022

@author: tavakoli
ptogram 2
"""
import math
while True:
    op=(input("enter your opration: "))
    if op=="exit":
        
        break
    elif op == "sin" or op=="log" or op=="cot" or op==" tan" or op=="!":
        a=int(input("enter number 1: "))
        
    else:
        
        a=int(input("enter number 1: "))
        b=int(input("enter number 2: "))
    if op== "+":
        result=a+b
        print(result)
    elif op=="-":
        result=a-b
        print(result)
    elif op=="*":
        result=a*b
        print(result)
        
    elif op=="/":
        if b!=0:
            result=a/b
            print(result)
        else:
            print("Cannot dived by zero")
    elif op=="^":
        result=a**b
        print(result)
    elif op=="sin":
        result=math.sin(a)
        print(" the sin value of coplex number is :", result)
    elif op=="log":
        result=math.log(a)
        print( " the log value of coplex number is :",result)
    elif op=="tan":
        result=math.tan(a)
        print( " the tan value of coplex number is :",result) 
    elif op=="cot":
        result=math.cot(a)
        print( " the cot value of coplex number is :",result)
    elif op=="!":
        result=math.factorial(a)
       
        print(result)    
       
        
        
        
        

