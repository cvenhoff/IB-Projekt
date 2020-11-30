import wbdriver
import userdata
from selenium.webdriver.support.ui import WebDriverWait

#elements
body_tag = "body"
#driver 
driver = wbdriver.driver

def fol():
    #return if interrupted
    if(userdata.promo_running_flag == False):
        return
    body = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_tag_name(body_tag))
    body_text = body.text
    body_text = body_text.split("\n")
    follow_button = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath('//*[contains(text(), "'+body_text[1]+'")]'))
    follow_button.click()
