'''
Created on May 18, 2018

@author: aranjan
'''
import unittest
import HTMLTestRunner
import logging
from Basic import PyUNIT
from Basic.PyUNIT2 import Test1
from Basic.PyUNIT import Test
from Basic.TruchTest import TruthTest
suite=unittest.TestSuite()
def ownsuite():
    suite.addTests(Test)
    suite.addTests(Test1)
    suite.addTests(TruthTest)
    return suite
if __name__ == '__main__':
    runner=unittest.TextTestRunner()
#     suite1=ownsuite()
    runner.run(ownsuite())

# class Suite(unittest.TestCase):
#     def test_main(self):
#         logging.info('Inside test suite')
#         self.suite = unittest.Testuite([unittest.defaultTestLoader.loadTestsFromTestCase(Test),
#                                          unittest.defaultTestLoader.loadTestsFromTestCase(Test1),
#                                          unittest.defaultTestLoader.loadTestsFromTestCase(TruthTest)])
#         if __name__ == '__main__':
#             outputfile = open("c\TestReport.html", "w")
#         runner = HTMLTestRunner.HTMLTestRunner(stream=outputfile, verbosity=2,title='Execution Report',description='Suite Run')
#         runner.run(self.suite)
