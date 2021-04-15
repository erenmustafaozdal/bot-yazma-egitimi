"""
multi_browser:  Birden çok tarayıcı ile işlem yapılan dosya
"""
# paketimizi içeri aktardık
from selenium import webdriver
import settings

# Chrome nesnesi oluşturalım
driver = webdriver.Chrome(executable_path=settings.driver_path)

# bir adrese git
driver.get("https://istanbulakademi.meb.gov.tr/")

# tarayıcı kapat
driver.close()
