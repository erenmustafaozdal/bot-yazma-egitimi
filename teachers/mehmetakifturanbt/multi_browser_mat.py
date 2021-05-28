"""
multi_browser:  Birden çok tarayıcı ile işlem yapılan dosya
"""
# paketimizi içeri aktardık
from selenium import webdriver
import settings

# Chrome nesnesi oluşturalım
driver = webdriver.Chrome(executable_path=settings.driver_path)

# Firefox nesnesi oluşturalım
driver2 = webdriver.Firefox(executable_path=settings.firefox_path)

# Internet Explorer nesnesi oluşturalım
#driver = webdriver.Ie(executable_path=settings.ie_path)

# bir adrese git
driver.get("https://istanbulakademi.meb.gov.tr/")
driver2.get("http://akifturan.com.tr") #kişisel web sayfam ama henüz içerik girilmedi.

# tarayıcı kapat
driver.close()
driver2.close()
