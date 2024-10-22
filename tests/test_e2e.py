import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Scripts.pageObjects.ConfirmPage import ConfirmPage
from Scripts.utilities.BaseClass import BaseClass
from Scripts.pageObjects.HomePage import HomePage
from Scripts.pageObjects.CheckoutPage import CheckoutPage
@pytest.mark.skip
# @pytest.mark.usefixtures("setup") ---- We will use this fixture in another package called utilities and BaseClass
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger
        #driver = webdriver.Chrome()
        #driver.implicitly_wait(2)
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
        # CSS slector  a[href*='shop']  XPATH = //a[contains(@href,'shop')]
        homePage = HomePage(self.driver)
        log.info("getting the cards Title here")
        checkoutPage =homePage.shopItems()  # This is optimized code
        # homePage.shopItems().click() ---- earlier it was like that before optimize
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # checkoutPage = CheckoutPage(self.driver)
        products =checkoutPage.getCardsTitle()
        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # Here we will use the Chaining the Web elements
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn']").click()
        checkoutPage.getfooter().click()
        time.sleep(2)
        # self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
        confirmPage =checkoutPage.getcheckbutton()
        # checkoutPage.getcheckbutton().click() earlier it was like that before optimize
        time.sleep(3)
        # self.driver.find_element(By.ID, "country").send_keys("Ind")
        # confirmPage = ConfirmPage(self.driver)
        log.info("Entering country Name here")
        print("Entering country Name here")
        confirmPage.getCountry().send_keys("Ind")
# Here we will remove wait code and make it generalize in our Base class and will call method here only.
        self.verifyPresence("India")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.getIndia().click()
        self.driver.find_element(By.CLASS_NAME, "checkbox-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
        SuccessText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in SuccessText
        #print(SuccessText)
        log.info("Text recieved from the application here" + SuccessText)
