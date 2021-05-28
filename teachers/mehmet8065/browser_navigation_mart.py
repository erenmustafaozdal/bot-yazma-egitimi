"""
browser_navigation: Tarayıcıda gezinme işlemleri
"""
from selenium import webdriver
import settings_example
import time

# tarayıcı nesnesi oluşturalım
driver = webdriver.Chrome(settings_example.driver_path)

# adrese git
driver.get("https://istanbulakademi.meb.gov.tr")

# bulunduğum adresi yazdıralım
print(driver.current_url)

time.sleep(2)

# yeni adrese git
driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
print(driver.current_url)

time.sleep(2)

# bir önceki sayfaya dön
driver.back()
print(driver.current_url)

time.sleep(2)

# bir sonraki sayfa dön
driver.forward()
print(driver.current_url)

time.sleep(2)

# sayfa başlığını yazdıralım
print(driver.title)

time.sleep(2)

# tarayıcıyı kapat
driver.close()
