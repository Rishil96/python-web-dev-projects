# Login Page Testing
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

# Open Login page using Selenium
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="http://localhost:8000/")

time.sleep(3)
# Select fields and buttons
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
submit = driver.find_element(By.TAG_NAME, "button")

time.sleep(3)
# Test 1: Click on submit without adding credentials
submit.click()
message = driver.find_element(By.ID, "message")
print("Test 1:", message.text)

time.sleep(3)
# Test 2: Add incorrect credentials and submit
username_field.clear()
password_field.clear()
username_field.send_keys("user123")
password_field.send_keys("password123")
submit.click()
message = driver.find_element(By.ID, "message")
print("Test 2:", message.text)

time.sleep(3)
# Test 3: Add correct credentials and submit
username_field.clear()
password_field.clear()
username_field.send_keys("admin")
password_field.send_keys("admin123")
submit.click()
message = driver.find_element(By.ID, "message")
print("Test 3:", message.text)

username_field.clear()
password_field.clear()
time.sleep(3)

driver.quit()
