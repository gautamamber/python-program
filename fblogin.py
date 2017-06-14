from selenium import webdriver
from selenium.webdriver.common.keys import Keys
username = raw_input('enter username')
password = raw_input('enter password')
driver = webdriver.Chrome()
def home():
	driver.get("https://www.facebook.com/")
def login():
	elem = driver.find_element_by_id("email")
	elem.send_keys(username)
	elem = driver.find_element_by_id("pass")
	elem.send_keys(password)
def click_b():
	elem = driver.find_element_by_id("loginbutton")
	elem.click()
def search():
	elem = driver.find_element_by_name("q")
	elem.send_keys("tushargupta")
home()
login()
click_b() 
search()
