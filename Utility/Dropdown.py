'''
Created on May 18, 2018

@author: aranjan
''' 
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver=webdriver.Chrome()
element=driver.find_element_by_id("ids")
select=Select(element)
select.select_by_index(0)
select.select_by_value(1)
select.select_by_visible_text("options")
siz=select.__sizeof__()
print(siz)
