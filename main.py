# Amazon Automated Price Tracker
import requests
import smtplib
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Step 1: Load environment variables from .env file
load_dotenv()

# Step 2: Read HTML from Product URL using requests
PRODUCT = "Instant Pot"
URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=URL)
product_html = response.text

# Step 3: Create BS4 object to extract the price from the page
soup = BeautifulSoup(product_html, "lxml")

price_element = soup.select_one(selector=".a-price .a-offscreen")
price = price_element.getText()[1:]

# Step 4: Send email using SMTP to inform about the discounted price
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    email = os.environ.get("USER_EMAIL_ID")
    password = os.environ.get("USER_EMAIL_PASSWORD")
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email,
                        to_addrs=email,
                        msg=f"Subject:Amazon Discount Alert for {PRODUCT}\n\n"
                            f"The current price for {PRODUCT} is at ₹{price}.\n"
                            f"Link: {URL}\n"
                            f"Hurry up before the price goes back up again!")
    print("Mail sent successfully!")
