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
        driver.implicitly_wait(5)
        driver.get("https://www.lcca.org.uk/")
        # Maximize the opened window
        driver.maximize_window()
        #time.sleep(5)
        # specify the image locater for the image
        driver.find_element(By.CSS_SELECTOR,"div[class='social-icons'] div:nth-child(1) a:nth-child(1)").click()
        # Get all window handles
        time.sleep(2)
        #driver.find_element(By.XPATH, "(//a[text()='Home'])[2]").click()
        window_handles= driver.window_handles
        #time.sleep(3)
        # Switch to the new tab (usually the last one opened)
        driver.switch_to.window(window_handles[1])
        time.sleep(2)
        # Whatapp_element=driver.find_element(By.XPATH,"//img[@alt='WhatsApp Main Page']")
        # # time.sleep(2)
        # # Whatapp_element.screenshot("Whatapp_element.png")
        # # #driver.switch_to.window(window_handles[2])
        # time.sleep(2)
        # driver.get_screenshot_as_file("screenshot.png")
        # # Switch back to the first tab
        driver.switch_to.window(window_handles[0])
        time.sleep(2)
        #driver.refresh()
        about_us_link=driver.find_element(By.XPATH,"(//a[text()='About Us'])[1]")
        about_us_url=about_us_link.get_attribute('href')
        # Use JavaScript to open the 'About Us" link in new tab
        driver.execute_script(f"window.open('{about_us_url}','_blank');")
        time.sleep(2)
        window_handles=driver.window_handles
        time.sleep(2)
        driver.switch_to.window(window_handles[2])
        time.sleep(2)
        driver.switch_to.window(window_handles[0])
        time.sleep(2)
        courses_link=driver.find_element(By.XPATH,"(//a[text()='Courses'])[1]")
        courses_url=courses_link.get_attribute('href')
        driver.execute_script(f"window.open('{courses_url}','_blank');")
        time.sleep(2)
        window_handles=driver.window_handles
        driver.switch_to.window(window_handles[3])
        time.sleep(2)
        driver.switch_to.window(window_handles[0])
        time.sleep(2)
        LCCA_Life_link=driver.find_element(By.XPATH,"(//a[text()='LCCA Life'])[1]")
        LCCA_Life_url=LCCA_Life_link.get_attribute('href')
        driver.execute_script(f"window.open('{LCCA_Life_url}','_blank');")
        time.sleep(2)
        window_handles=driver.window_handles
        driver.switch_to.window(window_handles[4])
        time.sleep(2)
        driver.switch_to.window(window_handles[0])
        time.sleep(2)
        Open_Days_link=driver.find_element(By.XPATH,"(//a[text()='Open Days'])[1]")
        Open_Days_url=Open_Days_link.get_attribute('href')
        driver.execute_script(f"window.open('{Open_Days_url}','_blank');")
        time.sleep(2)
        window_handles=driver.window_handles
        driver.switch_to.window(window_handles[5])
        time.sleep(2)
        driver.switch_to.window(window_handles[0])
        time.sleep(2)
        Blogs_link = driver.find_element(By.XPATH, "(//a[text()='Blog'])[1]")
        Blogs_url = Blogs_link.get_attribute('href')
        driver.execute_script(f"window.open('{Blogs_url}','_blank');")
        time.sleep(2)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[6])
        time.sleep(2)
        driver.switch_to.window(window_handles[0])
        time.sleep(2)
        # image_locator= (By.XPATH,"//img[@src='/media/923504/official-logo.gif']")
        # try:
        #     # Use WebDriverWait to wait until the image is present
        #     image_element = WebDriverWait(driver, 10).until(
        #         EC.visibility_of_element_located(image_locator)
        #     )
        #     print("The LCCA image is present on the Website")
        # except:
        #     print(" The LCCA logo image is not present on the site. Please lood into it asap")








