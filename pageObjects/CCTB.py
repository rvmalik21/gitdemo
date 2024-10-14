
from selenium.webdriver.common.by import By
class CCTB:
    def __init__(self, driver):
        self.driver= driver

    about_us=(By.XPATH,"//a[@class='nav-link font-bold-18'][normalize-space()='About Us']")
    def getaboutus(self):
        return self.driver.fing_element(*CCTB.about_us)






