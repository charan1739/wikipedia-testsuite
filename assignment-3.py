from selenium import webdriver
from selenium.webdriver.common.by import By
import time

bridge = webdriver.Chrome()
bridge.get("https://the-internet.herokuapp.com/upload")
bridge.implicitly_wait(10)

upload = bridge.find_element(By.ID, 'file-upload')
upload.send_keys("C:\\Users\\chara\\Downloads\\hall_ticket (1).pdf")

submit = bridge.find_element(By.ID, 'file-submit')
submit.click()

time.sleep(10)
bridge.quit()

