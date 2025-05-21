from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

@pytest.fixture
def browser():
    bridge = webdriver.Chrome()
    bridge.implicitly_wait(10)
    bridge.maximize_window()
    bridge.get("https://www.wikipedia.org/")
    yield bridge

@pytest.mark.parametrize("element_xpath, expected_title, content_ele",[
    ("//strong[text()='English']","Cher", "//a[text() = 'Cher']"),
    ("//strong[text() = 'Polski']", "Czy wiesz…", "//div[text() = ' Czy wiesz…']"),
    ("//strong[text() = 'Italiano']", "Benvenuti", "//a[text() = 'Benvenuti']"),
    ("//strong[text() = 'Deutsch']", "Willkommen bei Wikipedia", "//h2[text() = 'Willkommen bei  Wikipedia']"),
    ("//strong[text() = 'Italiano']", "Willkommen bei Wikipedia", "//h2[text() = 'Willkommen bei  Wikipedia']")
])

def test_wikipedia(browser,element_xpath,expected_title,content_ele):
    try:

        element = browser.find_element(By.XPATH,element_xpath)
        element.click()
        
        content = browser.find_element(By.XPATH,content_ele)
        assert content.text == expected_title
        print("successfull")

        time.sleep(10)
    

    except:
         print("failed")

@pytest.mark.selenium
def test_selenium(browser):

    search = browser.find_element(By.ID,"searchInput")
    search.send_keys('selenium' + Keys.ENTER)

    iscorrectresult = browser.find_element(By.ID,'firstHeading')
    assert iscorrectresult.text == 'Selenium'

@pytest.mark.java
def test_java(browser):

    search = browser.find_element(By.ID,"searchInput")
    search.send_keys('java' + Keys.ENTER)

    iscorrectresult = browser.find_element(By.ID,'firstHeading')
    assert iscorrectresult.text == 'Java'
   


@pytest.mark.python
def test_python(browser):

    search = browser.find_element(By.ID,"searchInput")
    search.send_keys('python' + Keys.ENTER)

    iscorrectresult = browser.find_element(By.ID,'firstHeading')
    assert iscorrectresult.text == 'Python'
   

