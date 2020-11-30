import wbdriver
import userdata
from concurrent.futures import ThreadPoolExecutor
from copy import copy
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request
import os

#profile attributes
follower_number = None
follows_number = None
content_number = None
follower_list = []
follows_list = []
not_followed_back_list = []

#flags
pub_data_collected = False
fol_data_collected = False

#elements
body_tag = "body"
#driver
driver = wbdriver.driver

def collect_pub_data():
    driver.get("https://www.instagram.com/"+userdata.username+"/")
    body = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_tag_name(body_tag))
    body_text = body.text
    body_text = body_text.split("\n")
    global follower_number, follows_number, content_number, pub_data_collected
    follower_number = body_text[3]
    follows_number = body_text[4]
    content_number = body_text[2]
    pub_data_collected = True
    return

def collect_fol_data():
    global follower_number, follows_number, follower_list, follows_list, not_followed_back_list, fol_data_collected
    #get information
    fl_number = (follower_number.split(" "))[0]
    fls_number = (follows_number.split(" "))[0]
    #followers or following
    def get_list(driver, divisor, number):
        #return if interrupted
        if(userdata.promo_running_flag == False):
            return
        driver.get("https://www.instagram.com/"+userdata.username+"/")
        #get button
        href = '//a[@href="/'+userdata.username+'/'+divisor+'/"]'
        button = WebDriverWait(driver, timeout = 30).until(lambda d: d.find_element_by_xpath(href))
        #follower list
        button.click()
        fBody  = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath("//div[@class='isgrP']"))
        el_list = []
        while(len(el_list) < int(number)):
            #return if interrupted
            if(userdata.promo_running_flag == False):
                return
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            el_list = driver.find_elements_by_tag_name('a')
            try:
                el_list = [elem.get_attribute('title') for elem in el_list]
            except Exception:
                pass 
            el_list = [elem for elem in el_list if elem != ""]
        return el_list 
    #driver2
    cookies = driver.get_cookies()
    driver2 = wbdriver.newDriver()
    driver2.get(driver.current_url)
    for cookie in cookies:
        driver2.add_cookie(cookie)
    #threading
    with ThreadPoolExecutor() as pool:
        t1 = pool.submit(get_list, driver, "following", fls_number)
        t2 = pool.submit(get_list, driver2, "followers", fl_number)
        #return if interrupted
        if(userdata.promo_running_flag == False):
            return
        follows_list = t1.result()
        follower_list = t2.result()
    driver2.close()
    #return if interrupted
    if(userdata.promo_running_flag == False):
            return
    not_followed_back_list = [elem for elem in follows_list if not(elem in follower_list)]
    fol_data_collected = True
    return

def get_profilepicture():
    driver.get("https://www.instagram.com/"+userdata.username+"/")
    pp = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/div/button/img'))
    pp = pp.get_attribute('src')
    urllib.request.urlretrieve(pp, os.path.join(os.path.dirname(__file__),"pp.png"))
    return
    