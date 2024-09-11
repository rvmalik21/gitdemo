#from selenium.webdriver.chrome import webdriver
import logging

import pytest
from selenium.webdriver.chromium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Scripts.TestData.HomePageData import HomePageData
from Scripts.pageObjects.HomePage import HomePage
from Scripts.utilities.BaseClass import BaseClass
@pytest.mark.usefixtures("getterData")
class TestHomepage(BaseClass):
    def test_formSubmission(self,getterData):
        log = self.getLogger
        homepage = HomePage(self.driver)
        #homepage.getName().send_keys("Ravi")
        log.info("FirsName will be here" + getterData["firstname"])
        homepage.getName().send_keys(getterData["firstname"])
        #homepage.getEmail().send_keys("ravtest91@gmail.com")
        homepage.getEmail().send_keys(getterData["secondname"])
        homepage.getPassword().send_keys("Test@12345")
        homepage.getcheckbutton().click()
        #self.selectOptionbyText(homepage.getGender(), "Male")
        self.selectOptionbyText(homepage.getGender(), getterData["gender"])
        homepage.getRadiooption().click()
        homepage.getDate().send_keys(getterData["dob"])
        homepage.getSubmission().click()
        altmessage = homepage.getMessage().text
        assert ("Success!" in altmessage)
        self.driver.refresh()
# Privide the set of date to Iterate it on the same Test Case again and again
# @pytest.fixture(params=[("Ravi ","Malik","Male"), ("Pooja ","Malik","FeMale")])
# # Privide the set of date to Iterate it on the same Test Case again and again
# def getData(request):
#     return request.param

# Here We are use params in Tuple
#@pytest.fixture(params=[("Ravi ","Malik","Male","14/11/2222"), ("Pooja ","Malik","Female","31/12/3333"),("Sumit","Sharma","Male","25/05/1111")])
# Here we passing params in dictionary format
@pytest.fixture(params=HomePageData.getTestData("testcase"))
def getterData(request):
    return request.param
# This is our actual Test Case
# driver = webdriver.Chrome()  These first three lines will go to conftest.py
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.maximize_window()
#driver.find_element(By.NAME, 'name').send_keys("Ravi")
# driver.find_element(By.NAME, 'email').send_keys("test.qa@yopmail.com")
# driver.find_element(By.ID, 'exampleInputPassword1').send_keys("Test@12345")
#driver.find_element(By.ID, "exampleCheck1").click()
# dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Male")
#driver.find_element(By.ID, "inlineRadio2").click()
#driver.find_element(By.CLASS_NAME, "form-control").send_keys("11/14/1992")
#driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
#element.submit()
# driver.find_element(By.CLASS_NAME, "alert).text





