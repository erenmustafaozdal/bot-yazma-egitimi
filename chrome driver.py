# google chrome tarayıcı driver
# paketimizi içe aktardık

from selenium import webdriver
import settings

# chrome nesnesi oluşturalım
driver= webdriver.Chrome(executable_path=settings.drive_path)
# bir adrese git
driver.get("https://istanbulakademi.meb.gov.tr/")

# tarayıcıyı kapat
driver.close()