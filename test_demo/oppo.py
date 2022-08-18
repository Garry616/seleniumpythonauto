import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager

def setup_function():
    global driver
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.carwale.com/")
    driver.find_elements_by_xpath("//div[normalize-space()='Hyundai']")
    driver.find_elements_by_xpath("//div[normalize-space()='BMW']")
    driver.find_elements_by_xpath("//div[normalize-space()='Honda']")
    driver.find_elements_by_xpath("//div[normalize-space()='Toyota'")
    driver.find_elements_by_xpath("//*[@id="root"]/div[2]/div/div[2]/div/h1")
 def test_selectCars(self, carBrand,carTitle):
        log.logger.info("******Inside Select Cars Test*********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        print("Car brand is : ",carBrand)
        if carBrand == "BMW":
           home.gotoNewCars().selectBMW()
           title = car.getCarTitle()
           print("Car Title is : "+title)
           assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Hyundai":
           home.gotoNewCars().selectHyundai()
           title = car.getCarTitle()
           print("Car Title is : " + title)
           assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Honda":
           home.gotoNewCars().selectHonda()
           title = car.getCarTitle()
           print("Car Title is : " + title)
           assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Toyota":
           home.gotoNewCars().selectToyota()
           title = car.getCarTitle()
           print("Car Title is : " + title)
           assert title == carTitle, "Not on the correct page as title is not matching"