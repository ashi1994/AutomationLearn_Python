'''
Created on May 21, 2018

@author: aranjan
'''
import unittest
from selenium import webdriver
class testcase1(unittest.TestCase):
    driver = webdriver.Chrome("C:\\workspace\\msqaautomationjars\\chromedriver.exe")
    def setUp(self):
        driver.get("http://the-internet.herokuapp.com")
        driver.maximize_window();
    def test_dropdown(self):
  
  
  
  def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()      