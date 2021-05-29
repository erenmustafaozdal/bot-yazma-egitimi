"""
EbaGiris_mfa_mfa
mfatiharslan
"""
from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(settings.driver_path)
driver.get("https://eba.gov.tr/")
driver.maximize_window()
driver.set_page_load_timeout(10)
#
# driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
# button = driver.find_element_by_xpath("//button[@title='edevlet girişi']//div[2]")
# button.click()
#
# tc = driver.find_element_by_id("tridField")
# tc.click()
# tc.send_keys(settings.tc)
#
# sifre = driver.find_element_by_id("egpField")
# sifre.click()
# sifre.send_keys(settings.password)
try:
    driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
    driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()
    driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)
    driver.find_element_by_id("egpField").send_keys(settings.password)
    driver.find_element_by_xpath("//input[@name='submitButton']").click()
except:
    # tıklama sonrası sayfa 10 saniyede yüklenemedi ise
    print("Sayfa 10 saniyede yüklenemedi...")
    driver.refresh()

while True:
    eba_wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
    try:
        eba_wait.until(ec.invisibility_of_element((By.ID, "generalPreloader")))
        break # gizlendi ise döngüden çık
    except:
        print("Çok bekledi. Sayfa yenileniyor...")
        driver.refresh()
time.sleep(5)
profil_menu = driver.find_element_by_xpath("//div[@id='vcProfileWidget']//div[@class='vc-profile-widget-caret vc-position-relative']").click()
time.sleep(5)
ogrtsifre = driver.find_element_by_xpath("//div[@id='eba-menu-panel']//div[2]//a[1]//div[1]").click()
time.sleep(3)
kapat = driver.find_element_by_xpath('//*[@id="uyari"]/div/div/div[1]/button').click()
time.sleep(2)

tc_no = open("veri.txt", "r")
item = tc_no.readlines()

inputbox = driver.find_element(By.ID, 'studentTckn').send_keys(item)

bilgigetir = driver.find_element_by_xpath('//*[@id="get-tckn"]/button').click()
time.sleep(2)
teksifre = driver.find_element_by_xpath("//button[contains(text(),'Tek Kullanımlık Giriş Şifresi Oluştur')]")
time.sleep(1)
teksifre.click()
yenisifreal= driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/h1/code')
yenisifre = driver.find_element_by_id("user-pass")
time.sleep(2)

dosya=open("veri.txt","a")
dosya.write("\n"+yenisifre.text)