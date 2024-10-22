import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#------------------This is just for practixe---------------------
# driver=webdriver.Chrome()
# driver.get("https://www.flemingcollegetoronto.ca/")
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
# time.sleep(5)
@pytest.mark.skip
class TestLCCA:
    def test_HomeLFCT(self):
        # Setup the WebDriver ( for example , using Chrome)
        driver=webdriver.Chrome()
        # Open the desiered web page
        driver.implicitly_wait(5)
        driver.get("https://www.flemingcollegetoronto.ca/")
        # Maximize the opened window
        driver.maximize_window()
        print(driver.title)
        print(driver.current_url)
        time.sleep(4)
