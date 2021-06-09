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

# todo: Öğrenci İşlemleri sayfasına git


print()
print("-"*50)
for student in students:

    try:
        # todo: Arama alanı görünene kadar bekle

        # todo: Öğrenci numarası ile arama yap

        # todo: Öğrenci genel bilgilerini güncelle

        # todo: Kiminle oturuyor?

        # todo: Oturduğu ev kira mı?

        # todo: Kendi odası var mı?

        # todo: Boy

        # todo: Kilo

        # todo: Kardeş sayısı

        # todo: Kaydet

        print("-"*50)
    except Exception as error:
        logger.exception(error)

