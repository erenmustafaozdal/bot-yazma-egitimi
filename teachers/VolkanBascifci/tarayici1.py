"""
browser_navigation: Tarayıcıda gezinme işlemleri
"""
from selenium import webdriver
import settings
import time

# tarayıcı nesnesi oluşturalım
driver = webdriver.Chrome(settings.driver_path)

# adrese git
driver.get("https://istanbulakademi.meb.gov.tr")

time.sleep(2)

driver.get()

# tarayıcıyı kapat
driver.close()