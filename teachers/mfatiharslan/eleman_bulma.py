from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(settings.driver_path)
driver.get("https://www.eba.gov.tr/")

#button = driver.find_element_by_xpath("//button[contains(text(),'KAPAT')]")
#button.click()

link=driver.find_element_by_link_text("ÖĞRETMEN")
link.click()

button= driver.find_element_by_xpath("//button[@title='edevlet girişi']//div[2]")
button.click()

tc = driver.find_element_by_id("tridField")
tc.click()
tc.send_keys("12345678912")

sifre = driver.find_element_by_id("egpField")
sifre.click()
sifre.send_keys("1145555")

giris= driver.find_element_by_class_name("submitButton")
giris.click()

time.sleep(2)
driver.close()

