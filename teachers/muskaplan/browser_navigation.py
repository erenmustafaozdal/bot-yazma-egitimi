"""
mustafa kaplan
browser_navigation: Tarayıcıda gezinme işlemleri
"""
from selenium import webdriver
import settings
import time

# tarayıcı nesnesi oluşturalım
driver = webdriver.Chrome(settings.driver_path)

# adrese git
driver.get("https://sehitoguzhancitoortaokulu.meb.k12.tr/")

# bulunduğum adresi yazdıralım
print(driver.current_url)

time.sleep(2)

# yeni adrese git
driver.get("https://sehitoguzhancitoortaokulu.meb.k12.tr/icerikler/okulumuz-ogrencileri-kendi-muzelerini-olusturuyor_10156929.html")
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
