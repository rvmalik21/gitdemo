#from selenium.webdriver.chrome import webdriver
#from selenium.webdriver.chromium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#----- Launching the browser
driver=webdriver.Chrome()
driver.get("https://www.lccm.org.uk/")
driver.maximize_window()
#-----Open Home page in new tab ------
home_link=driver.find_element(By.XPATH,"//li[@class='level-2']//a[normalize-space()='Home']")
home_url=home_link.get_attribute("href")
driver.execute_script(f"window.open('{home_url}','_blank')")
#//div[@class='owl-item']//span[contains(text(),'BOOK A TOUR AT THE MUSIC BOX')]
# ------ Assertion for message present on banner header image-----
msg =driver.find_element(By.XPATH,"//div[@class='owl-item']//span[contains(text(),'BOOK A TOUR AT THE MUSIC BOX')]").text
assert msg == "BOOK A TOUR AT THE MUSIC BOX"
time.sleep(4)
home_window=driver.window_handles
driver.switch_to.window(home_window[-1])
time.sleep(2)
driver.switch_to.window(home_window[0])
time.sleep(2)
#----Open the About Us page in new tab-----
about_us_link=driver.find_element(By.XPATH,"//li[contains(@class,'level-2')]//a[normalize-space()='About us']")
about_us_url=about_us_link.get_attribute("href")
driver.execute_script(f"window.open('{about_us_url}','_blank')")
time.sleep(4)
home_window=driver.window_handles
driver.switch_to.window(home_window[-1])
time.sleep(2)
driver.switch_to.window(home_window[0])
time.sleep(2)
#----- Opent he Courses in new tab using java script------
Courses_link=driver.find_element(By.XPATH,"//li[@class='level-2 horitzontal']//a[normalize-space()='Courses']")
Courses_url=Courses_link.get_attribute("href")
driver.execute_script(f"window.open('{Courses_url}','_blank')")
time.sleep(4)
home_window=driver.window_handles
driver.switch_to.window(home_window[-1])
time.sleep(2)
driver.switch_to.window(home_window[0])
time.sleep(2)
# ----- Open the Live at LCCM in new tab using the java script
Life_at_LCCM_link=driver.find_element(By.XPATH,"//li[contains(@class,'level-2')]//a[normalize-space()='Life at LCCM']")
Life_at_LCCM_url=Life_at_LCCM_link.get_attribute("href")
driver.execute_script(f"window.open('{Life_at_LCCM_url}','_blank')")
time.sleep(4)
home_window=driver.window_handles
driver.switch_to.window(home_window[-1])
time.sleep(2)
driver.switch_to.window(home_window[0])
time.sleep(2)
#----- Open the Open days in new tab using the java script------
Open_day_LCCM_link=driver.find_element(By.XPATH,"//li[contains(@class,'level-2')]//a[normalize-space()='Open Days']")
Open_day_LCCM_url=Open_day_LCCM_link.get_attribute("href")
driver.execute_script(f"window.open('{Open_day_LCCM_url}','_blank')")
time.sleep(4)
home_window=driver.window_handles
driver.switch_to.window(home_window[-1])
time.sleep(2)
driver.switch_to.window(home_window[0])
time.sleep(2)
# ----- Open the Scholarship in new tab using the java Script -----
Scholarship_link=driver.find_element(By.XPATH,"//li[contains(@class,'level-2')]//a[normalize-space()='The Dr. Mathew Knowles Scholarship']")
Scholarship_url=Scholarship_link.get_attribute("href")
driver.execute_script(f"window.open('{Scholarship_url}','_blank')")
time.sleep(4)
home_window=driver.window_handles
driver.switch_to.window(home_window[-1])
time.sleep(2)
driver.switch_to.window(home_window[0])
time.sleep(2)
# ------ Open the Apply header in new tab using the java Script -----
Apply_link=driver.find_element(By.XPATH,"//li[contains(@class,'level-2')]//a[normalize-space()='Apply']")
Apply_url=Apply_link.get_attribute("href")
driver.execute_script(f"window.open('{Apply_url}','_blank')")
time.sleep(4)
home_window=driver.window_handles
driver.switch_to.window(home_window[-1])
time.sleep(2)
driver.switch_to.window(home_window[0])
time.sleep(2)
# ----- Open the Blog header in new tab using the java Script ----
Blog_link=driver.find_element(By.XPATH,"//li[@class='level-2 horitzontal']//a[normalize-space()='Blog']")
Blog_url=Blog_link.get_attribute("href")
driver.execute_script(f"window.open('{Blog_url}','_blank')")
time.sleep(4)
home_window=driver.window_handles
driver.switch_to.window(home_window[-1])
time.sleep(2)
driver.switch_to.window(home_window[0])
time.sleep(2)
# ----- Open the Contact header in new tab using the java Script----
Contact_link=driver.find_element(By.XPATH,"//li[contains(@class,'level-2')]//a[normalize-space()='Contact']")
Contact_url=Contact_link.get_attribute("href")
driver.execute_script(f"window.open('{Contact_url}','_blank')")
time.sleep(4)
home_window=driver.window_handles
driver.switch_to.window(home_window[-1])
time.sleep(2)
driver.switch_to.window(home_window[0])
time.sleep(2)


