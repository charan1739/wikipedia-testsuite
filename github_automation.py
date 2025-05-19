from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

bridge = webdriver.Chrome()
bridge.get("https://www.github.com/login")

username = bridge.find_element(By.ID, 'login_field')
username.send_keys('charan1739')

password = bridge.find_element(By.ID, 'password')
password.send_keys('charanW3750D')   


button = bridge.find_element(By.NAME, 'commit')
button.click()

time.sleep(10)
bridge.quit()