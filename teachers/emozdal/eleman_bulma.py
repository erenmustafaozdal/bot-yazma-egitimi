from selenium import webdriver
import settings
import time

driver = webdriver.Chrome(settings.driver_path)
driver.get("https://istanbulakademi.meb.gov.tr/")
driver.maximize_window()

time.sleep(2)

driver.close()
