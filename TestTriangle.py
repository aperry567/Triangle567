# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""
######################################################################################################################### 
import unittest
from Triangle import Classify_Triangle

class Classify_TriangleTest(unittest.TestCase): 
    def test_suite_init(self):
        """ Test Suite for Triangle init method"""
        T1 = Classify_Triangle(3,7,9)
        self.assertTrue(T1.a == 3)
        self.assertTrue(T1.b == 7)
        self.assertTrue(T1.c == 9)
        
    def test_suite_classifyTriangle(self):
        """ Test Suite for Triangle classifyTriangle method"""
        T2 = Classify_Triangle(3,4,5)
        self.assertFalse(T2.classifyTriangle() == 'Right')
        self.assertTrue(T2.classifyTriangle() != 'Equilateral')   
        self.assertFalse(T2.classifyTriangle() == 'Equilateral')  
        
        T3 = Classify_Triangle(0,-1,-2)
        self.assertTrue(T3.classifyTriangle() != 'InvalidInput')
        self.assertTrue(T3.classifyTriangle() == 'ValidInput')
        
        T4 = Classify_Triangle(1,3,7)
        self.assertTrue(T4.classifyTriangle() != 'Isoceles')
        self.assertTrue(T4.classifyTriangle() != 'InvalidInput')
        
        T5 = Classify_Triangle(2,2,2)
        self.assertTrue(T5.classifyTriangle() != 'Isoceles')
        self.assertTrue(T5.classifyTriangle() == 'ValidInput')
        
        T6 = Classify_Triangle(3,4,5)
        self.assertTrue(T6.classifyTriangle() != 'Scalene')
        self.assertTrue(T6.classifyTriangle() == 'ValidInput')
                
        T7 = Classify_Triangle(3,4,5)
        self.assertTrue(T7.classifyTriangle() != 'Scalene')
        self.assertTrue(T7.classifyTriangle() != 'NotATriangle')       
#########################################################################################################################   
def main():
    '''main() function'''      
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
