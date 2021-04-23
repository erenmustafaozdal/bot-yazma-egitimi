"""
find element: sayfa elemanlarını bul iişlem yap
"""
from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(settings.driver_path)
driver.get("https://istanbulakademi.meb.gov.tr/")
driver.maximize_window()

#karşımıza çıkan reklamı kapatma
#button = driver.find_element_by_class_name("btn-warning")
#kısa yol class name ile elemana ulaşma
button = driver.find_element(By.CLASS_NAME, "btn-warning")
button.click()
time.sleep(1)

# id ile elemana ulaşma
driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")

#form = driver.find_element_by_id("choice_form")
#by kullanarak yapma
form = driver.find_element(By.ID, "choice_form")
print(form.text)

# name öz niteliği ile elemana ulaşma
#keywords = driver.find_element_by_name("keywords")
#veya by ile
keywords = driver.find_element(By.NAME, "keywords")
print(keywords.get_attribute("content"))

#bağlantı metni ile elemana ulaşma
#link = driver.find_element_by_link_text("Teknoloji Akademisi")
#link.click()

#kısmi bağlantı metni ile eleman oluşturma
link = driver.find_element_by_partial_link_text("Hata")
link.click()
#etiket adı ile elemana ulaşma
name = driver.find_element_by_tag_name("input")
name.send_keys("ELİF YILDIZ")
#css seçici ile elemana ulaşma
email = driver.find_element_by_css_selector("#sender_email")
email.send_keys("elif@gmail.com")
time.sleep(2)
email.clear()




