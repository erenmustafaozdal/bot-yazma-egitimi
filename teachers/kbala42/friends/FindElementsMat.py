'''
find_elements : Sayfa elemanlarını bulup işlemler yapma
Mehmet Akit Turan

'''

from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By


def goToPage(page):
    driver.get(page)
    driver.maximize_window()
    button = driver.find_element_by_class_name("btn-warning")
    button.click()


def classControl():
    goToPage(page_main)
    # btn btn-labeled btn-warning classlarının kaç tane olduğunu kontrol edelim
    classes = {"btn", "btn-labeled", "btn-warning"}
    for class1 in classes:
        print(f"Sayfada {class1} sınıfından {len(driver.find_elements_by_class_name(class1))} adet eleman var")
        # print(f"Sayfada {class1} sınıfından {len(driver.find_elements(By.CLASS_NAME, class1))} adet eleman var")
    driver.close()


def buttonClick():
    goToPage(page_main)
    button1 = driver.find_element(By.CLASS_NAME, "btn-warning")
    print(f"Düğmenin üzerinde '{button1.text}' yazıyor")
    time.sleep(2)
    driver.close()


def id():
    goToPage(page_akademi)
    form = driver.find_element_by_id("choice_form")
    form1 = driver.find_element(By.ID, "choice_form")
    print(form.text)
    print(form1.size)
    driver.close()


def name():
    goToPage(page_akademi)
    keywords = driver.find_element_by_name("keywords")
    author = driver.find_element(By.NAME, "author")
    print(keywords.get_attribute("content"))
    print(author.get_attribute("content"))
    driver.close()


def link():
    goToPage(page_akademi)
    link = driver.find_element_by_link_text("Teknoloji Akademisi")
    link2 = driver.find_element(By.LINK_TEXT, "Teknoloji Akademisi")
    link.click()
    print(link2)
    driver.close()


def partial_link():
    driver.get("https://istanbulakademi.meb.gov.tr/")
    driver.maximize_window()
    driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")  # bu satır olmadan çalışmıyor
    partial_link = driver.find_element_by_partial_link_text("Hata")
    partial_link.click()
    time.sleep(2)
    driver.close()


def tag():
    goToPage(page_hata)
    tag = driver.find_element_by_tag_name("input")
    tag2 = driver.find_element(By.TAG_NAME, "label")
    tag.send_keys("Mehmet Akif TURAN")
    print(tag2.text)
    time.sleep(2)
    driver.close()


def css_selector():
    goToPage(page_hata)
    email = driver.find_element_by_css_selector("#sender_email")
    phone = driver.find_element(By.CSS_SELECTOR, "#sender_phone")
    email.send_keys("mehmetakif@gmail.com")
    phone.send_keys(5555555555)
    time.sleep(1)
    email.send_keys("ekleme@gmail.com")
    time.sleep(2)
    email.clear()
    email.send_keys("mehmetakif@hotmail.com")
    time.sleep(1)
    driver.close()


def xpath():
    driver.get("https://istanbulakademi.meb.gov.tr/")
    driver.maximize_window()
    driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")  # bu satır olmadan çalışmıyor
    partial_link = driver.find_element_by_partial_link_text("Hata")
    partial_link.click()
    address = driver.find_element_by_xpath('//ul[@class="v-list"]/li[1]')
    print(address.text)
    driver.close()


while True:
    secim = int(input('''
    Chrome BOT Uygulaması
    -------------------------------------------------------
    1 Class Name Kontrolü
    2 Class Name İle Elemana Ulaşma - Düğme Tıklama
    3 Id İle Elemana Ulaşma - Form Metni Yazdırma
    4 Name Özniteliği İle Elemana Ulaşma - Anahtar Kelimeleri ve Yazarı Yazdırma
    5 Bağlantı Metni İle Elemana Ulaşma - Linke Tıklama
    6 Kısmi Bağlantı Metni İle Elemana Ulaşma - Link İçinde Geçen Kelime Vasıtasıyla Tıklama
    7 Etiket Adı İle Elemana Ulaşma - İnput Elemanına Veri Girişi
    8 CSS Seçici İle Elemana Ulaşma - Mail Adresi Girişi
    9 XPath Seçici İle Elemana Ulaşma - Site Adresi Yazdırma
    0 ÇIKIŞ 
    İşlem Seçiniz:

    '''))
    if secim == 0:
        break

    driver = webdriver.Chrome(settings.driver_path)
    page_main = "https://istanbulakademi.meb.gov.tr/"
    page_akademi = "https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615"
    page_hata = "https://istanbulakademi.meb.gov.tr/hata_bildir.php"

    if secim == 1:
        classControl()
    if secim == 2:
        buttonClick()
    if secim == 3:
        id()
    if secim == 4:
        name()
    if secim == 5:
        link()
    if secim == 6:
        partial_link()
    if secim == 7:
        tag()
    if secim == 8:
        css_selector()
    if secim == 9:
        xpath()