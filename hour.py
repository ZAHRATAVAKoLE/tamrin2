# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 21:32:57 2022

@author: tavakoli
tamrin 4

"""
number=int(input("enter your number: "))
h=number//3600
m=(number%3600)//60
s=(number%3600)%60
print("the hour is {} ,minutes {} and second {}".format(h,m,s))
