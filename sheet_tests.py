"""
ALGORİTMA
- Excel dosyasından yaprak test bilgilerini al
- EBA'ya giriş yap
- Yaprak testler için döngüye gir. Her yaprak test için aşağıdaki işlemleri yap.
    - Yaprak test ekleme sayfasına git
    - "Test Adı"nı yaz
    - "Sınıf"ı seç
    - "Ders"i seç
    - "Dosya"yı yükle
    - "Soru Sayısı"nı yaz
    - "Seçenek Sayısı"nı seç
    - "Cevap Anahtarı"nı aç
    - Her soru için döngüye gir ve doğru şıkları işaretle (Burada bekleme uzun olmalı)
    - Cevap anahtarını kaydet
    - Yaprak testi kaydet
"""
import settings
from classes.browser import Browser
from classes.eba import EBA
from classes.excel import Excel
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# hata yakaladıktan sonra yine de hata hakkında bize mesaj döndürmesi için bu modülü kullanıyoruz
import logging
logger = logging.getLogger()

##### Yaprak testleri oluştururken kullanacağımız seçiciler (XPATH vb.)
# sol menüdeki sınavlar tuşu
exams_menu = "//div[normalize-space()='Sınavlar']"
# sınavlar sayfasındaki yaprak testlerim bağlantısı
sheet_test = "//div[text()='Yaprak Testlerim']"
# yaprak test ekleme sayfasına gönderecek olan tuş
add_sheet_test_btn = "//div[@id='vc-new-button']/div[text()='YAPRAK TEST EKLE']"
# yaprak test adı alanı
test_name = "//input[@placeholder='Testin Adı']"
# sınıf alanı
test_grade = "//select[@name='grade']/option[contains(text(),'{}')]"
# ders alanı
test_course = "//select[@name='course']/option[contains(text(),'{}')]"
# dosya yükleme alanı (<input type="file">)
add_file_id = "paperTestFileButton"
# soru sayısı alanı
question_count = "//input[@name='lastName']"
# seçenek sayısı alanı
option_count = "//label[normalize-space()='{} Seçenekli']/input[@type='radio']"
# cevap anahtarı tuşu
answer_sheet = "//div[contains(text(),'CEVAP ANAHTARI')]"
# cevap anahtarı seçimi yapılacak pencere çerçevesi (iframe)
iframe_id = "utilViewIysPopupIframe"
# cevap anahtarındaki her bir soru tuşu
questions = "//div[contains(@class,'question-row')]"
# cevap anahtarındaki her sorunun içinde bulunan şıklar (A, B, C, D, E)
choice = ".//div[contains(@class,'choice')]/span[contains(text(),'{}')]"
# cevap anahtarını penceresini kapatma/kaydetme "tamam" tuşu
ok_btn_id = "finish-button"
# yaprak testi kaydetme tuşu
save_btn = "//div[contains(text(),'KAYDET')]"

# Excel dosyasından yaprak test bilgilerini al
excel = Excel("./excels/sheet_tests.xlsx")
sheet_tests = excel.get_datas()

##### EXCEL dosyasından aldığımız dictionary türünde bir yaprak test örneği
# {
#     'Cevap Anahtarı': 'A,C,B,C,A,A,B,C',
#     'Ders': 'Matematik',
#     'Dosya': 'C:\\Users\\erenMustafaOzdal\\Google '
#              'Drive\\Development\\Atölyeler\\Bot Yazma Eğitimi '
#              'Atölyesi\\bot-yazma-egitimi\\files\\sheet_tests\\Birer, Onar ve '
#              'Yüzer Ritmik Sayma.pdf',
#     'Seçenek Sayısı': 3,
#     'Soru Sayısı': 8,
#     'Sınıf': '3. Sınıf',
#     'Test Adı': 'Birer, Onar ve Yüzer Ritmik Sayma',
#     'row': 2
# }

# Tarayıcı nesnesini oluştur
browser = Browser(settings.driver_path)
driver = browser.get()

# EBA'ya giriş yap
eba = EBA(driver)
eba.login(settings.tc, settings.password)

# todo: sol menüden Sınavlar'a tıkla


# todo: Yaprak Testlerim'e tıkla


# Yaprak testler için döngüye gir. Her yaprak test için aşağıdaki işlemleri yap.
test_count = len(sheet_tests)
i = 0
while i < test_count:
    test = sheet_tests[i]

    try:
        # todo: Yaprak test ekleme sayfasına git


        # todo: "Test Adı"nı yaz


        # todo: "Sınıf"ı seç


        # todo: "Ders"i seç


        # todo: "Dosya"yı yükle


        # todo: "Soru Sayısı"nı yaz


        # todo: "Seçenek Sayısı"nı seç


        # todo: "Cevap Anahtarı"nı aç


        # todo: açılan pencerenin iframe'ini seç


        # todo: Her soru için döngüye gir ve doğru şıkları işaretle (Burada bekleme uzun olmalı)


        # todo: Cevap anahtarını kaydet


        # todo: tekrar ana çerçeveyi seç


        # todo: Yaprak testi kaydet


        i += 1
    except Exception as error:
        logger.exception(error)
        driver.back()
