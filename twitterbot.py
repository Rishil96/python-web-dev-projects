import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

class InternetSpeedTwitterBot:

    INTERNET_SPEED_URL = "https://www.speedtest.net/"

    def __init__(self):
        """
        Init object by creating a Chrome driver and up and down speeds
        """
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

    def tweet_at_provider(self):
        """
        Tweet the provider if internet speeds are lower
        :return:
        """
        pass
