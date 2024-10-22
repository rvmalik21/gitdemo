import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.skip
class TestAppleauth:
    def test_Appleauth(self):
        # Setup the WebDriver ( for example , using Chrome)
        driver=webdriver.Chrome()
        # Open the desired web page
        driver.implicitly_wait(5)
        driver.get("https://common-tracfone-api-brand-sm.cloud.synchronoss.net/")
        # Maximize the opened window
        driver.maximize_window()
        driver.find_element(By.XPATH,"//span[normalize-space()='Sign in with Apple']").click()
        # Entering the credentials of apple account
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,"#account_name_text_field").send_keys("intelegencianoida@gmail.com")
        # click on Arrow to proceed
        driver.find_element(By.XPATH,"//i[@class='shared-icon icon_sign_in']").click()
        # Entering password
        driver.find_element(By.XPATH, "//input[@id='password_text_field']").send_keys("Institute@29")
        # Submit the password
        driver.find_element(By.XPATH, "//i[@class='shared-icon icon_sign_in']").click()
        time.sleep(25)
        # Trusting this browser
        driver.find_element(By.XPATH, "//button[normalize-space()='Trust']").click()
        # Clicking on Continue
        driver.find_element(By.XPATH,"//div[normalize-space()='Continue']").click()
        time.sleep(5)

