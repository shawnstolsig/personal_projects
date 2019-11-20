import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
# profile = FirefoxProfile(r"C:\Users\shawn\AppData\Local\Mozilla\Firefox\Profiles\yvtt5opx.selProfile")
# driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary, executable_path=r"C:\Users\shawn\AppData\Local\Programs\Python\Python38-32\geckodriver.exe")

driver = webdriver.Firefox()
driver.get("http://www.google.com")

time.sleep(30)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

url = 'http://clans.worldofwarships.com/clans/gateway/wows/clan-battles/history'

# profile = webdriver.FirefoxProfile(r"C:\Users\shawn\AppData\Local\Mozilla\Firefox\Profiles\yvtt5opx.selProfile")
# web_soup = BeautifulSoup(web_r.text, 'html.parser')

# print(web_soup.findAll('img'))

driver.get(url)


html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, "html.parser")
print(sel_soup)
print(sel_soup.findAll('img'))
