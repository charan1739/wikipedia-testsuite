from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

bridge = webdriver.Chrome()
bridge.implicitly_wait(20)
bridge.get("https://www.selenium.dev/selenium/web/web-form.html")

inputtext = bridge.find_element(By.CSS_SELECTOR,'#my-text-id')
inputtext.send_keys("automation testing")

password = bridge.find_element(By.NAME,"my-password")
password.send_keys("uthyfkl")

textarea = bridge.find_element(By.NAME,"my-textarea")
textarea.send_keys('Automation testing with selenium in python')

dropdown = Select(bridge.find_element(By.NAME,"my-select"))
dropdown.select_by_visible_text('Two')

datalist = bridge.find_element(By.NAME,"my-datalist")
datalist.send_keys('New York')

file = bridge.find_element(By.NAME,"my-file")
file.send_keys("C:\\Users\\chara\\Downloads\\hall_ticket (1).pdf")

checkbox = bridge.find_element(By.ID,'my-check-2')
checkbox.click()

radio = bridge.find_element(By.ID,'my-radio-2')
radio.click()

datepicker = bridge.find_element(By.NAME,"my-date")
datepicker.click()

months = bridge.find_element(By.CSS_SELECTOR,".datepicker-switch")
months.click()

janmonth = bridge.find_element(By.XPATH,"//span[text() = 'Jan']")
janmonth.click()

date = bridge.find_element(By.XPATH,"//td[text() = '17']")
date.click()



# mobilenumber = bridge.find_element(By.ID,'userNumber')
# mobilenumber.send_keys("1234567890")

# dob = bridge.find_element(By.ID,'dateOfBirthInput')
# dob.click()

# month = Select(bridge.find_element(By.CLASS_NAME,'react-datepicker__month-select'))
# month.select_by_visible_text("April")

# year = Select(bridge.find_element(By.CLASS_NAME,'react-datepicker__year-select')) 
# year.select_by_visible_text("2000")

# date = bridge.find_element(By.CSS_SELECTOR, ".react-datepicker__day.react-datepicker__day--015")
# date.click()

# subject = bridge.find_element(By.ID, "subjectsInput")
# subject.send_keys("Computer Science")
# time.sleep(2)
# # subjects = bridge.find_element(By.XPATH,"//div[text() = 'Computer Science']")# subjects.click()

# hobbies = bridge.find_element(By.XPATH,"//label[text() = 'Music']")
# hobbies.click()

# hobbies1 = bridge.find_element(By.XPATH,"//label[text() = 'Sports']")
# hobbies1.click()

# file = bridge.find_element(By.ID,'uploadPicture')
# file.send_keys("C:\\Users\\chara\\Downloads\\hall_ticket (1).pdf")

# address = bridge.find_element(By.ID,'currentAddress')
# address.send_keys('floor no :- 5 , kapil kaveri hub, nanakramguda')

# options = bridge.find_element(By.XPATH,"//div[text() = 'Uttar Pradesh']")
# options.click()

# city = bridge.find_element(By.XPATH,"//div[text() = 'Agra']")
# city.click()

submitBtn = bridge.find_element(By.XPATH,"//button[@type = 'submit']")
submitBtn.click()



time.sleep(10)
