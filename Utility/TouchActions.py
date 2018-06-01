'''
Created on May 18, 2018

@author: aranjan
'''
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
driver=webdriver.Chrome()
element=driver.find_element_by_class_name("name")
element1=driver.find_element_by_class_name("namem")
touchaction=TouchActions(driver)
#Double taps on a given element.
touchaction.double_tap(element)
#Flicks, starting anywhere on the screen.
touchaction.flick(100, 100)
#Long press on an element.
touchaction.long_press(element1)
#Touch and scroll, moving by xoffset and yoffset.
touchaction.scroll(100, 200)