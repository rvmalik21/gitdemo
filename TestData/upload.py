import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
file_path= "C:\\Users\\ravi.malik\\Downloads\\downlaod.xlsx"
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()
# Define the locator as a tuple
# button_locator =(By.CLASS_NAME,"button")
# # Wait for the button to be present and then retrieve it
# button= WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(button_locator)
# )
# # Perform the click action
# button.click()
time.sleep(2)
#
# file_input=driver.find_element(By.XPATH, "//input[@type='file']")
# time.sleep(2)
# file_input.send_keys(file_path)
# time.sleep(2)
# wait =WebDriverWait(driver,5)
# toast_text=(By.XPATH, "//div[text()='Updated Excel Data Successfully.']")
# wait.until(EC.presence_of_element_located(toast_text))
# toast_msg=driver.find_element(*toast_text).text
# print(toast_msg)
#
# time.sleep(4)

price= driver.find_element(By.XPATH, "//div[text()='Apple']/parent::div/parent::div/div[@id='cell-4-undefined']")
price_text=price.text

print(price_text)

