from selenium import webdriver
import settings
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from html.parser import HTMLParser

ogrNumarasi = input("Öğrenci Numarasını Giriniz: ")
driver = webdriver.Chrome(settings.driver_path)

driver.get("https://mebbis.meb.gov.tr/")
driver.maximize_window()
kullaniciAdi = driver.find_element_by_id("txtKullaniciAd").send_keys(settings.kullaniciAdi)
kullaniciSifre = driver.find_element_by_id("txtSifre").send_keys(settings.kullaniciSifre + Keys.ENTER)

eokul = driver.find_element_by_xpath("//*[@id='team']/div/div/div[2]/div/div/div[1]/div/div/p/a/img")
hover = ActionChains(driver).move_to_element(eokul).perform()
eokulLink = driver.find_element_by_id("rptProjeler_ctl01_rptKullanicilar_ctl00_LinkButton1").click()
driver.switch_to.window(driver.window_handles[-1])
ogrenciIslemleri = driver.find_element_by_xpath("//a[@id='mdlIOO']").click()
ogrNo = driver.find_element_by_id("OGRMenu1_txtTC").send_keys(ogrNumarasi)
ogrAra = driver.find_element_by_id("OGRMenu1_btnAra").click()
time.sleep(5)
r = requests.get("https://e-okul.meb.gov.tr/IlkOgretim/OGR/IOG02001.aspx")
source = driver.page_source
print(source)
time.sleep(2)
tcbul = BeautifulSoup(source, 'html.parser')
time.sleep(2)
for item in tcbul.find_all('span', attrs={"id": "IOMPageHeader1_lblOgrenciTCNo"}):
    print(item.text)

dosya = open("veri.txt", "w", encoding="utf-8")
dosya.write(item.text)
time.sleep(2)

driver.get("https://eba.gov.tr/")
driver.maximize_window()

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

dosya = open("veri.txt", "r")
oge =dosya.readlines()

inputbox = driver.find_element(By.ID, 'studentTckn').send_keys(oge)

bilgigetir = driver.find_element_by_xpath('//*[@id="get-tckn"]/button').click()
time.sleep(2)
teksifre = driver.find_element_by_xpath("//button[contains(text(),'Tek Kullanımlık Giriş Şifresi Oluştur')]")
time.sleep(1)
teksifre.click()
yenisifreal= driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/h1/code')
yenisifre = driver.find_element_by_id("user-pass")
time.sleep(2)

dosya=open("veri.txt","w")
dosya.write("\n"+yenisifre.text)