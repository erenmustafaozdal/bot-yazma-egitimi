"""
multi_browser: birden fazla işlem yapılan dosya
"""

# paketimizi içeri aktardık
from selenium import webdriver
import settings

#chrome nesnesi oluşturalım
#driver = webdriver.Chrome(executable_path=settings.driver_path)

#firefox nesnesi oluşturalım
#driver = webdriver.Firefox(executable_path=settings.firefox_path)

#IE Explorer
driver = webdriver.Ie(executable_path=settings.ie_path)

#bir adrese git
driver.get("https://giris.eba.gov.tr/EBA_GIRIS/student.jsp")

# tarayıcıyı kapat
driver.close()