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
import  time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# SORUN ÇÖZÜMÜ: "EBA yükleniyor" mesajının gitmemesi (her sayfada karşılaşılabiliyor)
# ÇÖZÜM: Sol menü yüklenene kadar bekle
# Bunu için sol menünün yüklenip yüklenmediğini kontrol edecek bir fonksiyon tanımlıyoruz
def LeftMenuIsLoaded():
    try:
        # ID'si vc-treeleftmenu olan nesne yüklenene kadar bekle
        wait.until(ec.visibility_of_element_located((By.ID,"vc-treeleftmenu")))
    except: # 10 saniye bekledikten sonra bir hata alırsa
        print("Menünün yüklenmesi için çok bekledi. Sayfa yenileniyor...")# yazısını yazacak
        driver.refresh() # sayfayı yeniden yükleyecek
        LeftMenuIsLoaded() #yenilenebilir bir fonksiyon olarak kendini tekrar çağıracak
    # EBA yükleninceye kadar sonsuz döngüye sokuyoruz

# EBA'ya giriş işlemini gerçekleştiren fonksiyonu yazıyoruz
def login(tc, password):
    # Öğretmen giriş sayfasına gidiyoruz
    driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")

    # Eğer daha önce giriş yapıldı ise fonksiyondan çık
    # Daha öncede giriş EBA'ya giriş yapılmış ama halen aynı profilden EBA'dan çıkılmamışsa
    # EBA aynı profile tekrar yollar. Burada tekrar giriş yapma işlemini apmamak için bunu sorguluyoruz
    # 'VCollabPlayer' ifadesi EBA'ya giriş yaptıktan sonra her URL^de ortak bir değerdir,
    #Geçerli URL içinde varlığı sorgulanarak, giriş yapılıp yapılmadığı kontrol edilir
    if 'VCollabPlayer' in driver.current_url: # current_url'de VCOllabPlayer varsa fonksiyondan çık
        return

    # 'edevlet girişi' başlıklı tuşa basıyoruz ve E-Devlet giriş sayfasına gidiyoruz
    driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()

    # TC nosunu "#tridField" ccs selectörü belilenen girişe yazıdıryoruz
    driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)
    # E-devlet Şifresini "gpField" id ile belirlenen girişe yazıdıryoruz
    driver.find_element_by_id("egpField").send_keys(settings.password)

    # E-devlete giriş formunu gönderiyoruz
    # Eğer sayfa yüklenemez veya başka bir hata alınırsa giriş işlemini tekrar ettiriyoruz
    try:
        # e-devlet butonu dallanma elmanını selector ile tespit edip e-devlet sayfasına gidiyoruz
        driver.find_element_by_xpath("//input[@name='submitButton']").click()
    except:
        print("Sayfa 10 saniyede yüklenmedi.Sayfa yenileniyor...")
        # Sayfa yüklenmemişse fonksiyon kendini tekrar çağırıyor
        login(tc,password)
    # Eğer try bölümünde bir hata almazsa buraya geçiyor
    else:
        # Eğer başarılı bir şekilde EBA'ya giriş
        #yapıldı ise sol menünün yüklenmesini bekle
        LeftMenuIsLoaded()

#Tablo satırlarının görünmesini bekleyen fonksiyon
def TableIsLoaded():
    try: # Bütün elemanlar görünür oluncaya kadar bekle
        wait.until(ec.visibility_of_all_elements_located(
            (By.XPATH,"//div[@class= 'body-container ']/div[@role= 'row']")
        ))
    except: # hata varsa
        print("Tablo yüklenemedi. Sayfa yenileniyor...")
        driver.refresh()
        TableIsLoaded() # Sayfa yüklemedi ise özyinele


# TODO: Ekran örüntüleri için yoksa kalsörü oluştur
# "./images/student-based-reports"

# TODO: Excel dosyası eğer yoksa oluştur

# tarayıcı nesnesini oluşturuyoruz ve değişkene atıyoruz
driver = webdriver.Chrome(settings.driver_path)
# sayfayı maksimize yapıyoruz
driver.maximize_window()
#sayfanın yüklenmesini çok beklememek için
#20 saniye beklemesini yoksa hata vermesini elirliyoruz
#Sayfanı yüklenmesini bekletiyoruz
driver.set_page_load_timeout(20)

#Çeşitli sayfa elemanlarını beklemek için;
# WebDrverWait sınıfından driver sayfasında 10 sn bekleyen 1 sık aralıkla kontrol yapan wait nesnesi üretiyoruz
# Elemanların yüklenmesini bekletiyoruz
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

# EBA'ya giriş yapılır
login(settings.tc,settings.password)

# sol menüden "Raporlar menüsü
reportsMenu=wait.until(ec.element_to_be_clickable(
    (By.XPATH, "//div[@class='vc-lm-item-title '][normalize-space()='Raporlar']")
))

reportsMenu.click()

#'Raporlar' sayfasında 'Çalışma Raporları' bağlantısına tıklatıyoruz.
# Çalışma Raporları butonu tıklanabilir oluncaya kadar beletiyoruz
workReports = wait.until(ec.element_to_be_clickable(
    (By.XPATH,"//div[text()='Çalışma Raporları']")
))
workReports.click()

# Bu sayfanın yüklendiğinden emin olmak için tablo satırları yüklenene kadar bekle
TableIsLoaded() # foksiyonu çağırıyoruz


# TODO: 'Çalışma Raporları' sayfasında 'ÖĞRENCİ BAZLI' bağlantısına tıkla.
# Bu sayfanın yüklendiğinden emin olmak için tablo satırları yüklenene kadar bekle.
# //div[text()='ÖĞRENCİ BAZLI']

# TODO: Öğrencilerin olduğu tablo satırlarını al

# TODO: Öğrencilerin satırlarını döngüye al.
# 1. Öğrencinin adını al.
# 2. Son 10 çalışmanın tamamlanma yüzdelerini bir diziye aktar.
# 3. Son 10 çalışmanın performanslarını bir diziye aktar.
# 4. örtlimalfli tamamlamayı hesap et.
# 5. Ortalama performansı hesap et.
# 6. Ekran görüntüsünü kaydet.
# 7. Verileri ekrana yazdır.
# 8. Verileri Excel dosyasına yazdır.

# 2 saniye bekletiyoruz
time.sleep(2)

# Sayfayı kapatıyoruz
driver.close()