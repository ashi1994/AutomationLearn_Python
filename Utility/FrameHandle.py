'''
Created on May 18, 2018

@author: aranjan
'''
from selenium import webdriver
driver=webdriver.Chrome()
size=list(driver.find_elements_by_id("name"))
driver.switch_to_frame("name")
driver.switch_to_frame(1)
driver.switch_to_frame("//name[id=23")
driver.switch_to_default_content()