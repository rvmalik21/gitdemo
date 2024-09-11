#   :-- self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
#   :-- We will write the code to alternate the above line here using POM
from selenium.webdriver.common.by import By
from selenium import webdriver
from Scripts.pageObjects.CheckoutPage import CheckoutPage
class HomePage:
    def __init__(self, driver):
        self.driver= driver
    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbutton = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    rad = (By.ID, "inlineRadio2")
    date = (By.NAME,  "bday")
    sub = (By.CLASS_NAME, "btn")
    message =(By.CLASS_NAME, "alert")
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
    def getcheckbutton(self):
        return self.driver.find_element(*HomePage.checkbutton)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def getRadiooption(self):
        return self.driver.find_element(*HomePage.rad)
    def getDate(self):
        return self.driver.find_element(*HomePage.date)
    def getSubmission(self):
        return self.driver.find_element(*HomePage.sub)
    def getMessage(self):
        return self.driver.find_element(*HomePage.message)






