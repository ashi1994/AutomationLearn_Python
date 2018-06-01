'''
Created on May 18, 2018

@author: aranjan
'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
element=driver.find_element_by_class_name("name")
element1=driver.find_element_by_class_name("namem")
actions = ActionChains(driver)
#Double Click
actions.double_click(element)
#Right Click
actions.context_click(element)
# Mouse Hover
actions.move_by_offset(100, 100)
actions.move_to_element(element)
#Drag and drop
actions.drag_and_drop(element, element1)
#Should only be used with modifier keys (Control, Alt and Shift).
actions.key_down(Keys.CONTROL).send_keys("c").perform()
#Should be release the modifier keys
actions.key_up(Keys.CONTROL).send_keys("c").perform()