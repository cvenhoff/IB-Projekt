import wbdriver
import random
import userdata
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#driver
driver = wbdriver.driver

def message_func():
    #return if interrupted
    if(userdata.promo_running_flag == False):
        return
    message = random.choice(userdata.direct_messages)
    message_button = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button'))
    message_button.click()
    try:
        notNow = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]'))
        notNow.click()
    except Exception:
        pass
    text_area = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'))
    text_area.click()
    text_area = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'))
    text_area.click()
    text_area.send_keys(message)
    text_area.send_keys(Keys.RETURN)