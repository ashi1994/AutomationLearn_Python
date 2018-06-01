'''
Created on May 18, 2018

@author: aranjan
'''
import unittest
class Test1(unittest.TestCase):
    def testAdd(self):
        self.skipTest("skipped due to not valid")
        self.assertEqual(3, 3, "not same")
       
    
if __name__ == '__main__':
    unittest.main()