# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

driver.get("https://www.linkedin.com")
time.sleep(3)

# Finding username and password

search_bar = driver.find_element("xpath", "/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input")
search_bar.send_keys("shinuaccamani@gmail.com")
search_bar.send_keys(Keys.RETURN)
time.sleep(3)
search_bar = driver.find_element("xpath", "/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input")
search_bar.send_keys("shinuaccamani")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# minimize the chat
search_bar = driver.find_element("xpath", "/html/body/div[5]/div[4]/aside/div[1]/header/div[3]/button[2]")
search_bar.click()
time.sleep(5)

# Search for conestoga college
search_bar = driver.find_element("xpath", "/html/body/div[5]/header/div/div/div/div[1]/input")
search_bar.send_keys("conestoga college")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# click me
click_me = driver.find_element("xpath", "/html/body/div[5]/header/div/nav/ul/li[6]/div/button/img")
click_me.click()
time.sleep(3)
# account settings
account_settings = driver.find_element("xpath", "/html/body/div[5]/header/div/nav/ul/li[6]/div/div")
account_settings.click()
time.sleep(3)
# Closing the webdriver
driver.close()

