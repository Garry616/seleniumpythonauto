import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
@pytest.fixture()
def log_on_failure(request,browser_launch):
    yield
    item = request.node
    driver=browser_launch
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)


def setup_function():
    global driver
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.facebook.com/")

def teardown_function():
    driver.quit()

def get_data():
    return[
        ("standar_user","secret_sauce"),
        ("anil","swapnil"),
        ("aniket","swapnil")
    ]
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username,password",get_data())
def test_login(username,password,browser_launch):
    driver=browser_launch
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)
    #assert 1==5
    #allure.attach(driver.get_screenshot_as_png(),name="login",attachment_type=AttachmentType.PNG)
