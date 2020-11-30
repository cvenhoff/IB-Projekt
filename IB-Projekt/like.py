import wbdriver
import userdata
from selenium.webdriver.support.ui import WebDriverWait

#elements
like_button_class = "_8-yf5 "
#driver
driver = wbdriver.driver

def lk():
    #return if interrupted
    if(userdata.promo_running_flag == False):
        return
    like_button = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_class_name(like_button_class))
    if(like_button.get_attribute('fill') != "#ed4956"):
        like_button.click()
