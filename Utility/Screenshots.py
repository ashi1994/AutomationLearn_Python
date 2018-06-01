from selenium import webdriver
driver=webdriver.Chrome("C:\\workspace\\msqaautomationjars\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com")
driver.save_screenshot("demo.png")

def setUp(self):    driver=webdriver.Chrome("C:\\workspace\\msqaautomationjars\\chromedriver.exe")
driver.maximize_window()
def tearDown(self): driver.close()