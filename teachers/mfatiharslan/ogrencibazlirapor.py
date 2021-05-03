from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import  settings
import time
driver= webdriver.Chrome(settings.driver_path)
driver.maximize_window()
driver.set_page_load_timeout(10)
try:

    driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
    driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()
    driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)
    driver.find_element_by_id("egpField").send_keys(settings.password)
    driver.find_element_by_xpath("//input[@name='submitButton']").click()
except:
    print("Sayfa 10 Saniyede Yüklenemedi...")
    driver.refresh()

while True:

    eba_wait= WebDriverWait(driver,timeout=3,poll_frequency=1)
    try:
        eba_wait.until(ec.invisibility_of_element((By.ID,"generalPreloader")))
        break
    except:
        print("Çok bekledi. Sayfa yenileniyor...")
        driver.refresh()


wait=WebDriverWait(driver,timeout=3,poll_frequency=1)

wait.until(ec.element_to_be_clickable((By.XPATH , "//div[contains(@class,'vc-lm-item-title')][normalize-space()='Raporlar']"))).click()
driver.find_element_by_xpath('//*[@id="vcReportsController"]/div[2]/div/div[1]/div[1]/div/div/div[2]').click()
time.sleep(5)

driver.close()
