import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://www.flemingcollegetoronto.ca/")
driver.maximize_window()
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 10)
#---Hoverig the mouse on About us using Actions chain and perform---
driver.find_element(By.XPATH,"//a[@class='nav__link nav__link--open-menu']//*[name()='svg']").click()
hover_element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='sidebar-menu__link sidebar-menu__link--dropdown'][normalize-space()='About']")))
actions = ActionChains(driver)  # Initialize Actions
actions.move_to_element(hover_element).perform()
#---Extractiing the link and url from the sub menu and opening it on new tab using java Script
our_team_link=driver.find_element(By.XPATH, "(//a[@class='sidebar-menu__link'])[5]")
our_team_url=our_team_link.get_attribute("href")
driver.execute_script(f"window.open('{our_team_url}','_blank')")
#--- Handling the tab using the window_handles ---
window_handles=driver.window_handles
driver.switch_to.window(window_handles[-1])
time.sleep(2)
driver.switch_to.window(window_handles[0])
#--- Again extracting links and url and opeing it in new tabs
brochures_link=driver.find_element(By.XPATH, "//a[normalize-space()='Brochures']")
brochures_url=brochures_link.get_attribute("href")
driver.execute_script(f"window.open('{brochures_url}','_blank')")
#--- Handling the tab using the window_handles ---
window_handles=driver.window_handles
driver.switch_to.window(window_handles[-1])
time.sleep(2)
driver.switch_to.window(window_handles[0])
time.sleep(4)
#----- Again fetching the link and extract url form the link and open it in new Tab using java Script
student_testimonial_link=driver.find_element(By.XPATH,"//a[text()='Student Testimonials']")
student_testimonial_url=student_testimonial_link.get_attribute("href")
driver.execute_script(f"window.open('{student_testimonial_url}','_blank')")
time.sleep(2)
#----- Handling the tab using swithc_to and the window_handles------
window_handles=driver.window_handles
driver.switch_to.window(window_handles[-1])
time.sleep(2)
driver.switch_to.window(window_handles[0])

# ----- Again fetching the link and url and opening it in new tab using the java Script

careers_link=driver.find_element(By.XPATH,"//a[normalize-space()='Careers']")
careers_url=careers_link.get_attribute("href")
driver.execute_script(f"window.open('{careers_url}','_blank')")
time.sleep(2)
#----- Handling the tab using the swithc_to and the window_handles-----
window_handles=driver.window_handles
driver.switch_to.window(window_handles[-1])
time.sleep(2)
driver.switch_to.window(window_handles[0])
time.sleep(3)


