import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCCTB:
    def test_LSBFUK(self):

        driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://www.lsbf.org.uk/")
        driver.maximize_window()
        links = driver.find_elements(By.TAG_NAME, 'a')
        time.sleep(2)
        # Iterate through the list of links and print the href attribute
        count=0
        for link in links:
            urls = link.get_attribute('href')  # Get the 'href' attribute of the <a> tag.

            
        for url in urls:
            driver.execute_script(f"window.open('{url}', '_blank')")
            driver.getCurrentUrl()
            count= count+1

            print(url)
            print(count)
            time.sleep(1)