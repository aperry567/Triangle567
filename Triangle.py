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
            
        if (self.a + self.b) =< (self.c) or (self.a + self.b) < (self.b) or (self.b + self.c) < (self.a):
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
    # require that the input values be >= 0 and <= 200
'''    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= b or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
'''