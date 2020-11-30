from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1500,800")

def newDriver():
    return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

#driver
driver = newDriver()