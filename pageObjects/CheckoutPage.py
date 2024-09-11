#   :-- products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

from selenium.webdriver.common.by import By

from Scripts.pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cards = (By.XPATH, "//div[@class='card h-100']")
    footer = (By.CSS_SELECTOR, "a[class*='btn']")
    checkadd =(By.CSS_SELECTOR, "button[class*='btn-success']")
    def getCardsTitle(self):
        return self.driver.find_elements(*CheckoutPage.cards)
        #return self.driver.find_element(*checkoutPage.cards)

    #------self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn']").click()------
    def getfooter(self):
        return self.driver.find_element(*CheckoutPage.footer)

#-----self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()----------
    def getcheckbutton(self):
        self.driver.find_element(*CheckoutPage.checkadd).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

