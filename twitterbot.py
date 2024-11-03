import os
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv


class InternetSpeedTwitterBot:

    INTERNET_SPEED_URL = "https://www.speedtest.net/"
    TWITTER_SIGN_IN_URL = "https://twitter.com/login"

    def __init__(self):
        """
        Init object by creating a Chrome driver and up and down speeds
        """
        load_dotenv()
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """
        Check current internet speed
        """
        self.driver.get(url=self.INTERNET_SPEED_URL)
        print("Loading the speedtest.net website.")
        time.sleep(5)
        # Start test
        go_button = self.driver.find_element(by=By.CSS_SELECTOR, value="a[class=\"js-start-test test-mode-multi\"]")
        go_button.click()
        # Wait till test is complete
        print("Waiting for 1 minute for the test to complete.")
        time.sleep(60)
        # Get results from the test
        print("Getting results from the test.")
        try:
            self.down = self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text
            self.up = self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text
        except Exception as e:
            print(f"An unknown exception occurred: {e}")
            self.down = -1
            self.up = -1

        self.down = float(self.down)
        self.up = float(self.up)
        print(f"Download Speed: {self.down}")
        print(f"Upload Speed: {self.up}")
        time.sleep(3)

    def tweet_at_provider(self):
        """
        Tweet the provider if internet speeds are lower
        """
        twitter_email = os.environ.get("TWITTER_EMAIL")
        twitter_password = os.environ.get("TWITTER_PASSWORD")

        self.driver.get(self.TWITTER_SIGN_IN_URL)

        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/'
                                               'div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH,
                                            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/'
                                                  'div/div[2]/label/div/div[2]/div/input')

        email.send_keys(twitter_email)
        password.send_keys(twitter_password)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
                                                       'div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/'
                                                       'div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div'
                                                       '/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up."
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                      'div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/'
                                                      'div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()
