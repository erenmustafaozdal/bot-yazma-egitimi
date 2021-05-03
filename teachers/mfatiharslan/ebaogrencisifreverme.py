from selenium import webdriver
import  settings
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#ogrNumarasi = input("Öğrenci Numarasını Giriniz: ")
driver = webdriver.Chrome(settings.driver_path)

driver.get("https://mebbis.meb.gov.tr/")
driver.maximize_window()
kullaniciAdi = driver.find_element_by_id("txtKullaniciAd").send_keys(settings.kullaniciAdi)
kullaniciSifre = driver.find_element_by_id("txtSifre").send_keys(settings.kullaniciSifre + Keys.ENTER)

eba = driver.find_element_by_xpath("//div[4]//div[1]//div[1]//div[1]//div[1]//div[1]//p[1]//a[1]//img[1]")
hover = ActionChains(driver).move_to_element(eba).perform()
ebaLink = driver.find_element_by_id("//a[@id='rptProjeler_ctl03_rptKullanicilar_ctl00_LinkButton1']").click()
driver.close()
# # İlkokul-ortaokul öğrenci işlemleri
# ogrenciIslemleri = driver.find_element_by_xpath('//*[@id="mdlIOO"]').click()
#
# # Öğrenci numarası girişi
# ogrNo = driver.find_element_by_id("OGRMenu1_txtTC").send_keys(ogrNumarasi)
#
# # Öğrenci ara
# ogrAra = driver.find_element_by_id("OGRMenu1_btnAra").click()
