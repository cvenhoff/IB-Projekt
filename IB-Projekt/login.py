import wbdriver 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

#elements
username_id = "//input[@name='username']"
password_id = "//input[@name='password']"
#driver
driver = wbdriver.driver

def login_func(username, password):
    driver.get("https://www.instagram.com/")
    #get username entry field
    username_entry = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath(username_id))
    username_entry.clear()
    username_entry.send_keys(username)
    #get password entry field
    password_entry = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath(password_id))
    password_entry.clear()
    password_entry.send_keys(password)
    #log in
    password_entry.send_keys(Keys.RETURN)
    #check if worked
    try: 
        WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements_by_id("slfErrorAlert"))
        return False
    except Exception:
        return True
