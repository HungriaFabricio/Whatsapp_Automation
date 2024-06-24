# %%

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time

class Essentials:
    def __init__(self):
        chrome_userdata = r"C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data"
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--remote-debugging-pipe")
        chrome_options.add_argument("enable-automation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--dns-prefetch-disable")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(f"user-data-dir={chrome_userdata}")
        self.driver = uc.Chrome(options=chrome_options, version_main=126, enable_cdp_events=True, headless=True)
        self.url = "https://github.com/"
        self.driver.maximize_window()

    def search(self):
        driver = self.driver
        driver.get(self.url)

essencial = Essentials()
essencial.search()

time.sleep(5)
# %%
