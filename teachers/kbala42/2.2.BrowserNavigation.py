"""
BrowserNavigation.py: Tarayıcıda gezinme işlemleri
"""
from selenium import webdriver
import settings
import time

# driver adında bir Chrome nesnesi oluşturuyoruz
driver = webdriver.Chrome(settings.driver_path)

# Girilen adrese gidiyoruz
driver.get("https://istanbulakademi.meb.gov.tr")

# bulunduğumuz url adresini console penceresinde yazdırıyoruz
print(driver.current_url)
# 2. saniye web sayfasını bekletiyoruz
time.sleep(2)

# Girilen yeni adrese gidiyoruz
driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
print(driver.current_url)
# 2. saniye web sayfasını bekletiyoruz
time.sleep(2)

# Bir önceki web sayfasına geri dönüyoruz
driver.back()
# bulunduğumuz url adresini console penceresinde yazdırıyoruz
print(driver.current_url)
# 2. saniye web sayfasını bekletiyoruz
time.sleep(2)

# Bir sonraki sayfaya dönüyoruz
driver.forward()
# bulunduğumuz url adresini console penceresinde yazdırıyoruz
print(driver.current_url)
# 2. saniye web sayfasını bekletiyoruz
time.sleep(2)

# Sayfanın başlığını  console penceresinde yazdırıyoruz
print(driver.title)
# 2. saniye web sayfasını bekletiyoruz
time.sleep(2)

# Tarayıcımızı kapatıyoruz
driver.close()
