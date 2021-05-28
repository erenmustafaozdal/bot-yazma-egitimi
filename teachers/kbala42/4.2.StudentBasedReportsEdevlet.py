"""
Bu aşamada EBA Giriş sayfasından E-Devlet giriş sayfasına Devlet butonunu tıklatarak geiriyoruz
"""

from selenium import webdriver
import settings
import  time

# nesne olştur ve değişkene at
driver = webdriver.Chrome(settings.driver_path)
# sayfayı maksimize yapıyoruz
driver.maximize_window()

#EBA' ya giriş yap
driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")

# e-devlet butonu dallanma elmanını selector ile tespit edip e-devlet sayfasına gidiyoruz
driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()

# 2 saniye bekletiyoruz
time.sleep((2))

# Sayfayı kapatıyoruz
driver.close()