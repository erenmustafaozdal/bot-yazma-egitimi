from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(settings.driver_path)
driver.get("https://istanbulakademi.meb.gov.tr/")
driver.maximize_window()
button=driver.find_element(By.CLASS_NAME, "btn-warning")
button.click()
#faaliyet=driver.find_elements_by_class_name("btn-info")
#print(len(faaliyet))
#faaliyet.click()
#driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
#form = driver.find_element_by_id("choice_form")
#form= driver.find_element(By.ID,"choice_form")
#print(form.text) formu yazdırma

#anahtar_kelimeler = driver.find_element_by_name("keywords")
anahtar_kelimeler=driver.find_element(By.NAME, "author")
print(anahtar_kelimeler.get_attribute("content"))
#get_attribute anahtar kelimenin özniteliği ile content e ulaş getir ve yazdır
time.sleep(2)
driver.close()