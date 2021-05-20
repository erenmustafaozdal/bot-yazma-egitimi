"""
FindElementsLen.py: Açılan sayfada belirli bir elmanın sayısı
"""
from selenium import webdriver
import settings
import  time
from selenium.webdriver.common.by import By

# nesne olştur ve değişkene at
driver = webdriver.Chrome(settings.driver_path)
driver.get("https://istanbulakademi.meb.gov.tr")
# sayfayı maksimize yapıyoruz
driver.maximize_window()

# Açılan sayfada ki modal penceresini kapatmamız gerekiyor.
# Bunun içinde aynı sınıf adına sahip kaç eleman olduğunu bulmalıyız. Eğer bir tane varsa bizim için belireyici olacaktır.

#Buton class sahip elmanları buluyoruz
print(len(driver.find_elements_by_class_name("btn")))

#Buton class sahip elmanları buluyoruz driver.find_element_by_class_name("btn-warning")
print(len(driver.find_elements_by_class_name("btn-warning")))

# Sayfayı kapatıyoruz
driver.close()