import wbdriver
import math
import userdata
from selenium.webdriver.support.ui import WebDriverWait

#driver
driver = wbdriver.driver
#elements
name = '//*[@id="react-root"]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/a'

def search(hashtags, interaction_number, ppa, job_list):
    #get jobs_number
    job_number = 0
    if(job_list[0]):
        job_number = job_number + ppa
    if(job_list[1]):
        job_number = job_number + 1
    #start
    pic_number = math.ceil(math.ceil(interaction_number/len(hashtags))/job_number)
    accounts = []
    for hashtag in hashtags:
        #return if interrupted
        if(userdata.promo_running_flag == False):
            return
        hrefs = []
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        while(len(hrefs) < pic_number):
            #return if interrupted
            if(userdata.promo_running_flag == False):
                return
            hrefs = driver.find_elements_by_tag_name('a')
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            hrefs = [elem.get_attribute('href') for elem in hrefs]   
            hrefs = [href for href in hrefs if "/p/" in href]
        hrefs = hrefs[:pic_number]
        for href in hrefs:
            #return if interrupted
            if(userdata.promo_running_flag == False):
                return
            driver.get(href)
            acc_ref = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element_by_xpath(name))
            accounts.append(acc_ref.get_attribute('href'))
    return accounts