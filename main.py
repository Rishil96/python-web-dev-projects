# Amazon Automated Price Tracker
import smtplib
import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# Step 1: Load environment variables from .env file
load_dotenv()

# Step 2: Setup Product name, URL and price we want to pay for the product
PRODUCT = "Redragon K617 Fizz 60% Wired RGB Gaming Keyboard"
URL = ("https://www.amazon.in/Redragon-K617-Keyboard-Mechanical-Supported/dp/B09BVCVTBC/ref=sr_1_7?"
       "crid=GFGCNKGEMIGL&dib=eyJ2IjoiMSJ9.U39jaBA8IB03lndvbVcxqPZUMYgwrL9fAkPUnbp40JBEhp1SoYkFH9iufuPj-"
       "9lOZC4NU7pSAmy5E9wqrhS7ODzzftoYhjdRwNE0ewvrXOwcYAmJKIWV2yT8cTPQBnPnPEpEwn0a8NGE6slFWbijQBf1iFXz9P"
       "JWvk7j7DVNv194G0uYaEeN0eTvtCOwaDrqrSz_4V0jQQ3Ls4jUDDEMCXLT941DKkDk5TZBpSPY4Y4.fSxVSKHTSTYSpGU2-InJQ"
       "2ey3UwcSL6GCnZLuz7GOG8&dib_tag=se&keywords=mechanical%2Bkeyboards%2Bwireless&qid=1729592987&"
       "sprefix=mechanical%2B%2Caps%2C250&sr=8-7&th=1")
PRICE = 2000

# Step 3: Create selenium webdriver and get the webpage
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Step 4: Target price tag
price_symbol = driver.find_element(by=By.CLASS_NAME, value="a-price-symbol")
price_amount = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
current_price = float(price_amount.text.replace(",", ""))


# Step 5: Send email using SMTP to inform about the discounted price
if current_price <= PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        email = os.environ.get("USER_EMAIL_ID")
        password = os.environ.get("USER_EMAIL_PASSWORD")
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=f"Subject:Amazon Discount Alert for {PRODUCT}\n\n"
                                f"The current price for {PRODUCT} is at {price_symbol.text}{price_amount.text}.\n"
                                f"Link: {URL}\n"
                                f"Hurry up before the price goes back up again!")
        print(f"{PRODUCT} is at discount. Notification sent successfully!")
else:
    print(f"{PRODUCT} too expensive at the moment!")

# Step 6: Close the webdriver
driver.quit()
