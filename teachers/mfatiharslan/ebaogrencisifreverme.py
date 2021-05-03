from selenium import webdriver
import  settings
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(settings.driver_path)
driver.get("https://eokul.meb.gov.tr/")
driver.maximize_window()
driver.find_element_by_xpath("//img[@alt='e-Okul Yönetimi Bilgi Sistemi Girişi']").click()
driver.find_element_by_xpath("//button[@id='btnEdevletGiris']")