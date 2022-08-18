import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
def setup_function():
    global driver
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.google.co.in/")
    driver.maximize_window()
def test_agcgd():
    search_box=driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
    print(search_box.is_displayed())