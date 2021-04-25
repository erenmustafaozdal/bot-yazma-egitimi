from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(settings.driver_path)
driver.get("https://istanbulakademi.meb.gov.tr/")
driver.maximize_window()


#ekran görüntüsü almak için kullandık
driver.save_screenshot("./images/ekran-goruntusu.png")

#çıkan pencereyi kapatmak için ekledik
#button = driver.find_element(By.CLASS_NAME, "btn-warning")
button = driver.find_element_by_class_name("btn-warning")
button.click()

driver.close()

#PYCHARMDA PROJE OLARAK OLUŞTURULMADIĞI İÇİN HATA ALDIK (KLASÖR OLARAK AÇILMIŞ) DÜZELDİ