"""
multi_browser:  Birden çok tarayıcı ile işlem yapılan dosya
"""
# paketimizi içeri aktardık
from selenium import webdriver
import settings_example

# Chrome nesnesi oluşturalım
driver = webdriver.Chrome(executable_path=settings_example.driver_path)

# Firefox nesnesi oluşturalım
#driver = webdriver.Firefox(executable_path=settings.firefox_path)

# Internet Explorer nesnesi oluşturalım
#driver = webdriver.Ie(executable_path=settings.ie_path)

# bir adrese git
driver.get("https://istanbulakademi.meb.gov.tr/")

# tarayıcı kapat
driver.close()

print("bye")