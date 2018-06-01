'''
Created on May 18, 2018

@author: aranjan
'''
import unittest
class Test(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(3, 4, "not same")

if __name__ == '__main__':
    unittest.main()