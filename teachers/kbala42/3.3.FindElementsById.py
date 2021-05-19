"""
FindElementsModalClose: Modal penceresinde kapatma butonunu bulduk. Pencereyi kapatıyoruz
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

time.sleep(1)

# Belirlediğimiz sayfayı açıyoruz
driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")

# id olarak belirlediğimiz elmanı değişkende saklıyoruz
#form=driver.find_element_by_id("choice_form")
#ikinci kullanım
form = driver.find_element(By.ID, "choice_form")

#elemanı içeriğini yazdırıyoruz
print(form.text)


# Sayfayı kapatıyoruz
driver.close()