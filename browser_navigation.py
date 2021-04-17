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

# bulunduğum adresi yazdıralım
print(driver.current_url)
time.sleep(2)

# Yeni adrese git
driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
print(driver.current_url)
time.sleep(2)

#Bir önceki sayfaya geri dön
driver.back()
print(driver.current_url)
time.sleep(2)

# Bir sonraki sayfaya dön
driver.forward()
print(driver.current_url)
time.sleep(2)

# Sayfanın başlığı yazdıralım
print(driver.title)

time.sleep(2)

# tarayıcıyı kapat
driver.close()
