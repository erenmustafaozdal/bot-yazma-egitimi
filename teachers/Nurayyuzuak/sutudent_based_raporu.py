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
time.sleep(2)
#tarayıcıyı kapat
driver.close()