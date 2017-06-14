from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
user = "gautamamber5@gmail.com"

def home():
	driver.get("https://www.onesidedlove.com/")
	elem = driver.find_element_by_name("EMAIL")
	elem.send_keys(user)
	elem = driver.find_element_by_css_selector("#mc4wp-form-1 > div.mc4wp-form-fields > p:nth-child(2) > input[type='submit']")
	elem.click()

home()