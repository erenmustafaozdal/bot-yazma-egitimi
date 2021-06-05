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
from classes.browser_mat import Browser
from classes.eba_mat import EBA
from classes.excel_mat import Excel
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
eba.login_mebbis(settings.tc, settings.password)

# Sınavlar sayfasına git
driver.get(URL)

# Sınavlar için döngüye gir. Her sınav için aşağıdaki işlemleri yap.
print("-"*50)
exam_count = len(exams)
i = 0
while i < exam_count:
    exam = exams[i]

    try:
        # Sınav oluştur penceresini aç
        eba.wait.until(ec.element_to_be_clickable(
            (By.XPATH, add_exam_btn)
        )).click()

        # açılan pencerenin iframe'ini seç
        # driver.switch_to.frame(iframe_id)
        eba.wait.until(ec.frame_to_be_available_and_switch_to_it(
            (By.ID, iframe_id)
        ))

        # SORU EKLE tuşuna bas
        wait = WebDriverWait(driver, 30)
        wait.until(ec.element_to_be_clickable(
            (By.XPATH, add_question_btn)
        )).click()

        # EBA SORULARI sekmesine tıkla
        eba.wait.until(ec.element_to_be_clickable(
            (By.XPATH, eba_questions)
        )).click()

        # "Okul Türü"nü seç (Ör: İlkokul)
        eba.wait.until(ec.presence_of_element_located(
            (By.XPATH, school.format(exam['Okul Türü']))
        )).click()

        # "Sınıf"ı seç
        eba.wait.until(ec.presence_of_element_located(
            (By.XPATH, classroom.format(exam['Sınıf']))
        )).click()

        # "Ders"i seç
        eba.wait.until(ec.presence_of_element_located(
            (By.XPATH, lesson.format(exam['Ders']))
        )).click()

        # Eğer varsa "Ünite"yi seç
        if exam['Ünite']:
            eba.wait.until(ec.presence_of_element_located(
                (By.XPATH, unit.format(exam['Ünite']))
            )).click()

        # Eğer varsa "Konu"yu seç
        if exam['Konu']:
            eba.wait.until(ec.presence_of_element_located(
                (By.XPATH, subject.format(exam['Konu']))
            )).click()


        # İstenen "Soru Sayısı" kadar soru seçmek için döngüye gir
        selected = 0
        while True:

            try:
                # İstenen "Zorluk Derecesi"ne göre sorular seç
                wait = WebDriverWait(driver, 5)
                add_icons = wait.until(ec.visibility_of_all_elements_located(
                    (By.XPATH, questions.format(exam['Zorluk Derecesi']))
                ))

                # kalan soru adedince ikon üzerinde işlem yap
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
                # İstenen sayıya ulaşmadıysa ve eğer varsa sonraki sayfaya geç
                #  İstenen sayıya ulaştıysa döngüden çık
                try:
                    if selected == exam['Soru Sayısı']:
                        break

                    print(f"Soru sayısı ({exam['Soru Sayısı']}) tamamlanmadı. Sonraki sayfaya geçiliyor.")
                    # sonraki sayfaya geç
                    driver.find_element_by_xpath(next_questions_btn).click()

                    eba.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "mainpreloader")))
                    eba.wait.until(ec.invisibility_of_element((By.CLASS_NAME, "mainpreloader")))

                except:
                    print('Başka sayfa kalmadı.')
                    break

        # Sınav bilgileri bölümüne geç
        driver.find_element_by_xpath(ok_btn).click()

        eba.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "mainpreloader")))
        eba.wait.until(ec.invisibility_of_element((By.CLASS_NAME, "mainpreloader")))

        eba.wait.until(ec.element_to_be_clickable(
            (By.XPATH, next_btn)
        )).click()

        # "Sınav Başlığı"nı yaz
        eba.wait.until(ec.visibility_of_element_located(
            (By.XPATH, exam_name)
        )).send_keys(exam['Sınav Başlığı'])

        # "Zorluk Derecesi"ni seç
        eba.wait.until(ec.presence_of_element_located(
            (By.XPATH, exam_difficulty.format(exam['Zorluk Derecesi']))
        )).click()

        # "Sınıf"ı seç
        eba.wait.until(ec.presence_of_element_located(
            (By.XPATH, exam_classroom.format(exam['Sınıf']))
        )).click()


        # Eğer "Sınav Tipi" seçim kutusu varsa
        #   İstenen tip varsa onu seç
        #   Yoksa rastgele tip seçimi yap
        try:
            wait = WebDriverWait(driver, 1)
            type = exam['Sınav Tipi'] if exam['Sınav Tipi'] != None else ""
            options = wait.until(ec.presence_of_all_elements_located(
                (By.XPATH, exam_type.format(type))
            ))
            option = random.choice(options)
            option.click()
        except:
            pass

        # sınavı kaydet
        driver.find_element_by_id(save_btn_id).click()

        # tekrar ana çerçeveyi seç
        driver.switch_to.default_content()

        # "işleminiz başarı ile gerçekleştirildi." bilgisi gidene kadar bekle
        eba.wait.until(ec.visibility_of_element_located((By.ID, toast_id)))
        eba.wait.until(ec.invisibility_of_element((By.ID, toast_id)))

        i += 1
        print(f"'{exam['Sınıf']} {exam['Ders']}' için sınav oluşturuldu.")
    except Exception as error:
        logger.exception(error)
        driver.refresh()

    print("-"*50)
