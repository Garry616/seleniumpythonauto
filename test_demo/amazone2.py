import pytest
import allure
from allure_commons.types import AttachmentType
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
def setup_function():
    global driver
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_28ors6rnjl_b&adgrpid=60611463244&hvpone=&hvptwo=&hvadid=611311135347&hvpos=&hvnetw=g&hvrand=309431713260516260&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062113&hvtargid=kwd-298319537966&hydadcr=15413_2320038&gclid=Cj0KCQjwuaiXBhCCARIsAKZLt3mGJ9FkBQgORiCRgDeYhnMfmNSn_reeL7EHJmI8xMHadLft1_5-VSkaAp_-EALw_wcB")
    driver.maximize_window()
def test_amazonenen():
    driver.find_element_by_id("twotabsearchtextbox").send_keys("laptop")
    driver.find_element_by_id("nav-search-submit-button").click()
    time.sleep(30)
    gaurav1=driver.find_element_by_xpath("//div[@class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1']//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']")
    print(gaurav1.text)
    driver.find_element_by_xpath("//img[@alt='Sponsored Ad - HP 14s, 11th Gen Intel Core i3, 8GB RAM/512GB SSD 14inch(36.6 cm) FHD,Micro-Edge, IPS Display/Alexa Built-i...']").click()
    driver.switch_to_window(driver.window_handles[1])
    driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
    time.sleep(15)
    driver.find_element_by_xpath("//input[@aria-labelledby='attach-sidesheet-view-cart-button-announce']").click()
    gaurav=driver.find_element_by_xpath("//span[@class='a-truncate-cut']")
    print(gaurav.text)
    assert gaurav1.text=="11th Gen Intel Core i3"




#//input[@aria-labelledby='attach-sidesheet-view-cart-button-announce']