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


# SORUN ÇÖZÜMÜ: "EBA yükleniyor" mesajının gitmemesi
# ÇÖZÜM: Sol menü yüklenene kadar bekle
def left_menu_is_loaded():
    try:
        wait.until(ec.visibility_of_element_located((By.ID, "vc-treeleftmenu")))
    except:
        print("Menünün yüklenmesi için çok bekledi. Sayfa yenileniyor...")
        driver.refresh()
        left_menu_is_loaded()


# EBA'ya giriş yapma işlemini gerçekleştiren fonksiyon
def login(tc, password):
    # Öğretmen girişi sayfasına git
    driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")

    # Eğer daha önceden giriş yapıldı ise fonksiyondan çık
    # 'VCollabPlayer' ifadesi EBA'ya giriş yaptıktan sonra
    # her URL'de olan ortak bir değerdir.
    # Geçerli URL içinde varlığı sorgulanarak,
    # giriş yapılıp yapılmadığı tespit edilir
    if 'VCollabPlayer' in driver.current_url:
        return

    # E-Devlet girişi tuşuna bas ve E-Devlet girişi sayfasına git
    driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()

    # TC ve şifre yaz
    driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)
    driver.find_element_by_id("egpField").send_keys(settings.password)

    # E-Devlet giriş formunu gönder.
    # Eğer sayfa yüklenemez veya başka bir hata alınırsa
    # giriş işlemini tekrar et.
    try:
        driver.find_element_by_xpath("//input[@name='submitButton']").click()
    except:
        print("Sayfa 10 saniyede yüklenemedi. Sayfa yenileniyor...")
        login(tc, password)
    else:
        # Eğer başarılı bir şekilde EBA'ya giriş
        # yapıldı ise sol menünün yüklenmesini bekle
        left_menu_is_loaded()


# tarayıcı nesnesi oluştur
driver = webdriver.Chrome(settings.driver_path)
driver.maximize_window()
# sayfanın yüklemesini çok beklememesi için
# 10 saniye beklemesini, yoksa hata vermesini belirliyoruz
driver.set_page_load_timeout(10)


# Çeşitli sayfa elemanlarını beklemek için
# WebDriverWait bekleme nesnesi oluşturulur
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)


# EBA'ya giriş yapılır
login(settings.tc, settings.password)


# Sol menüden 'Raporlar' menüsüne tıkla
reports_menu = wait.until(ec.element_to_be_clickable(
    (By.XPATH, "//div[@class='vc-lm-item-title '][normalize-space()='Raporlar']")
))
reports_menu.click()




# tarayıcı kapat
time.sleep(2)
driver.close()
