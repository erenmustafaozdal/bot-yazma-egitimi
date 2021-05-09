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
import os
# Öncelikle openpyxl paketi yüklenir: pip install openpyxl
from openpyxl import Workbook, load_workbook
from datetime import datetime


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
        print("Sayfa 20 saniyede yüklenemedi. Sayfa yenileniyor...")
        login(tc, password)
    else:
        # Eğer başarılı bir şekilde EBA'ya giriş
        # yapıldı ise sol menünün yüklenmesini bekle
        left_menu_is_loaded()


# Tablo satırlarının görünmesini bekleyen fonksiyon
def table_is_loaded():
    try:
        return wait.until(ec.visibility_of_all_elements_located(
            (By.XPATH, "//div[@class='body-container']/div[@role='row']")
        ))
    except:
        print("Tablo yüklenemedi. Sayfa yenileniyor...")
        driver.refresh()
        return table_is_loaded()


# Ekran görüntüleri için yoksa klasörü oluştur
#  "./images/student-based-reports"
img_dir = "./images/student-based-reports"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

# Excel dosyası eğer yoksa oluştur
xl_path = "./excels/student-based_reports.xlsx"
if not os.path.exists(xl_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Öğrenci Bazlı Çalışma Raporları"
    ws.append(["Tarih", "Öğrenci", "Tamamlama", "Performans", "Ekran Görüntüsü"])
else:
    wb = load_workbook(xl_path)
    ws = wb["Öğrenci Bazlı Çalışma Raporları"]


# tarayıcı nesnesi oluştur
driver = webdriver.Chrome(settings.driver_path)
driver.maximize_window()
# sayfanın yüklemesini çok beklememesi için
# 20 saniye beklemesini, yoksa hata vermesini belirliyoruz
# hata verdiğinde bu hatayı yakalayıp (login fonksiyonunda)
# sayfanın yenilenmesini veya giriş işlemini tekrar etmesini sağlayacağız
driver.set_page_load_timeout(20)


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


# 'Raporlar' sayfasında 'Çalışma Raporları' bağlantısına tıkla.
work_reports = wait.until(ec.element_to_be_clickable(
    (By.XPATH, "//div[text()='Çalışma Raporları']")
))
work_reports.click()

# Bu sayfanın yüklendiğinden emin olmak için tablo satırları yüklenene kadar bekle
table_is_loaded()


# 'Çalışma Raporları' sayfasında 'ÖĞRENCİ BAZLI' bağlantısına tıkla.
student_based_link = wait.until(ec.element_to_be_clickable(
    (By.XPATH, "//div[text()='ÖĞRENCİ BAZLI']")
))
student_based_link.click()

# Bu sayfanın yüklendiğinden emin olmak için tablo satırları yüklenene kadar bekle.
# Öğrencilerin olduğu tablo satırlarını al
students = table_is_loaded()


# Öğrencilerin satırlarını döngüye al.
# 1. Öğrencinin adını al.
# 2. Son 10 çalışmanın tamamlanma yüzdelerini bir diziye aktar.
# 3. Son 10 çalışmanın performanslarını bir diziye aktar.
# 4. Ortamala tamamlamayı hesap et.
# 5. Ortalama performansı hesap et.
# 6. Ekran görüntüsünü kaydet.
# 7. Verileri ekrana yazdır.
# TODO: 8. Verileri Excel dosyasına yazdır.
student_count = len(students)

# Günün tarihini al
date = datetime.today()
# Excel'de yazılmış en son satırı al
last_row = ws.max_row
for student_i in range(student_count):
    # Sayfa her yenilendiğinde elemanları baştan oluşturulur.
    # Yukarıda "students" değişkenine satırlar aktarılsa bile;
    # ilk öğrenci kontrol edilip, döngünün en altında
    # önceki sayfaya geri döndüğünde; sonraki öğrencinin satırı
    # yeniden oluşturulduğu için tıklama yapılamıyordu.
    # Bu sebeple döngü her döndüğünde satırlar tekrar alınır ve sıradaki satır tıklanır.
    students = table_is_loaded()
    students[student_i].click()

    # çalışma satırlarını al
    works = table_is_loaded()

    student_name = driver.find_element_by_xpath("//div[@class='vc-font-size-x-large m-l-sm ng-binding']").text

    # çalışma satırlarını gez ve hesaplamalar yap
    completes = []  # tamamlama yüzdeleri bu listeye atılarak hesaplanacak
    performances = []  # performanslar bu listeye atılarak hesaplanacak

    # eğer bütün çalışmalar gezilecekse "for work in works:" şeklinde
    # döngü oluşturulabilir. Bu örnekte son 10 çalışma kontrol ediliyor.
    for work_i in range(10):
        # tamamlanma alınır
        complete = works[work_i].find_element_by_xpath(".//div[@id='vcProgressBar']//span").text
        completes.append(int(complete.replace("%", "")))

        # performans alınır
        performance = works[work_i].find_element_by_xpath(".//div[@id='multiColouredProgress']//span").text
        if performance != '-':
            performances.append(int(performance))

    # tamamlama ortalamasını alalım
    complete_avg = sum(completes) / len(completes)
    # performans ortalamasını alalım
    performance_avg = "performans yok"  # varsayılan bir değer belirliyoruz.
    if len(performances) > 0:  # eğer performans değeri varsa ortlama hesap edilir
        performance_avg = sum(performances) / len(performances)

    # ekran görüntüsü alalım
    # Ekran Görüntüsü Adı Formatı: 20210508-Öğrenci Adı.png
    img_path = f"{img_dir}/{date.strftime('%Y%m%d')}-{student_name}.png"
    driver.find_element_by_xpath("//div[@class='vc-layout-view-content-padding']").screenshot(img_path)

    # ekrana yazdır
    print("*"*50)
    print("Öğrenci: ", student_name)
    print("--- Tamamlama:", complete_avg)
    print("--- Performans:", performance_avg)

    # Excel'e yazdır
    # (last_row = 1) + (student_i = 0) + 1
    row = last_row + student_i + 1
    ws[f"A{row}"] = date
    ws[f"A{row}"].number_format = "d mmmm yyyy, dddd"
    ws[f"B{row}"] = student_name
    ws[f"C{row}"] = complete_avg
    ws[f"D{row}"] = performance_avg
    # =KÖPRÜ("../images/student-based-reports/Ekran Görüntüsü.png";"Görüntü")
    ws[f"E{row}"] = f'=HYPERLINK(".{img_path}", "Görüntü")'

    # sonraki satırdaki öğrenciye geçmek için
    # bir önceki sayfadaki tabloya geri dönüyoruz
    driver.back()


# tarayıcı kapat
time.sleep(2)
driver.close()

# Excel dosyasını kaydet ve kapat
wb.save(xl_path)
wb.close()
