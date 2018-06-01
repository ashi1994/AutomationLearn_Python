'''
Created on May 18, 2018

@author: aranjan
'''
from selenium import webdriver
driver=webdriver.Chrome()
driver.refresh()
driver.back()
driver.forward()
driver.close()
driver.window_handles()
driver.quit()