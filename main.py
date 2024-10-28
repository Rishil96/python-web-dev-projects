# LinkedIn Job Search
import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://in.linkedin.com/"
SECONDS = 3

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get job role from user
job_role = input("Please enter the job role that you are looking for: ")
print(f"You are searching for the role {job_role}")

# Step 3: Login to LinkedIn
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
time.sleep(SECONDS)

# Find Sign in button and click on it
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
time.sleep(SECONDS)

# Select username and password input fields
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Add email ID and password in login form and click sign in
email = os.environ.get("LINKEDIN_EMAIL_ID")
password = os.environ.get("LINKEDIN_PASSWORD")

username_field.send_keys(email)
password_field.send_keys(password)
time.sleep(SECONDS)

login_button = driver.find_element(By.CSS_SELECTOR, "button[data-litms-control-urn=\"login-submit\"]")
login_button.click()
time.sleep(SECONDS)

# Step 4: Go to search field and search for role
job_search_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"Search\"]")
job_search_field.send_keys(job_role)
job_search_field.send_keys(Keys.ENTER)
time.sleep(SECONDS)


# Step 6: Retrieve job openings and display it on console
job_openings = driver.find_elements(By.CSS_SELECTOR, "div.search-results-container "
                                                     "ul.reusable-search__entity-cluster--"
                                                     "quick-filter-action-container "
                                                     "li a")
job_openings = job_openings[:5]

job_link = 1
for job in job_openings:
    print(f"Job Link {job_link}:", job.get_attribute("href"))
    job_link += 1
