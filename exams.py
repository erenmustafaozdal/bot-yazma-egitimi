"""
ALGORİTMA
- Excel dosyasından sınav bilgilerini al
- EBA'ya giriş yap
- Sınavlar için döngüye gir. Her sınav için aşağıdaki işlemleri yap.
    - Sınav oluştur penceresini aç
    - SORU EKLE tuşuna bas (Burada bekleme uzun olmalı)
    - EBA SORULARI sekmesine tıkla
    - "Okul Türü"nü seç (Ör: İlkokul)
    - "Sınıf"ı seç
    - "Ders"i seç
    - Eğer varsa "Ünite"yi seç
    - Eğer varsa "Konu"yu seç
    - İstenen "Soru Sayısı" kadar soru seçmek için döngüye gir
        - İstenen "Zorluk Derecesi"ne göre sorular seç
        - İstenen sayıya ulaşmadıysa ve eğer varsa sonraki sayfaya geç
        - İstenen sayıya ulaştıysa döngüden çık
    - Sınav bilgileri bölümüne geç
    - "Sınav Başlığı"nı yaz
    - "Zorluk Derecesi"ni seç
    - "Sınıf"ı seç
    - Eğer "Sınav Tipi" seçim kutusu varsa
        - İstenen tip varsa onu seç
        - Yoksa rastgele tip seçimi yap
"""
import settings
from classes.browser import Browser
from classes.eba import EBA
from classes.excel import Excel
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import random

# hata yakaladıktan sonra yine de hata hakkında bize mesaj döndürmesi için bu modülü kullanıyoruz
import logging
logger = logging.getLogger()

##### Sınavları oluştururken kullanacağımız seçiciler (XPATH vb.)
# sınavlar sayfası adresi
URL = "https://ders.eba.gov.tr/ders/proxy/VCollabPlayer_v0.0.817/index.html#/main/iysExams?scope=mine&pageNumber=1&pageSize=24&sortField=createdate&sortDirection=desc"
# sınav oluşturma tuşu
add_exam_btn = "//div[@id='vc-new-button']/div[text()='SINAV OLUŞTUR']"
# sınav oluşturulacak pencere çerçevesi (iframe)
iframe_id = "utilViewIysPopupIframe"
# soru ekle tuşu
add_question_btn = "//span[text()='SORU EKLE']"
# eba soruları tuşu
eba_questions = "//div[@type='all']"
# okul alanı
school = "(//div[@class='search-navigation']//select)[1]/option[text()='{}']"
# sınıf alanı
classroom = "(//div[@class='search-navigation']//select)[2]/option[text()='{}']"
# ders alanı
lesson = "(//div[@class='search-navigation']//select)[3]/option[text()='{}']"
# ünite alanı
unit = "(//div[@class='search-navigation']//select)[4]/option[text()='{}']"
# konu alanı
subject = "(//div[@class='search-navigation']//select)[5]/option[text()='{}']"
# sorular (Kolay, Orta, Zor, Kategorilendirilmemiş)
questions = "//section[@id='question-section']//span[text()='{}']/preceding-sibling::i"
# sonraki sorular tuşu
next_questions_btn = "//a[normalize-space()='Sonraki']"
# tamam tuşu
ok_btn = "//span[text()='Tamam']"
# sınav bilgilerinde sonraki tuşu
next_btn = "//span[text()='Sonraki']"
# sınav başlığı alanı
exam_name = "//div[@config-type='e_name']//input"
# sınav zorluğu alanı
exam_difficulty = "//div[@config-type='e_difficulty']//select/option[text()='{}']"
# sınav sınıfı alanı
exam_classroom = "//div[@config-type='e_classroom']//select/option[text()='{}']"
# sınav tipi alanı
exam_type = "//div[@config-type='e_type']//select/option[@value!=-1][starts-with(text(),'{}')]"
# kaydet tuşu
save_btn_id = "okButton"
# işlem bilgisi baloncuğu
toast_id = "toast-container"

# Excel dosyasından yaprak test bilgilerini al
excel = Excel("./excels/exams.xlsx")
exams = excel.get_datas()
del excel

##### EXCEL dosyasından aldığımız dictionary türünde bir sınav örneği
# {
#     'Ders': 'Matematik',
#     'Konu': 'Doğal Sayılarla Toplama İşlemi – 2',
#     'Okul Türü': 'İlkokul',
#     'Soru Sayısı': 3,
#     'Sınav Başlığı': '4. Sınıf Matematik - Doğal Sayılarla Toplama İşlemi – 2 (Kolay)',
#     'Sınav Tipi': 'Konu Testi',
#     'Sınıf': '4. Sınıf',
#     'Zorluk Derecesi': 'Kolay',
#     'row': 2,
#     'Ünite': '2. Ünite'
# }

# Tarayıcı nesnesini oluştur
browser = Browser(settings.driver_path)
driver = browser.get()

# EBA'ya giriş yap
eba = EBA(driver)
eba.login(settings.tc, settings.password)

# Sınavlar sayfasına git
driver.get(URL)

# Sınavlar için döngüye gir. Her sınav için aşağıdaki işlemleri yap.
print("-"*50)
exam_count = len(exams)
i = 0
while i < exam_count:
    exam = exams[i]

    try:
        # todo: Sınav oluştur penceresini aç


        # todo: açılan pencerenin iframe'ini seç


        # todo: SORU EKLE tuşuna bas


        # todo: EBA SORULARI sekmesine tıkla


        # todo: "Okul Türü"nü seç (Ör: İlkokul)


        # todo: "Sınıf"ı seç


        # todo: "Ders"i seç


        # todo: Eğer varsa "Ünite"yi seç


        # todo: Eğer varsa "Konu"yu seç


        # todo: İstenen "Soru Sayısı" kadar soru seçmek için döngüye gir
        selected = 0
        while True:

            try:
                # todo: İstenen "Zorluk Derecesi"ne göre sorular seç
                wait = WebDriverWait(driver, 5)
                add_icons = []

                # todo: kalan soru adedince ikon üzerinde işlem yap
                #  ÖR: add_icons[:(5-2)]
                #      -> 2 adet daha önce seçilmiş
                #      -> kalan 3 seçim için listenin başındaki ilk 3 elemanı döndür
                for icon in add_icons[:(exam['Soru Sayısı']-selected)]:
                    icon.click()
                    selected += 1
                    print(f"{selected}./{exam['Soru Sayısı']} soru seçildi.")

            except:
                pass
            finally:
                # todo: İstenen sayıya ulaşmadıysa ve eğer varsa sonraki sayfaya geç
                #  İstenen sayıya ulaştıysa döngüden çık
                try:
                    if selected == exam['Soru Sayısı']:
                        break

                    print(f"Soru sayısı ({exam['Soru Sayısı']}) tamamlanmadı. Sonraki sayfaya geçiliyor.")
                    # todo: sonraki sayfaya geç


                except:
                    print('Başka sayfa kalmadı.')
                    break

        # todo: Sınav bilgileri bölümüne geç


        # todo: "Sınav Başlığı"nı yaz


        # todo: "Zorluk Derecesi"ni seç


        # todo: "Sınıf"ı seç


        # todo: Eğer "Sınav Tipi" seçim kutusu varsa
        #   İstenen tip varsa onu seç
        #   Yoksa rastgele tip seçimi yap
        try:
            pass
        except:
            pass

        # todo: sınavı kaydet


        # todo: tekrar ana çerçeveyi seç


        # todo: "işleminiz başarı ile gerçekleştirildi." bilgisi gidene kadar bekle


        i += 1
        print(f"'{exam['Sınıf']} {exam['Ders']}' için sınav oluşturuldu.")
    except Exception as error:
        logger.exception(error)
        driver.refresh()

    print("-"*50)
