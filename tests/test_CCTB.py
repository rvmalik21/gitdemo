#  This is the script of finding all the links and open them in new tab



import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from Scripts.pageObjects.CCTB import CCTB


class TestCCTB:


    def test_CCBTHome(self):

        driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://www.canadianctb.ca/")
        driver.maximize_window()
        convocation_link=driver.find_element(By.XPATH, "(//a[text()='Convocation'])[2]")
        convocation_url=convocation_link.get_attribute('href')
        window_handles = driver.window_handles
        driver.execute_script(f"window.open('{convocation_url}', '_blank')")
        print(f"this is the url {convocation_url}")
        about_us_link = driver.find_element(By.XPATH,
                                            "//a[@class='nav-link font-bold-18'][normalize-space()='About Us']")
        about_us_url = about_us_link.get_attribute('href')
        driver.execute_script(f"window.open('{about_us_url}', '_blank')")
        print(f"this is the url {about_us_url}")
        program_link = driver.find_element(By.XPATH,
                                           "//a[@class='nav-link font-bold-18'][normalize-space()='Programs']")
        program_url = program_link.get_attribute("href")
        driver.execute_script(f"window.open('{program_url}','_blank')")
        print(f"this is the url {program_url}")
        admission_link=driver.find_element(By.XPATH, "//a[@class='nav-link font-bold-18'][normalize-space()='Admissions']")
        admission_url=admission_link.get_attribute("href")
        driver.execute_script(f"window.open('{admission_url}','_blank')")
        print(f"this is the url {admission_url}")
        accommodation_link=driver.find_element(By.XPATH, "(//a[text()='Accommodation'])[3]")
        accommodation_url=accommodation_link.get_attribute("href")
        driver.execute_script(f"window.open('{accommodation_url}')")
        print(f"this is the url {accommodation_url}")

        all_window_handles = driver.window_handles
        print(f"this is the url {all_window_handles}")
        # time.sleep(3)
        # Switch to the new tab (usually the last one opened)
        # driver.switch_to.window(all_window_handles[-1])
        # driver.execute_script(f"window.location.href = '{convocation_url}'")
        # time.sleep(2)
        # driver.switch_to.window((all_window_handles[0]))
        # time.sleep(2)
        # driver.find_element(By.XPATH,"//a[@class='nav-link font-bold-18'][normalize-space()='About Us']")
        # driver.switch_to.window(all_window_handles[-1])
        # time.sleep(2)
        #
        #
        #
        # driver.switch_to.window(all_window_handles[-1])
        # driver.execute_script(f"window.location.href = '{convocation_url}'")
        # time.sleep(3)
        #
        # driver.switch_to.window((all_window_handles[0]))
        #
        #
        # driver.switch_to.window(all_window_handles[-1])
        # driver.execute_script(f"window.location.href = '{convocation_url}'")
        # time.sleep(2)
        # driver.switch_to.window((all_window_handles[0]))


        # Switch to the new tab (usually the last one opened)
        # driver.switch_to.window(awindow_handles[2])
        # driver.execute_script(f"window.location.href = '{about_us_url}'")
        # time.sleep(2)
        # driver.switch_to.window((all_window_handles[0]))
        # time.sleep(5)




        # links = driver.find_elements(By.TAG_NAME,'a')
        # time.sleep(2)
        # # Iterate through the list of links and print the href attribute
        # count=0
        # for link in links:
        #     href = link.get_attribute('href')  # Get the 'href' attribute of the <a> tag.
        #     count+=1
        #     print(f"This is the {count} url of {href} : ")
        #     driver.execute_script(f"window.open('{href}', '_blank')")
        #
        # time.sleep(5)
        # driver.switch_to.window(window_handles[0])
        # time.sleep(5)
