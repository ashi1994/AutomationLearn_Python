from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
user = ""
pwd = ""
driver = webdriver.Chrome("C:\\workspace\\msqaautomationjars\\chromedriver.exe")
driver.get("https://www.google.com/gmail/about/")
driver.maximize_window();

#driver.get_screenshot_as_file("ashiwani.png")
#driver.get_screenshot_as_png("ashiwani1")
driver.find_element_by_xpath("//*[text()='Sign In']").click()
time.sleep(10)
#driver.find_element_by_xpath("//input[@name='identifier']").click()
driver.find_element_by_xpath("//input[@name='identifier']").send_keys('ashiwanir323@gmail.com')
time.sleep(20)
driver.find_element_by_xpath("//span[text()='Next']").click()
time.sleep(10)
driver.find_element_by_xpath("//input[@name='password']").click().send_keys('rajputujjain')
time.sleep(10)
driver.find_element_by_xpath("//span[text()='Next']").click()
driver.close()
