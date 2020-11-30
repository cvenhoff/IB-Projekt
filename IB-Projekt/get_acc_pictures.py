import wbdriver
import userdata
from selenium.webdriver.support.ui import WebDriverWait

#driver
driver = wbdriver.driver

def get_pics(ppa):
    hrefs = []
    while(len(hrefs) < ppa):
        #return if interrupted
        if(userdata.promo_running_flag == False):
            return
        hrefs = driver.find_elements_by_tag_name('a')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        hrefs = [elem.get_attribute('href') for elem in hrefs]   
        hrefs = [href for href in hrefs if "/p/" in href] 
    hrefs = hrefs[:ppa]
    return hrefs
    