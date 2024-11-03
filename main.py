# Advanced Selenium Features
import pathlib
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get(url="http://localhost:8000/")

name = "Rishil"
email = "rishil.ramesh@gmail.com"
password = "Rishil123#"

# 1. Enter name, email, password on input fields
name_field = driver.find_element(by=By.ID, value="name")
email_field = driver.find_element(by=By.ID, value="email")
password_field = driver.find_element(by=By.ID, value="password")

name_field.send_keys(name)
time.sleep(1)
email_field.send_keys(email)
time.sleep(1)
password_field.send_keys(password)
time.sleep(1)


# 2. Upload file
file_path = str(pathlib.WindowsPath(os.getcwd(), "data.txt"))
print(file_path)

file_upload = driver.find_element(by=By.ID, value="fileUpload")
file_upload.send_keys(file_path)
time.sleep(1)

# 3. Select an option
drop_down = driver.find_element(by=By.ID, value="options")
select = Select(drop_down)

select.select_by_visible_text("Option 2")
time.sleep(1)
select.select_by_value("option1")
time.sleep(1)
select.select_by_index(2)
time.sleep(1)

# 4. Click Buttons
buttons = driver.find_elements(by=By.TAG_NAME, value="button")

# Submit button
buttons[0].click()
time.sleep(1)

# Popup button
buttons[1].click()
time.sleep(1)

driver.find_element(by=By.ID, value="popup").click()

# 5. Click link
link = driver.find_element(by=By.ID, value="dynamicContent")
link.click()
time.sleep(1)

# 6. Interact with IFrame
iframe = driver.find_element(by=By.ID, value="div#iframeContainer iframe")
driver.switch_to.frame(iframe)

iframe_link = driver.find_element(by=By.TAG_NAME, value="a")
iframe_link.click()
time.sleep(1)

driver.switch_to.default_content()
driver.execute_script("alert('Selenium OP!')")

print("Interaction complete!")

