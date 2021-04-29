"""
find_elements:  sayfa elemanlarını bulup işlemler yapacağız
"""
from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(settings.driver_path)
driver.get("https://istanbulakademi.meb.gov.tr/")
driver.maximize_window()

# class name ile elemana ulaşma
# button = driver.find_element_by_class_name("btn-warning")
button = driver.find_element(By.CLASS_NAME, "btn-warning")
button.click()

# id ile elemana ulaşma
driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
# form = driver.find_element_by_id("choice_form")
# form = driver.find_element(By.ID, "choice_form")
# print(form.text)

# name özniteliği ile elemana ulaşma
# anahtar_kelimeler = driver.find_element_by_name("keywords")
# anahtar_kelimeler = driver.find_element(By.NAME, "keywords")
# print(anahtar_kelimeler.get_attribute("content"))

# bağlantı metni ile elemana ulaşma
# link = driver.find_element_by_link_text("Teknoloji Akademisi")
# link.click()
# time.sleep(2)

# kısmi bağlantı metni ile elemana ulaşma
link = driver.find_element_by_partial_link_text("Hata")
link.click()

# etiket adı ile elemana ulaşma
# name = driver.find_element_by_tag_name("input")
# name.send_keys("Eren Mustafa ÖZDAL")

# css seçici ile elemana ulaşma
# By.CSS_SELECTOR
# email = driver.find_element_by_css_selector("#sender_email")
# email.send_keys("ali@gmail.com")
# time.sleep(2)
# email.clear()
# email.send_keys("eren.060737@gmail.com")

time.sleep(2)

# xpath seçici ile elemana ulaşma
address = driver.find_element_by_xpath('//ul[@class="v-list"]/li[1]')
print(address.text)



# tarayıcıyı kapat
driver.close()
#Murat Altun
