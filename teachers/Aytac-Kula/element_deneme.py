from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(settings.driver_path)
driver.get("https://tr.wikipedia.org/wiki/%C4%B0stanbul")
driver.maximize_window()

