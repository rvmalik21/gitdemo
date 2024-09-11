#  : -- self.driver.find_element(By.ID, "country").send_keys("Ind") alter this in page object model
from selenium.webdriver.common.by import By
class ConfirmPage:
    def __init__(self, driver):
        self.driver =driver
    country = (By.ID , "country")
    india = (By.LINK_TEXT, "India")
    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)
    #---- self.driver.find_element(By.LINK_TEXT, "India").click()-------
    def getIndia(self):
        return self.driver.find_element(*ConfirmPage.india)


