"""
find_elements: sayfa elemanlarını bulup işlemler yapacağız.
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

# sınıf adıyla ulaşma
# btn-wwarning sınıfındaki elemanı bulup tıklatıyoruz
#button = driver.find_element_by_class_name("btn-warning")
# ikinci kullanım
button = driver.find_element(By.CLASS_NAME,"btn-warning")
button.click()

#time.sleep(1)

# id ile elemana ulaşma
driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
#form = driver.find_element_by_id("choice_form")
#form = driver.find_element(By.ID, "choice_form")
#print(form.text)

# name öz niteliği ile elemana ulaşma
#anahtar_kelimeler = driver.find_element_by_name("keywords")
#print(anahtar_kelimeler.get_attribute("content"))

# bağlantı metni ile elemana ulaşma
#link = driver.find_element_by_link_text("Teknoloji Akademisi")
#link.click()
#time.sleep(2)

#kısmi bağlantı metni ile elemana ulaşma
link = driver.find_element_by_partial_link_text("Hata Bildir")
link.click()

# etiket adı ile elemana ulaşma
#name = driver.find_element_by_tag_name("input")
#name.send_keys("Kamil Bala")

#css seçci ile elemana ulaşma
#email = driver.find_element_by_css_selector("#sender_email")
#time.sleep(2)
#email.send_keys("kbala42@aim.com")

address = driver.find_element_by_xpath('//ul[@class="v-list"]/li[1]')
print(address.text)

time.sleep(2)

#driver.close()
