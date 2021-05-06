from  selenium import webdriver
import settings
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


# tarayıcı nesnesi oluştur
driver = webdriver.Chrome(settings.driver_path)
driver.maximize_window()

# EBA'ya giriş yap
driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()
driver.find_element_by_xpath("//input[@id='tridField']").send_keys(settings.tc)
driver.find_element_by_id("egpField").send_keys(settings.password)
driver.find_element_by_xpath("//input[@name='submitButton']").click()
time.sleep(2)
#tarayıcıyı kapat
driver.close()