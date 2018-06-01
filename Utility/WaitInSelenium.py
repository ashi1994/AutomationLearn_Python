from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Chrome()
#Implicit wait in selenium
driver.implicitly_wait(5)# In seconds
#Explict wait in selenium
elem1=driver.find_element_by_id("2")
alert=driver.switch_to_alert()
wait1=WebDriverWait(driver,10)
wait1.until(expected_conditions.element_to_be_clickable(elem1))
wait1.until(expected_conditions.alert_is_present(alert),"message")
    