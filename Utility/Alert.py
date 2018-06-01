'''
Created on May 18, 2018

@author: aranjan
'''
from selenium import webdriver
driver=webdriver.Chrome()
alert=driver.switch_to_alert()
alert.accept()
alert.dismiss()
alert.send_keys("somethings")
alert.text
#Send the username / password to an Authenticated dialog (like with Basic HTTP Auth). 
driver.switch_to_alert.authenticate('ashiwani','ranjan')