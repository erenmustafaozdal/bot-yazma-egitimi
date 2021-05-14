from selenium import webdriver
import settings
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import os
# Öncelikle openpyxl paketi yüklenir: pip install openpyxl
#from openpyxl import Workbook, load_workbook
#from datetime import datetime

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

#ekran görüntüleri için yoksa klasörü oluştur.
img_dir = "./images/student-based-reports"  #değişkene atadık aşağıda kullanmak için
if not os.path.exists(img_dir):
    os.mkdir(img_dir)


# Tarayıcı nesnesi oluştur
driver = webdriver.Chrome(settings.driver_path)
driver.maximize_window()
# sayfanın yüklenmesini çok beklmemek 10 saniye beklemesini yoksa hata vermesini belirliyoruz.
driver.set_page_load_timeout(10)

#sayfa elemanlarını beklemek için WebDriverWait bekleme nesnesi oluşturulur.
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

#Ebaya giriş yap
login(settings.tc, settings.password)

#sol menüden raporlar menüsüne tıkla
reports_menu = wait.until(ec.element_to_be_clickable(
    (By.XPATH, "//div[@class='vc-lm-item-title '][normalize-space()='Raporlar']")
))
reports_menu.click()

#Raporlar menüsündeki Çalışma raporlarına tıkla

work_reports = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[text()='Çalışma Raporları']")))
work_reports.click()

#Çalışma raporları sayfasının yüklendiğinden emin olmak için tablo satırları yüklenene kadar bekle
table_is_loaded()

#öğrenci bazlı bağlantısına tıkla
student_based_link = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[text()= 'ÖĞRENCİ BAZLI']")))
student_based_link.click()
#öğrenci bazlı sayfanın yüklendiğine emin olmak için tablo satırları yüklenene kadar bekle
students = table_is_loaded()

#öğrenci bazlı sayfaya girdik ve tek tek öğrencilerin çalışmalarını kontrol eedeceğiz

#öğrencilerin sayısınca for döngüsüne sok, öğrencilerin sayısını al
student_count = len(students) #öğrenci sayısını aldık
for student_i in range(student_count): #öğrenci sayısınca döngüye gir
    students = table_is_loaded() #öğrencileri tekrar alması için(listeyi baştan görmesi için)
    students[student_i].click() #bir sonraki öğrenciye tıklatmak için
    # Not: table is loaded fonksiyonunu farklı sayfalarda kullanabildik
    works = table_is_loaded() #öğrenci bazlı sayfada çalışma satırlarını al
    #öğrenci adını al,yaz
    student_name = driver.find_element_by_xpath("//div[@class='vc-font-size-x-large m-l-sm ng-binding']").text


    # çalışma satırlarını gez ve hesaplamalar yap
    completes = []  # tamamlama yüzdeleri bu listeye atılarak hesaplanacak
    performances = []  # performanslar bu listeye atılarak hesaplanacak

    # eğer bütün çalışmalar gezilecekse "for work in works:" şeklinde
    # döngü oluşturulabilir. Bu örnekte son 10 çalışma kontrol ediliyor.
    for work_i in range(10):
        # tamamlanma alınır
        complete = works[work_i].find_element_by_xpath(".//div[@id='vcProgressBar']//span").text
        completes.append(int(complete.replace("%", ""))) #başındaki yüzdeyi boşlukla değiştir

        # performans alınır
        performance = works[work_i].find_element_by_xpath(".//div[@id='multiColouredProgress']//span").text
        if performance != '-': #performans çizgiye eşit değilse yani boş değilse
            performances.append(int(performance))

    # tamamlama ortalamasını alalım
    complete_avg = sum(completes) / len(completes)
    # performans ortalamasını alalım
    performance_avg = "performans yok"  # varsayılan bir değer belirliyoruz.
    if len(performances) > 0:  # eğer performans değeri varsa ortlama hesap edilir
            performance_avg = sum(performances) / len(performances)

    # ekran görüntüsü alalım
    # Ekran Görüntüsü Adı Formatı: 20210508-Öğrenci Adı.png
    img_path = f"{img_dir}/{student_name}.png"
    driver.find_element_by_xpath("//div[@class='vc-layout-view-content-padding']").screenshot(img_path)

    # ekrana yazdır
    print("*" * 50)
    print("Öğrenci: ", student_name)
    print("--- Tamamlama:", complete_avg)
    print("--- Performans:", performance_avg)


    break
    # sonraki satırdaki öğrenciye geçmek için
    # bir önceki sayfadaki tabloya geri dönüyoruz
    driver.back()



