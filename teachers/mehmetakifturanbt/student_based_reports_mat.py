"""
ALGORİTMA
- Ekran görüntüleri için yoksa klasörü oluştur ("./images/student-based-reports")
- Excel dosyası eğer yoksa oluştur
- EBA'ya giriş yap
    ---------------------
    Karşılaşılan Sorunlar
    ---------------------
    - "EBA yükleniyor" mesajının gitmemesi (her sayfada karşılaşılabiliyor)
    - Sayfanın görünen kısmı yüklense bile, sekme başlığında yükleniyor resmi
        dönmeye devam ediyor ve sayfa yüklenmesi bitmiyor
- Raporlar > Çalışma Raporları > Öğrenci Bazlı sayfasına git
- Tablodaki öğrencileri gez. Her öğrenci için;
    - Son 10 çalışmayı kontrol et
    - Tamamlama ortalamasını hesap et
    - Performans ortalamasını hesap et
    - Excel' kaydet
"""
from selenium import webdriver
import settings
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


# tarayıcı nesnesi oluştur
driver = webdriver.Chrome(settings.driver_path)
driver.maximize_window()
# sayfanın yüklemesini çok beklememesi için 10 saniye beklemesini, yoksa hata vermesini belirliyoruz
driver.set_page_load_timeout(10)


# EBA'a giriş yap
driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()
driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)
driver.find_element_by_xpath("//input[@id='egpField']").send_keys(settings.password)
driver.find_element_by_css_selector("input[name='submitButton']").click()


# ÖNEMLİ NOT: E-Devlet Girişinde Tek Kullanımlık Şifre Kullandığım İçin Kod Eklemesi Yaptım
try:
    tek_kullanimlik_sifre = input("Tek Kullanımlık Şifrenizi Giriniz: ")
    driver.find_element_by_xpath("//input[@id='otpDogrulamaKodu']").send_keys(tek_kullanimlik_sifre)
    driver.find_element_by_css_selector("input[name='submitButton']").click()
except:
    #tıklama sonrası sayfa 10 saniyede yüklenemedi ise
    print("Sayfa 10 saniyede yüklenemedi. Sayfayı yeniliyorum!")
    driver.refresh()



# SORUN ÇÖZÜMÜ: "EBA yükleniyor" mesajının gitmemesi (her sayfada karşılaşılabiliyor)
# "EBA Yükleniyor" animasyonu gidene kadar sayfayı yenileme döngüsü
while True:
    eba_wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
    try:
        eba_wait.until(ec.invisibility_of_element((By.ID, "generalPreloader"))) # Eba'nın yükleniyor animasyonu
        break # gizlendi ise döngüyü bitir
    except:
        print("Çok bekledi. Sayfa yenileniyor...")
        driver.refresh()


wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
# //div[@class='vc-lm-item-title '][normalize-space()='Raporlar']
# //div[@id='3e8510bd-2428-4fa8-12e1-42ea125d8ff2'] ID SÜREKLİ DEĞİŞTİĞİ İÇİN KULLANAMIYORUZ!! Önce bunu denemiştik.
# time.sleep(30)
wait.until(ec.element_to_be_clickable(
        (By.XPATH, "//div[@class='vc-lm-item-title '][normalize-space()='Raporlar']"))
).click()


# tarayıcı kapat
time.sleep(2)
driver.close()
