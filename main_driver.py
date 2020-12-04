from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver():
    def __init__(self, driver_path):
        self.driver_path = driver_path

    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        driver = webdriver.Chrome(self.driver_path, options=options)
        return driver
