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
# işlem bilgisi baloncuğu
toast_id = "toast-container"

# Excel dosyasından yaprak test bilgilerini al
excel = Excel("./excels/sheet_tests.xlsx")
sheet_tests = excel.get_datas()
del excel

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

# sol menüden Sınavlar'a tıkla
eba.wait.until(ec.element_to_be_clickable(
    (By.XPATH, exams_menu)
)).click()

# Yaprak Testlerim'e tıkla
eba.wait.until(ec.element_to_be_clickable(
    (By.XPATH, sheet_test)
)).click()

# Yaprak testler için döngüye gir. Her yaprak test için aşağıdaki işlemleri yap.
test_count = len(sheet_tests)
i = 0
while i < test_count:
    test = sheet_tests[i]

    try:
        # Yaprak test ekleme sayfasına git
        eba.wait.until(ec.element_to_be_clickable(
            (By.XPATH, add_sheet_test_btn)
        )).click()

        # "Test Adı"nı yaz
        eba.wait.until(ec.visibility_of_element_located(
            (By.XPATH, test_name)
        )).send_keys(test['Test Adı'])

        # "Sınıf"ı seç
        eba.wait.until(ec.presence_of_element_located(
            (By.XPATH, test_grade.format(test['Sınıf']))
        )).click()

        # "Ders"i seç
        eba.wait.until(ec.presence_of_element_located(
            (By.XPATH, test_course.format(test['Ders']))
        )).click()

        # "Dosya"yı yükle
        driver.find_element_by_id(add_file_id).send_keys(test['Dosya'])

        # "Soru Sayısı"nı yaz
        eba.wait.until(ec.visibility_of_element_located(
            (By.XPATH, question_count)
        )).send_keys(test['Soru Sayısı'])

        # "Seçenek Sayısı"nı seç
        driver.find_element_by_xpath(
            option_count.format(test['Seçenek Sayısı'])
        ).click()

        # "Cevap Anahtarı"nı aç
        driver.find_element_by_xpath(answer_sheet).click()

        # açılan pencerenin iframe'ini seç
        # driver.switch_to.frame(iframe_id)
        eba.wait.until(ec.frame_to_be_available_and_switch_to_it(
            (By.ID, iframe_id)
        ))

        # Her soru için döngüye gir ve doğru şıkları işaretle (Burada bekleme uzun olmalı)
        wait = WebDriverWait(driver, 30)
        question_elements = wait.until(ec.visibility_of_all_elements_located(
            (By.XPATH, questions)
        ))
        answers = test['Cevap Anahtarı'].split(',')
        for index, question in enumerate(question_elements):
            if index != 0:
                question.click()

            question.find_element_by_xpath(choice.format(answers[index])).click()

        # Cevap anahtarını kaydet
        driver.find_element_by_id(ok_btn_id).click()

        # tekrar ana çerçeveyi seç
        driver.switch_to.default_content()

        # Yaprak testi kaydet
        driver.find_element_by_xpath(save_btn).click()

        #  "yaprak testiniz başarıyla eklendi" bilgisi gidene kadar bekle
        # if i == test_count - 1:  # son test tam kaydedilmesi için
        eba.wait.until(ec.visibility_of_element_located((By.ID, toast_id)))
        eba.wait.until(ec.invisibility_of_element((By.ID, toast_id)))

        i += 1
        print(f"'{test['Test Adı']}' yaprak testi kaydedildi.")
    except Exception as error:
        logger.exception(error)
        driver.back()
