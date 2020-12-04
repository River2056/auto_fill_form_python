from selenium import webdriver
from app import prop

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
driver = webdriver.Chrome(prop.driver_path, options=options)
