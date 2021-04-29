from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(settings.driver_path)
driver.get("https://istanbulakademi.meb.gov.tr/")
driver.maximize_window()

# class name ile elemana ulaşma
button=driver.find_element(By.CLASS_NAME, "btn-warning")
button.click()
#faaliyet=driver.find_elements_by_class_name("btn-info")
#print(len(faaliyet))
#faaliyet.click()

# id ile elemana ulaşma
driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
#form = driver.find_element_by_id("choice_form")
#form= driver.find_element(By.ID,"choice_form")
#print(form.text) formu yazdırma

# name özniteliği ile elemana ulaşma
#anahtar_kelimeler = driver.find_element_by_name("keywords")
#anahtar_kelimeler=driver.find_element(By.NAME, "author")
#print(anahtar_kelimeler.get_attribute("content"))
#get_attribute anahtar kelimenin özniteliği ile content e ulaş getir ve yazdır

# bağlantı metni ile elemana ulaşma
#link = driver.find_element_by_link_text("Yorumlar")
#link=driver.find_element(By.LINK_TEXT,"Yorumlar")
#link.click()

# kısmi bağlantı metni ile elemana ulaşma
link = driver.find_element_by_partial_link_text("Hata")
link.click()

#etiket adı ile elemana ulaşma
#name = driver.find_element_by_tag_name("input")
#name.send_keys("Nuray Yüzüak")

time.sleep(4)
driver.close()