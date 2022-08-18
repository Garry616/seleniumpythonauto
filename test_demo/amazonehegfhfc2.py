from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
def setup_function():
    global driver
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_28ors6rnjl_b&adgrpid=60611463244&hvpone=&hvptwo=&hvadid=611311135347&hvpos=&hvnetw=g&hvrand=309431713260516260&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062113&hvtargid=kwd-298319537966&hydadcr=15413_2320038&gclid=Cj0KCQjwuaiXBhCCARIsAKZLt3mGJ9FkBQgORiCRgDeYhnMfmNSn_reeL7EHJmI8xMHadLft1_5-VSkaAp_-EALw_wcB")
    driver.maximize_window()
def test_amazonenen():







