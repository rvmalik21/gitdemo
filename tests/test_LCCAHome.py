import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLCCA:
    def test_HomeLCCA(self):
        # Setup the WebDriver ( for example , using Chrome)
        driver=webdriver.Chrome()
        # Open the desiered web page
        driver.get("https://www.lcca.org.uk/")
        # Maximize the opened window
        driver.maximize_window()
        # specify the image locater for the image
        driver.find_element(By.CSS_SELECTOR,"div[class='social-icons'] div:nth-child(1) a:nth-child(1)").click()
        # Get all window handles
        window_handles= driver.window_handles
        # Switch to the new tab (usually the last one opened)
        driver.switch_to.window(window_handles[1])
        time.sleep(2)
        # Switch back to the first tab
        driver.switch_to.window(window_handles[0])
        time.sleep(5)
        # image_locator= (By.XPATH,"//img[@src='/media/923504/official-logo.gif']")
        # try:
        #     # Use WebDriverWait to wait until the image is present
        #     image_element = WebDriverWait(driver, 10).until(
        #         EC.visibility_of_element_located(image_locator)
        #     )
        #     print("The LCCA image is present on the Website")
        # except:
        #     print(" The LCCA logo image is not present on the site. Please lood into it asap")








