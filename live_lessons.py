"""
ALGORİTMA
- Kullanıcıları al. Her kullanıcı için aşağıdaki işlemleri yap.
    - Kullanıcı canlı dersler Excel dosyasından verileri al.
    - Her ders için aşağıdaki işlemleri yap.
        - Dersi Zoom'da kaydet
            - JWT Token oluştur
            - Varsayılan ders ayarlarını tanımla
            - İstenen ders ayarlarında kullanıcı ayarı değişikliği gerekiyorsa bu değişiklikleri yap
            - Ders kaydı sırasında bir hata döndürdü mü kontrol et
        - Ders Zoom'da kaydedildi ise durumuna "zoom" yaz
        - Dersi EBA'da kaydet
            - "Canlı Dersler" sayfasına git
            - "Harici Canlı Ders Ekle" sayfasına git
            - Ders bilgilerini ekle
            - Konu ve Şube/Grup (birden fazla olabilir) seç
            - Öğrencileri listele
            - Dersi kaydet
        - Ders EBA'da kaydedildi ise durumuna "eba" yaz
        - Ders için Telegram'da mesaj planla
        - Ders için mesaj planlandı ise durumuna "hazır" yaz

- Herhangi bir ders kaydı sırasında bir hata olursa durumunu kontrol et ve aşağıdaki işlemlerden birini yap.
    - "Durum = zoom" ise; Zoom'daki dersi sil
    - "Durum = eba" ise; Zoom'daki ve EBA'daki dersi ve Telegram mesajını sil
    - Hata sonrası Excel dosyasına bitenleri yaz
- Herhangi bir hata olmadı ve ders kayıtları bittiyse tüm derslerin durumunu temizle
"""
# Todo: Modül ve sınıfları içeri aktar
from classes.zoom import Zoom
from classes.telegram import Telegram
from classes.excel import Excel
from classes.browser import Browser
from classes.eba import EBA
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import settings
import time
from datetime import datetime

# hata yakaladıktan sonra yine de hata hakkında bize mesaj döndürmesi için bu modülü kullanıyoruz
import logging
logger = logging.getLogger()

# dictionary veri tipini satırlar halinde ekrana yazdırmak için bu modülü kullanıyoruz
import pprint
pp = pprint.PrettyPrinter(indent=4)

# Canlı ders eklerken işimize yarayacak seçiciler (XPATH vb.)
live_lessons_menu = "//div[normalize-space()='Canlı Dersler']"
add_live_lesson_btn = "//button[normalize-space()='Harici Canlı Ders Ekle']"
live_lesson_title = "//div[contains(text(), 'Ders Başlığı')]/following-sibling::input"
classroom = "//div[contains(text(), 'Sınıf')]/following-sibling::select/option[contains(text(),'{}')]"
date_picker = "//div[contains(text(), 'Tarih')]/following-sibling::p//button"
day_btns = "//table[@class='uib-daypicker']//button[not(@disabled)][normalize-space()='{}']"
lesson_hour = "//div[contains(text(), 'Saat')]/following-sibling::div/select/option[text()='{}']"
description = "//div[contains(text(), 'Açıklama')]/following-sibling::input"
lesson_link = "//div[contains(text(), 'Ders Linki')]/following-sibling::input"
zoom_app = "//div[contains(text(), 'Uygulama')]/following-sibling::select/option[contains(text(),'Zoom')]"
lesson_password = "//div[contains(text(), 'Ders Şifresi')]/following-sibling::input"
lesson_select = "//div[contains(text(), 'Ders *')]/following-sibling::div"
lesson_name = lesson_select + "//span[@class='ui-select-choices-row-inner'][normalize-space()='{}']"
group_select = "//span[contains(text(), 'Şube')]/parent::div/following-sibling::div"
group_name = ".//span[contains(text(),'{}')]"
list_students = "//div[contains(text(), 'ÖĞRENCİLERİ LİSTELE')]"
send_live_lesson = "//div[contains(text(), 'CANLI DERSİ GÖNDER')]"
ok_btn = "//a[normalize-space()='TAMAM']"


##### EXCEL'den dosyasından aldığımız dictionary türünde bir ders örneği
# {   'Auto Recording': 'on',
#     'Açıklama': '31 Mayıs 2021 Pazartesi günü 09:10 - 09:40 saat aralığında '
#                 'yapılacak Fen Bilimleri dersi.',
#     'Canlı Ders Başlığı': 'Fen Bilimleri',
#     'Canlı Ders Tarihi': datetime.datetime(2021, 5, 31, 0, 0),
#     'Ders': 'Fen Bilimleri',
#     'Ders Saat Aralığı': '09:10 - 09:40',
#     'Durum': None,
#     'Haftanın Günü': 'Pazartesi',
#     'Host Video': 'on',
#     'Join Before Host': 'off',
#     'Meeting ID': 'new',
#     'Mute Upon Entry': 'on',
#     'Participant Video': 'on',
#     'Password': None,
#     'Request Permission to Unmute Participants': 'on',
#     'Sınıf': '3. Sınıf',
#     'Waiting Room': 'off',
#     'row': 2,
#     'Şube/Grup': '3. Sınıf / A Şubesi'}

def get_lesson_message(lesson:'dict'):
    """
    Velilere gönderilecek ders giriş bilgileri mesajı şablonunun bulunduğu,
    mesaj metnini geri döndüren fonksiyon

    :param lesson: dictionary türünde JSON nesnesi
    :return:
    """

    return f"""**CANLI DERS BAŞLIYOR**\n
**📚 Ders:** {lesson['Canlı Ders Başlığı']}
**👨‍🏫 Ders ID:** [{lesson['id']}]({lesson['join_url']})
**🔑 Şifre:** {lesson['password']}\n
➖➖➖➖➖\n
[{lesson['join_url']}]({lesson['join_url']})"""


# Kullanıcıları al. Her kullanıcı için aşağıdaki işlemleri yap. (Kullanıcılar döngüsü)
for user in settings.users:

    # Telegram nesnesi oluştur
    telegram = Telegram(user['telegram_api_id'], user['telegram_api_hash'])

    # Geçmiş ders mesajları sil
    if telegram.ready():
        telegram.delete_messages(user['telegram_chat_id'], 'CANLI DERS BAŞLIYOR')

    # Kullanıcı canlı dersler Excel dosyasından verileri al.
    excel = Excel(user['live_lessons_xl'], data_only=True)
    lessons = excel.get_datas()
    del excel

    # Zoom nesnesi oluştur
    zoom = Zoom(user['zoom_api_key'], user['zoom_api_secret'])

    # Tarayıcı nesnesi oluştur
    browser = Browser(settings.driver_path)
    driver = browser.get()

    # EBA nesnesi oluştur
    eba = EBA(driver)

    # EBA'ya giriş yap
    eba.login(user['tc'], user['password'])

    # Canlı dersler sayfasına git
    eba.wait.until(ec.element_to_be_clickable(
        (By.XPATH, live_lessons_menu)
    )).click()
    time.sleep(2)

    # Durumu "hazır" olmayan her ders için aşağıdaki işlemleri yap. (Kullanıcının dersleri döngüsü)
    for index, lesson in enumerate(lessons):
        if lesson['Durum'] == 'hazır':
            continue


        # Dersin başlama tarihini düzelt
        start_hour = datetime.strptime(lesson['Ders Saat Aralığı'].split(" - ")[0], "%H:%M")
        #  Zoom ve Telegram'da kullanmak için dersin tarihini ve saat aralığını birleştir
        lesson["start_time"] = lesson['Canlı Ders Tarihi'].replace(hour=start_hour.hour, minute=start_hour.minute)

        try:
            pass
            # Dersi Zoom'da kaydet (try başlangıcı)
            response_data = zoom.create_meeting({
                "topic": lesson['Canlı Ders Başlığı'],
                "start_time": lesson["start_time"].strftime("%Y-%m-%dT%H:%M:%S"),
                "password": "" if lesson["Password"] is None else lesson["Password"],
                "agenda": "" if lesson["Açıklama"] is None else lesson["Açıklama"],
                "settings": {
                    "use_pmi": True if lesson["Meeting ID"] == "pmi" else False,
                    "host_video": True if lesson["Host Video"] == "on" else False,
                    "participant_video": True if lesson["Participant Video"] == "on" else False,
                    "join_before_host": False if lesson["Join Before Host"] == "off" else True,
                    "mute_upon_entry": False if lesson["Mute Upon Entry"] == "off" else True,
                    "auto_recording": "local" if lesson["Auto Recording"] == "on" else "none",
                    "waiting_room": True if lesson["Waiting Room"] == "on" else False,
                    "request_permission_to_unmute_participants": True if lesson["Request Permission to Unmute Participants"] == "on" else False
                }
            })
            #  Zoom'dan gelen id, password ve join_url bilgilerini lessons içindeki ders bilgisine ekle
            lessons[index] = {**lesson, **response_data}

            # Ders Zoom'da kaydedildi ise durumuna "zoom" yaz
            lessons[index]["Durum"] = "zoom"

            # Dersi EBA'da kaydet (EBA işlemleri başlagıcı: Burası bir fonksiyon içine alınabilir)

            # Harici canlı ders ekleme sayfasına git
            eba.left_menu_is_loaded()
            eba.wait.until(ec.element_to_be_clickable((By.XPATH, add_live_lesson_btn))).click()

            # Canlı dersin meta verilerini ekle (Ders başlığı ve sınıf)
            eba.wait.until(ec.visibility_of_element_located(
                (By.XPATH, live_lesson_title)
            )).send_keys(lesson['Canlı Ders Başlığı'])
            driver.find_element_by_xpath(classroom.format(lesson['Sınıf'])).click()

            # Canlı dersin tarihini seç
            driver.find_element_by_xpath(date_picker).click()
            elements = driver.find_elements_by_xpath(day_btns.format(
                lesson['Canlı Ders Tarihi'].strftime('%d')
            ))
            elements[-1].click()
            time.sleep(2)

            # Canlı dersin zaman aralığını seç
            eba.wait.until(ec.element_to_be_clickable(
                (By.XPATH, lesson_hour.format(lesson['Ders Saat Aralığı']))
            )).click()

            # Canlı dersin açıklamasını ekle
            driver.find_element_by_xpath(description).send_keys(lesson['Açıklama'])

            # Canlı dersin Zoom bilgilerini ekle
            driver.find_element_by_xpath(lesson_link).send_keys(lessons[index]['join_url'])
            driver.find_element_by_xpath(lesson_password).send_keys(lessons[index]['password'])
            driver.find_element_by_xpath(zoom_app).click()

            # Canlı dersi seç
            eba.wait.until(ec.element_to_be_clickable((By.XPATH, lesson_select))).click()
            eba.wait.until(ec.element_to_be_clickable(
                (By.XPATH, lesson_name.format(lesson['Ders']))
            )).click()

            # Canlı dersin yapılacağı şube ve grupları seç
            #  Birden fazla seçim yapılabilir
            #  Excel çalışma kitabında virgül (,) ile ayrılarak eklenebilir
            element = eba.wait.until(ec.element_to_be_clickable(
                (By.XPATH, group_select)
            ))
            element.click()
            time.sleep(1)
            for group in lesson['Şube/Grup'].split(','):
                element.find_element_by_xpath(
                    group_name.format(group.strip())
                ).click()

            # Öğrenci listele tıklanır
            driver.find_element_by_xpath(list_students).click()

            # Canlı dersi gönder tıkla
            eba.wait.until(ec.element_to_be_clickable((By.XPATH, send_live_lesson))).click()

            # Tamam tıkla
            eba.wait.until(ec.element_to_be_clickable((By.XPATH, ok_btn))).click()

            # Todo: Ders EBA'da kaydedildi ise durumuna "eba" yaz

            # Todo: Ders için Telegram'da mesaj planla

            # Todo: Ders için mesaj planlandı ise durumuna "hazır" yaz

        # Todo: Herhangi bir ders kaydı sırasında hata olursa durumunu kontrol et ve aşağıdaki işlemlerden birini yap.

        except Exception as error:
            logger.exception(error)

            # Todo: "Durum = zoom" ise; Zoom'daki dersi sil
            if lessons[index]['Durum'] == 'zoom':
                # zoom dersi silinir
                zoom.delete_meeting(lessons[index]['id'])

            # Todo: "Durum = eba" ise; Zoom'daki ve EBA'daki dersi ve Telegram mesajını sil

            # Todo: Hata sonrası Excel dosyasın bitenleri yaz
            #  "Durum" sutünuna her ders için durumu yaz
            #  Bir sonraki çalıştırmada durumu "hazır" olanlar dışındaki dersler oluşturulacak

            raise

        break

    # Todo: Herhangi bir hata olmadı ve ders kayıtları bittiyse tüm derslerin durumunu temizle
