import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
class LSBFSGSmoke:
    def test_HomeLCCA(self):
        # Setup the WebDriver ( for example , using Chrome)
        driver=webdriver.Chrome()
        # Open the desiered web page
        driver.implicitly_wait(5)
        driver.get("https://www.lsbf.edu.sg/")