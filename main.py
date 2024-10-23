# Cookie Clicker Project
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Create Chrome Driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

# Step 2: Setup time objects to create a 5-minute range to run the cookie clicker
timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5 minutes

# Step 3: Get cookie to click on
cookie = driver.find_element(By.ID, "cookie")

# Step 4: Get all products to buy that speeds up clicking cookies
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]


# Step 5: Start clicking on cookie
while time.time() <= five_min:
    # Click cookie
    cookie.click()

    # If 5 second mark is reached then go to the shop to purchase upgrades
    if time.time() > timeout:
        # Get all upgrade tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, index in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = index

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5


# Step 6: Print final cookie per second result
cookie_per_s = driver.find_element(by=By.ID, value="cps").text
print("Cookie per second:", cookie_per_s)
