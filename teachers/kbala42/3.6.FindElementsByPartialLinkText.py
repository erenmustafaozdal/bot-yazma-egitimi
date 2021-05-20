"""
FindElementsByPartialLinkText: Kısmi bağlantı metni ile elemana ulaşma
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

# Modal penceresi lapatma butonunu bulduktan sonra onu bir değişkende saklıyoruz
#button = driver.find_element_by_class_name("btn-warning")
# ikinci kullanım
button = driver.find_element(By.CLASS_NAME,"btn-warning")
# Butona tıklatıyoruz
button.click()

# Belirlediğimiz sayfayı açıyoruz
driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")

time.sleep(1)

# Kısmi olarak belirlediğimiz sözcük sayfasına gidiyoruz
link=driver.find_element_by_partial_link_text("Hata")
# Belirlediğimiz sayfayı açıyoruz
link.click()

time.sleep(2)

# Sayfayı kapatıyoruz
driver.close()