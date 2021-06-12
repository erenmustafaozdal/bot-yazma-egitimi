"""
EbaOgrenciSifreVerme2_mfa
mfatiharslan
"""
from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#Öğrenci no girişi
ogrNumarasi = input("Öğrenci Numarasını Giriniz: ")
driver = webdriver.Chrome(settings.driver_path)

#Mebbis Giriş
driver.get("https://mebbis.meb.gov.tr/")
driver.maximize_window()
kullaniciAdi = driver.find_element_by_id("txtKullaniciAd").send_keys(settings.kullaniciAdi)
kullaniciSifre = driver.find_element_by_id("txtSifre").send_keys(settings.kullaniciSifre + Keys.ENTER)

#Eokul Giriş ve Öğrenciyi bulma
eokul = driver.find_element_by_xpath("//*[@id='team']/div/div/div[2]/div/div/div[1]/div/div/p/a/img")
hover = ActionChains(driver).move_to_element(eokul).perform()
eokulLink = driver.find_element_by_id("rptProjeler_ctl01_rptKullanicilar_ctl00_LinkButton1").click()
driver.switch_to.window(driver.window_handles[-1])
ogrenciIslemleri = driver.find_element_by_xpath("//a[@id='mdlIOO']").click()
ogrNo = driver.find_element_by_id("OGRMenu1_txtTC").send_keys(ogrNumarasi)
ogrAra = driver.find_element_by_id("OGRMenu1_btnAra").click()
time.sleep(5)

# Öğrenci Tc No Alma ve Veri.txt dosyasına geçici olarak yazdırma

ogrenciTcno=driver.find_element(By.ID,"IOMPageHeader1_lblOgrenciTCNo")
dosya = open("veri.txt", "w", encoding="utf-8")
dosya.write(ogrenciTcno.text)
time.sleep(2)

#Ebaya Giriş
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
# Profil menüsünü açma
profil_menu = driver.find_element_by_xpath("//div[@id='vcProfileWidget']//div[@class='vc-profile-widget-caret vc-position-relative']").click()
time.sleep(5)

# Öğretmenin  Şifre Vereceği  Bölümüne Giriş
ogrtsifre = driver.find_element_by_xpath("//div[@id='eba-menu-panel']//div[2]//a[1]//div[1]").click()
time.sleep(3)

#Ekrana gelen uyarıyı kapatma

uyarı_kapat = driver.find_element_by_xpath('//*[@id="uyari"]/div/div/div[1]/button').click()
time.sleep(2)

# Kaydettiğimiz Öğrenci Tc' sini giriş
dosya = open("veri.txt", "r")
oge =dosya.readlines()

inputbox = driver.find_element(By.ID, 'studentTckn').send_keys(oge)

bilgigetir = driver.find_element_by_xpath('//*[@id="get-tckn"]/button').click()
time.sleep(2)

#Tek Kullanımlık Giriş Şifresi Oulşturma
teksifre = driver.find_element_by_xpath("//button[contains(text(),'Tek Kullanımlık Giriş Şifresi Oluştur')]")
time.sleep(1)
teksifre.click()
yenisifreal= driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/h1/code')
yenisifre = driver.find_element_by_id("user-pass")
time.sleep(2)

#Tek kullanımlık Şifreyi Veri.Txt ye Yazdırma
dosya=open("veri.txt","w") # w olmasının sebebi Tc bilgisi kayıtlı kalmasın "a" yapılabilir
dosya.write("\n"+yenisifre.text) # üst satırda a olursa alt satıra geçsin diye \n
driver.close()