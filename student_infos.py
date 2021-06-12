"""
ALGORİTMA
- Excel dosyasından öğrenci bilgilerini al
- Mebbis'e giriş yap
- E-okul'a git
- Öğrenci İşlemleri sayfasına git
- Öğrenciler için döngüye gir. Her öğrenci için aşağıdaki işlemleri yap.
    - Öğrenci numarası ile arama yap
    - Öğrenci genel bilgilerini güncelle
    - Kaydet
"""
import settings
from classes.browser import Browser
from classes.eokul import EOKUL
from classes.excel import Excel
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

# hata yakaladıktan sonra yine de hata hakkında bize mesaj döndürmesi için bu modülü kullanıyoruz
import logging
logger = logging.getLogger()

##### Öğrenci bilgilerini güncellerken kullanacağımız seçiciler (XPATH vb.)
# Öğrenci İşlemleri menüsü
students_menu_id = "mdlIOO"
# Öğrenci arama alanı
student_search_id = "OGRMenu1_txtTC"
# Öğrenci arama tuşu
student_search_btn_id = "OGRMenu1_btnAra"
# Genel bilgiler sol menüsü
general_info = "//td[@title='Öğrenci Genel Bilgileri']"
# "Kiminle oturuyor?" seçim kutusu
live_with = "//select[@id='ddlKiminleOturuyor']/option[contains(text(),'{}')]"
# "Oturduğu ev kira mı?" seçim kutusu
house_rented = "//select[@id='ddlEvKirami']/option[contains(text(),'{}')]"
# "Kendi odası var mı?" seçim kutusu
own_room = "//select[@id='ddlOdasiVarmi']/option[contains(text(),'{}')]"
# "Boy" alanı
student_length_id = "txtBoy"
# "Kilo" alanı
student_weight_id = "txtKilo"
# "Kardeş sayısı" alanı
siblings_number_id = "txtKardesSayisi"
# Kaydet tuşu
save_btn = "//img[@alt='Kaydet']"

# Excel dosyasından öğrenci bilgilerini al
# excel = Excel("C:\\Users\\erenMustafaOzdal\\Downloads\\student_infos_real.xlsx")
excel = Excel("./excels/student_infos.xlsx")
students = excel.get_datas()
del excel

##### EXCEL dosyasından aldığımız dictionary türünde bir öğrenci örneği
# {
#     'Boy': 110,
#     'Kardeş sayısı': 2,
#     'Kendi odası var mı?': 'Var',
#     'Kilo': 33,
#     'Kiminle oturuyor?': 'Velisiyle',
#     'Lütfen öğrenci numarasını yazınız': 2003,
#     'Oturduğu ev kira mı?': 'Kendilerinin',
#     'Zaman damgası': datetime.datetime(2021, 6, 4, 6, 46, 51, 529000),
#     'row': 2
# }

# Tarayıcı nesnesini oluştur
browser = Browser(settings.driver_path)
driver = browser.get()

# Mebbis'e giriş yap ve E-okul'a git
eokul = EOKUL(driver)
eokul.login(settings.tc, settings.password)

# Öğrenci İşlemleri sayfasına git
eokul.wait.until(ec.element_to_be_clickable(
    (By.ID, students_menu_id)
)).click()

print()
print("-"*50)
for student in students:

    try:
        # Arama alanı görünene kadar bekle
        search_element = eokul.wait.until(ec.visibility_of_element_located(
            (By.ID, student_search_id)
        ))

        # Öğrenci numarası ile arama yap
        no = student['Lütfen öğrenci numarasını yazınız']
        search_element.send_keys(no)
        driver.find_element_by_id(student_search_btn_id).click()
        print(f'"{no}" numaralı öğrenci seçildi.')

        # Öğrenci genel bilgilerini güncelle
        eokul.wait.until(ec.element_to_be_clickable(
            (By.XPATH, general_info)
        )).click()

        # Kiminle oturuyor?
        last = eokul.wait.until(ec.presence_of_element_located(
            (By.XPATH, live_with.format('') + '[@selected]')
        )).text
        new = student['Kiminle oturuyor?']
        driver.find_element_by_xpath(live_with.format(new)).click()
        print(f'--- "Kiminle oturuyor?" alanı güncellendi: {last} -> {new}')

        # Oturduğu ev kira mı?
        last = driver.find_element_by_xpath(house_rented.format('') + '[@selected]').text
        new = student['Oturduğu ev kira mı?']
        driver.find_element_by_xpath(house_rented.format(new)).click()
        print(f'--- "Oturduğu ev kira mı?" alanı güncellendi: {last} -> {new}')

        # Kendi odası var mı?
        last = driver.find_element_by_xpath(own_room.format('') + '[@selected]').text
        new = student['Kendi odası var mı?']
        driver.find_element_by_xpath(own_room.format(new)).click()
        print(f'--- "Kendi odası var mı?" alanı güncellendi: {last} -> {new}')

        # Boy
        length_element = driver.find_element_by_id(student_length_id)
        last = length_element.get_attribute('value')
        new = student['Boy']
        length_element.clear()
        if new:
            length_element.send_keys(new)
            print(f'--- "Boy" alanı güncellendi: {last} -> {new}')

        # Kilo
        weight_element = driver.find_element_by_id(student_weight_id)
        last = weight_element.get_attribute('value')
        new = student['Kilo']
        weight_element.clear()
        if new:
            weight_element.send_keys(new)
            print(f'--- "Kilo" alanı güncellendi: {last} -> {new}')

        # Kardeş sayısı
        sibling_element = driver.find_element_by_id(siblings_number_id)
        last = sibling_element.get_attribute('value')
        new = student['Kardeş sayısı']
        sibling_element.clear()
        if new:
            sibling_element.send_keys(new)
            print(f'--- "Kardeş sayısı" alanı güncellendi: {last} -> {new}')

        # Kaydet
        driver.find_element_by_xpath(save_btn).click()
        print(f'"{no}" numaralı öğrenci bilgileri kaydedildi.')

        print("-"*50)
    except Exception as error:
        logger.exception(error)
