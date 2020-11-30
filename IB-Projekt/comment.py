import wbdriver
import random
import time
import userdata
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#elements
comment_sec_class = "Ypffh"
#driver
driver = wbdriver.driver

def com(comments):
    #return if interrupted
    if(userdata.promo_running_flag == False):
        return
    comment = random.choice(comments)
    comment_sec = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_class_name(comment_sec_class))
    comment_sec.click()
    comment_sec = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_class_name(comment_sec_class))
    comment_sec.click()
    comment_sec.send_keys(comment)
    time.sleep(10)
    comment_sec.send_keys(Keys.RETURN)

    