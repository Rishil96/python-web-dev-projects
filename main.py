# Data Entry Automation
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# ---------------------------- Scrape apartment links from Zillow ---------------------------- #
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

zillow_response = requests.get(url=ZILLOW_URL)
soup = BeautifulSoup(zillow_response.text, "lxml")

apartments = soup.select(selector=".StyledPropertyCardDataWrapper")
all_apartment_details = []

for apartment in apartments:
    # Save current apartment details
    address = apartment.select_one(selector="address[data-test=\"property-card-addr\"]").text
    price = apartment.select_one(selector="span[data-test=\"property-card-price\"]").text
    link = apartment.select_one(selector=".StyledPropertyCardDataArea-anchor").get_attribute_list("href")[0]

    current_apartment_details = {
        "address": address.strip(),
        "price": price,
        "link": link
    }
    # Append current apartment details to list in dictionary format
    all_apartment_details.append(current_apartment_details)

# ------------------------------- Form filling using Selenium -------------------------------#
driver = webdriver.Chrome()

for apartment in all_apartment_details:
    driver.get(url="https://forms.gle/LwBVzA2Xyzd4kT9t5")

    # Find all fields using XPATH
    address_field = driver.find_element(by=By.XPATH,
                                        value="//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/div/div/div[2]/"
                                              "div/div[1]/div/div[1]/input")
    price_field = driver.find_element(by=By.XPATH,
                                      value="//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[2]/div/div/div[2]"
                                            "/div/div[1]/div/div[1]/input")
    link_field = driver.find_element(by=By.XPATH,
                                     value="//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[3]/div/div/div[2]/"
                                           "div/div[1]/div/div[1]/input")

    # Fill all fields
    address_field.send_keys(apartment.get("address", "no address found"))
    time.sleep(1)
    price_field.send_keys(apartment.get("price", "no price found"))
    time.sleep(1)
    link_field.send_keys(apartment.get("link", "no link found"))
    time.sleep(1)

    # Click on submit button
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="div[aria-label=\"Submit\"]")
    submit_button.click()
    time.sleep(3)

driver.quit()
