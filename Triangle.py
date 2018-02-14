# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""
class Classify_Triangle:  
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def classifyTriangle(self):
        """ Ayana's Triangle Code """
        if self.a >= 0 or self.b >= 0 or self.c >= 0:
            return 'ValidInput'
            
        if self.a <= 200 or self.b <= 200 or self.c <= 200:
            return 'ValidInput' 
        
        if not(isinstance(self.a,int) and isinstance(self.b,int) and isinstance(self.c,int)):
            return 'InvalidInput'
            
        if (self.a + self.b) < (self.c) or (self.a + self.b) < (self.b) or (self.b + self.c) < (self.a):
            return 'NotATriangle'
            
        if (self.a == self.b and self.b == self.c):
            return 'Equilateral'
        elif ((self.a ** 2) + (self.b ** 2)) == (self.c ** 2):
            return 'Right'
        elif (self.a != self.b) and  (self.b != self.c) and (self.a != self.c):
            return 'Scalene'
        else:
            return 'Isoceles'
###########################################################################################################
