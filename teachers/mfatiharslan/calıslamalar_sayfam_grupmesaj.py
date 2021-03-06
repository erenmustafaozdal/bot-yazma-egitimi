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


wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='vc-lm-item-title '][normalize-space()='Raporlar']"))).click()
time.sleep(2)

#çalışmaları kontrol
driver.find_element_by_xpath("//body/div[@id='indexBaseContainer']/div[@class='vc-fullHeight ng-scope']/div[@class='ng-scope']/div[@id='componentMainView']/div[@class='vc-fullHeight vc-background']/div[@id='componentMainSubView']/div[@role='main']/div[@class='vc-router-content ng-scope']/div[@id='vcReportsController']/div[@class='vc-layout-view-content-padding-headerless']/div[@class='p-w-xs']/div[@class='display-flow-root-class row']/div[1]/div[1]/div[1]").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@id='target1']//div[1]").click()
time.sleep(5)

#mesaj gönderme
driver.find_element_by_xpath("//div[contains(@class,'vc-lm-item-title')][normalize-space()='Sayfam']").click()
time.sleep(5)
driver.find_element_by_css_selector("textarea[placeholder='Ne paylaşmak istersin?']").send_keys(settings.mesaj)
driver.find_element_by_xpath("//option[@label='Bilişim Kurs Sınıfı']").click()
time.sleep(5)
driver.find_element_by_id("vc-PostButton").click()
time.sleep(5)
driver.find_element_by_xpath("//a[contains(text(),'PAYLAŞ')]").click()
time.sleep(5)

# mesajı silme
driver.find_element_by_xpath("//div[@id='vc-feedListItemsContainer']//div[2]//button[1]//i[1]").click()
driver.find_element_by_css_selector("div[class='btn-group pull-right vc-position-absolute pos-r-0 ng-scope dropdown open'] a[class='ng-binding']").click()
driver.find_element_by_xpath("//a[contains(text(),'SİL')]").click()
time.sleep(5)

driver.close()
