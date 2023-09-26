from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.firefox.service import Service
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


service = Service("C:\Projects\Web_analytics\geckodriver.exe")
driver = webdriver.Firefox(service=service)

driver.get("https://www.ebay.com")

time.sleep(3)

element = driver.find_element(By.ID, "gdpr-banner-decline")
element.click()

element = driver.find_element(By.ID, "gh-btn")
element.click()


#-------------------------- 1st phase login ---------------------------------------------


element = driver.find_element(By.ID, "gh-ug")
element.click()

element = driver.find_element(By.ID, "userid") #id was deletet, i used my personal id
element.send_keys("email")

element = driver.find_element(By.ID, "signin-continue-btn")
element.click()

element = driver.find_element(By.ID, "pass") #as id
element.click()

time.sleep(2)

element.clear()
element.send_keys("password")

element = driver.find_element(By.ID, "sgnBt")
element.click()

driver.close()

# -------------------------- 2nd phase, changing language --------------------------------------------

default_language = driver.find_element(By.ID, "gh-eb-Geo-a-default")
eng_language = driver.find_element(By.CSS_SELECTOR, "#gh-eb-Geo-a-en > span.gh-eb-Geo-txt")


actions = ActionChains(driver)

actions.move_to_element(default_language).perform()

wait = WebDriverWait(driver, 15)
wait.until(EC.text_to_be_present_in_element((By.ID, "gh-eb-Geo-a-en"), "English"))
           
actions.click(eng_language).perform()

#------------------------- 3rd phase, links are set up correctly and lead to relevant pages ----------
