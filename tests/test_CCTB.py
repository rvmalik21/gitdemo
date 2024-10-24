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
        # ----- This is will open the Convocation link ------
        convocation_link=driver.find_element(By.XPATH, "(//a[text()='Convocation'])[2]")
        convocation_url=convocation_link.get_attribute('href')
        window_handles = driver.window_handles
        driver.execute_script(f"window.open('{convocation_url}', '_blank')")
        time.sleep(3)
        print(f"this is the url {convocation_url}")
        about_us_link = driver.find_element(By.XPATH,
                                            "//a[@class='nav-link font-bold-18'][normalize-space()='About Us']")
        # ----- This is will open the about_us link ------
        about_us_url = about_us_link.get_attribute('href')
        driver.execute_script(f"window.open('{about_us_url}', '_blank')")
        time.sleep(3)
        print(f"this is the url {about_us_url}")
        # ----- This is will open the program link ------
        program_link = driver.find_element(By.XPATH,
                                           "//a[@class='nav-link font-bold-18'][normalize-space()='Programs']")
        program_url = program_link.get_attribute("href")
        driver.execute_script(f"window.open('{program_url}','_blank')")
        time.sleep(3)
        print(f"this is the url {program_url}")
        # ----- This is will open the admission link ------
        admission_link=driver.find_element(By.XPATH, "//a[@class='nav-link font-bold-18'][normalize-space()='Admissions']")
        admission_url=admission_link.get_attribute("href")
        driver.execute_script(f"window.open('{admission_url}','_blank')")
        time.sleep(3)
        print(f"this is the url {admission_url}")
        # ----- This is will open the accommodation link ------
        accommodation_link=driver.find_element(By.XPATH, "(//a[text()='Accommodation'])[3]")
        accommodation_url=accommodation_link.get_attribute("href")
        driver.execute_script(f"window.open('{accommodation_url}')")
        time.sleep(3)
        print(f"this is the url {accommodation_url}")
        # ----- This is will open the Location  link ------
        location_link = driver.find_element(By.XPATH, "(//a[text()='Location'])[3]")
        location_url = location_link.get_attribute("href")
        driver.execute_script(f"window.open('{location_url}','_blank')")
        time.sleep(3)

        print(f"this is the url {location_url}")
        # -----This will open the Contact Us link ------(//a[text()='Contact Us'])[2]
        Contact_Us_link = driver.find_element(By.XPATH, "(//a[text()='Contact Us'])[2]")
        Contact_Us_url = Contact_Us_link.get_attribute("href")
        driver.execute_script(f"window.open('{Contact_Us_url}','_blank')")
        time.sleep(3)

        print(f"this is the url {Contact_Us_url}")
        all_window_handles = driver.window_handles
        print(f"These are the session for individuals tabs opened here {all_window_handles}")
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
