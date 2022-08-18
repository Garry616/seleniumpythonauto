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
    driver.get("https://ijmeet.com/")

def test_host():
    driver.find_element_by_xpath("//a[contains(text(),' Host Meeting ')]").click()
    img=driver.find_element_by_xpath("//div[@class='mx-2 mirror_page-hero__wrapper page-hero mirrorpage-hero--left ']")
    if 'ng-hide'in img.get_attribute('class'):
        print("pass")
    else:
        print("image is visible on screen")




