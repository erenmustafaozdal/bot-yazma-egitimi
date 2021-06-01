from selenium import webdriver
import settings
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import os
from openpyxl import Workbook, load_workbook
from classes.excel import Excel


def mebbis_is_loaded():
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(@class,'carousel')]")))
    except:
        print("Duyurular paneli için çok bekledi. Sayfa yenileniyor...")
        driver.refresh()
        mebbis_is_loaded()
    else:
        print("Mebbis duyuru paneli yüklendi.")

# e-Okul giriş sayfası açıldıktan sonra sol menünün yüklenmesini bekleme.
def eokul_navbar_is_loaded():
    try:
        wait.until(ec.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class,'navbar')]")))
    except:
        print("Menünün yüklenmesi için çok bekledi. Sayfa yenileniyor...")
        driver.refresh()
        eokul_navbar_is_loaded()
    else:
        print("E-Okul navbar yüklendi.")


# Mebbis'e giriş yapma işlemini gerçekleştiren fonksiyon
def login(tc, password):
    # Mebbis giriş sayfasına git
    driver.get("https://mebbis.meb.gov.tr/default.aspx")
    driver.find_element_by_xpath("//input[@id='txtKullaniciAd']").send_keys(settings.tc)
    driver.find_element_by_xpath("//input[@id='txtSifre']").send_keys(settings.password)

    try:
        driver.find_element_by_xpath("//input[@id='btnGiris']").click()
    except:
        print("Sayfa 10 saniyede yüklenemedi. Sayfa yenileniyor...")
        login(tc, password)
    else:
        print("Mebbis Login başarılı.")
        # Eğer başarılı bir şekilde Mebbis'e giriş
        # yapıldı ise duyurular panelinin yüklenmesini bekle
        mebbis_is_loaded()


# Tablo satırlarının görünmesini bekleyen fonksiyon
def table_is_loaded():
    try:
        return wait.until(ec.visibility_of_all_elements_located(
            (By.XPATH, "//table[@id='dgListem']/tbody/tr")
        ))
    except:
        print("Liste yüklenemedi. Sayfa yenileniyor...")
        driver.get("https://e-okul.meb.gov.tr/OrtaOgretim/OKL/OOK07003.aspx")
        return "Yüklenemedi"
    else:
        print("Tablo yüklendi.")


# tarayıcı nesnesi oluştur
driver = webdriver.Chrome(settings.driver_path)
driver.maximize_window()
# sayfanın yüklemesini çok beklememesi için
# 20 saniye beklemesini, yoksa hata vermesini belirliyoruz
# hata verdiğinde bu hatayı yakalayıp (login fonksiyonunda)
# sayfanın yenilenmesini veya giriş işlemini tekrar etmesini sağlayacağız
driver.set_page_load_timeout(20)
wait = WebDriverWait(driver, timeout=5, poll_frequency=1)

# Kitap listesini Excel dosyasından verileri al.
liste = load_workbook("E:\kitaplist.xlsx")
sayfa = liste.active
excel = Excel("E:\kitaplist.xlsx", data_only=True)
kitap = excel.get_datas()
del excel


# Mebbis'e giriş yapılır.
login(settings.tc, settings.password)
driver.find_element_by_xpath("//img[@src='images/uygulamaikon/e-okul.png']").click()
driver.find_elements_by_xpath("//a[contains(@title,'E-OKUL')]")[1].click()
# Yeni pencerede açılan E-Okul'a geçiş yapılıyor.
driver.switch_to.window(driver.window_handles[-1])
#e-okul sol menü gelene kadar bekleniyor.
eokul_navbar_is_loaded()

# Ders notu girişi ekranına kadar gerekli menü tıklamaları yapılıyor.
driver.find_element_by_xpath("//span[contains(text(),'İlkokul-Ortaokul Kurum İşlemleri')]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//td[@title='Okuduğu Kitaplar']").click()
time.sleep(0.5)
driver.find_element_by_xpath("//td[@title='Sınıf Kitaplığı Oluşturma']").click()



#sınıf seçimi
driver.find_element_by_xpath("//option[contains(text(),'6. Sınıf-Hafif Zihinsel / A Şubesi')]").click()
driver.find_element_by_xpath("//input[@id='btnListele']").click()

#kitap grubu çocuk kitapları
driver.find_element_by_xpath("//option[@value='4']").click()

#kitap türü seçimi
wait.until(ec.element_to_be_clickable((By.XPATH,"//option[normalize-space()='100 Temel eser']")))
driver.find_element_by_xpath("//option[normalize-space()='100 Temel eser']").click()
time.sleep(5)



