"""
MultiBrowser:  Birden çok tarayıcı ile işlem yapılan dosya
"""
# paketimizi içeri aktardık
from selenium import webdriver
from teachers.kbala42 import settings

# driver adında bir Chrome nesnesi oluşturuyoruz
driver = webdriver.Chrome(executable_path=settings.driver_path)


# Girilen adrese gidiyoruz
driver.get("https://istanbulakademi.meb.gov.tr/")


# tarayıcıyı kapatıyoruz
driver.close()
