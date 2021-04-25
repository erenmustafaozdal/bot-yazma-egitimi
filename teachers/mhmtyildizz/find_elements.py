from selenium import webdriver
import settings

import time


driver = webdriver.Chrome(settings.driver_path)
driver.get("https://istanbulakademi.meb.gov.tr/")
driver.maximize_window()


driver.close()