import profiledata
import userdata
import wbdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

#driver
driver = wbdriver.driver
#parameter
delay = 0

def unfollow_func():
    #return if interrupted
    if(userdata.promo_running_flag == False):
        return
    el_list = driver.find_elements_by_tag_name('a')
    try:
        hrefs = [elem.get_attribute('href') for elem in el_list if elem.get_attribute('title') in profiledata.not_followed_back_list]
    except Exception:
        pass
    for href in hrefs:
        driver.get(href)
        unfollow_button = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button'))
        unfollow_button.click()
        sure_button = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]'))
        sure_button.click()
        time.sleep(delay)