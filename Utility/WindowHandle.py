'''
Created on May 18, 2018

@author: aranjan
'''
from selenium import webdriver
driver=webdriver.Chrome()
firstWindow=driver.window_handles[0]
str1=firstWindow.title
driver.switch_to_window("firstWindow")
secondWindow=driver.window_handles[1]
##switch on to new child window
driver.switch_to_window("secondWindow")
str2=driver.title
print(str2)
print(secondWindow)
#assert that main window and child window title don't match
AssertionError.assertNotEqual(str1,str2)
print('This window has a different title')
#switch back to original window
driver.switch_to.window(firstWindow)
#assert that the title now match
AssertionError.assertEqual(str1,driver.title)
print('Returned to parent window. Title now match')



#https://seleniumwithjavapython.wordpress.com/selenium-with-python/switching-between-windows-and-alerts/