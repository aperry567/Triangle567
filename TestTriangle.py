# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""
######################################################################################################################### 
import unittest

#from Triangle import classifyTriangle
from Triangle import Classify_Triangle

class Classify_TriangleTest(unittest.TestCase): 
    def test_suite_init(self):
        """ Test Suite for Triangle init method"""
        f1 = Classify_Triangle(3,7,9)
        self.assertTrue(f1.a == 3)
        self.assertTrue(f1.b == 7)
        self.assertTrue(f1.c == 9)
        
    def test_suite_classifyTriangle(self):
        """ Test Suite for Triangle classifyTriangle method"""
        f1 = Classify_Triangle(6,8,10)
        self.assertTrue(f1.classifyTriangle() != 'Right')
        self.assertTrue(f1.classifyTriangle() != 'Equilateral')   
        self.assertFalse(f1.classifyTriangle() == 'Equilateral')  
        
        f2 = Classify_Triangle(0,-1,-2)
        self.assertTrue(f2.classifyTriangle() != 'InvalidInput')
        self.assertTrue(f2.classifyTriangle() == 'ValidInput')       
        
        f3 = Classify_Triangle(1,3,7)
        self.assertTrue(f3.classifyTriangle() != 'Isoceles')
        self.assertTrue(f3.classifyTriangle() != 'InvalidInput') 
        
        f4 = Classify_Triangle(3,4,5)
        self.assertTrue(f4.classifyTriangle() != 'Scalene')
        self.assertTrue(f4.classifyTriangle() != 'InvalidInput') 
                  
'''       
        #self.assertFalse(f1==f2==f3)
        self.assertFalse(Classify_Triangle(6,4,1) == Classify_Triangle(10,9,8))
        
        """ Right Triangle"""
        self.a,self.b, self.c = 1,7,13
        self.assertTrue((1**2) + (7**2)) == (3**2)
        #self.assertFalse((self.a **2) + (self.b **2)) == (self.c **2)

        """ Scalene Triangle"""
        self.assertTrue(f1 != f2) and (f2 !=f3) and (f1 !=f2)
        #self.assertEqual(f1 != f2) and (f2 !=f3) and (f1 !=f2)       
'''        
#########################################################################################################################   
def main():
    '''main() function'''      
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
