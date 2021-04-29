from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(settings.driver_path)
driver.get("https://istanbulakademi.meb.gov.tr/")
driver.maximize_window()
button=driver.find_element(By.CLASS_NAME, "btn-warning")
button.click()


time.sleep(2)
driver.close()