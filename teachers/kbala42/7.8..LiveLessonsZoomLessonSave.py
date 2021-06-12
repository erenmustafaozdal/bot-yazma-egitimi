"""
Zoom'a Ders Kaydı
"""
from classes.telegram import Telegram
from classes.Excel import Excel
import settings
# Browser sınıfını import ediyoruz
from classes.Browser import Browser
# EBA sınıfını import ediyoruz
from classes.Eba import EBA
from classes.Zoom import Zoom
# Şartları kullanmak için ekliyoruz
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from datetime import datetime

#Ekranda daha düzgün bir şekilde yazması için pprint modülü ekliyoruz
import pprint
pp = pprint.PrettyPrinter(indent=4)

# hata yakaladıktan sonra yine de hata hakkında bize mesaj döndürmesi için bu modülü kullanıyoruz
import logging
logger = logging.getLogger()

# Canlı ders eklerken işimize yarayacak seçiciler (XPATH vb.)
live_lessons_menu = "//div[normalize-space()='Canlı Dersler']" # Canlı ders butonu değişkeni
add_live_lesson_btn = "//button[normalize-space()='Harici Canlı Ders Ekle']"  #Harici Ders Ekle butonu
live_lesson_title = "//div[contains(text(), 'Ders Başlığı')]/following-sibling::input" # Ders Başlığı seçicisi
classroom = "//div[contains(text(), 'Sınıf')]/following-sibling::select/option[contains(text(),'{}')]" # Sınıf seçimi
date_picker = "//div[contains(text(), 'Tarih')]/following-sibling::p//button"# Date picker seçimi
day_btns = "//table[@class='uib-daypicker']//button[not(@disabled)][normalize-space()='{}']" # Gün seçimi
lesson_hour = "//div[contains(text(), 'Saat')]/following-sibling::div/select/option[text()='{}']" # saat seçimi
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
lesson_delete_btn = "//div[@class='body-container']/div[@role='row']//div[contains(normalize-space(), '{}') and contains(normalize-space(), '{}')]//i[@class='vt-icon-delete']"
delete_yes_btn = "//a[normalize-space()='EVET']"
next_button = "//a[text()='Sonraki']"


def GetLessonMessage(lesson:'dict'):
    """
    Velilere gönderilecek ders giriş bilgileri mesajı şablonunun bulunduğu
    mesaj metnini geri döndüren fonksiyon

    :param lesson: dictionary türünde JSON nesnesi
    :return:
    """
    return f"""**CANLI DERS BAŞLIYOR**\n
    **📚 ‍ Ders:** {lesson['Canlı Ders Başlığı']}
    **👨‍🏫 Ders ID:** [{lesson['id']}] ({lesson['join_url']})
    **🔑  Şifre:** {lesson['password']}\n
    ➖➖➖➖➖\n
    [{lesson['join_url']}] ({lesson['join_url']})"""

# Kullanıcıları alıyoruz. Her kullanıcı için aşağıdaki işlemleri yapıyoruz
for user in settings.users:
    # Telegram sınıfından telegram_api_key ve telegram_api_secret parametreleri ile bir telegram nesnesi oluşturuyoruz
    telegram = Telegram(user['telegram_api_id'], user['telegram_api_hash'])

    # Geçmiş ders mesajlarını ilioruz
    # Silme işlemini yapmak için telegram nesnesi hazırsa yapıyoruz. Yani telegram kullanıyorsa yapılacak
    if telegram.ready():
        #telegram.delete_messages(user['telegram_chat_id'],'CANLI DERS BAŞLIYOR')
        telegram.delete_messages('Deneme', 'CANLI DERS BAŞLIYOR')

    # Kullanıcı canlı dersler Excel dosyasından verileri alıyoruz
    # Kullanıcının live_lessons_xl tanımlı excel dosyasından excel nesnesi oluşturuyoruz
    # True parametresi yalnızca okunan içerikleri okumak için kullanıyoruz
    excel= Excel(user['live_lessons_xl'], data_only=True)
    # excel'de verileri alıyoruz
    lessons=excel.get_datas()
    del excel

    # Zoom nesnesi oluşturuyoruz
    zoom = Zoom(user['zoom_api_key'], user['zoom_api_secret'])

    # Tarayıcı nesnesi oluştur
    # browser = Browser(settings.driver_path, profile=user['tc']) # Browser sınıfında Geriye uyumluluk
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
                    "request_permission_to_unmute_participants": True if lesson[
                                                                             "Request Permission to Unmute Participants"] == "on" else False
                }
            })
            #  Zoom'dan gelen id, password ve join_url bilgilerini lessons içindeki ders bilgisine ekle
            pp.pprint(response_data)
            lessons[index] = {**lesson, **response_data}

            # Ders Zoom'da kaydedildi ise durumuna "zoom" yaz
            lessons[index]["Durum"] = "zoom"

            # Dersi EBA'da kaydet (EBA işlemleri başlagıcı: Burası bir fonksiyon içine alınabilir)

            # raise Exception('Hata oldu') # Deneme amaçlı hata yaptırıyoruz. Except test etmek için.

        except Exception as error:
            logger.exception(error)
            pass
            # "Durum = zoom" ise; Zoom'daki dersi sil
            if lessons[index]['Durum'] == 'zoom':
                # zoom dersi silinir
                zoom.delete_meeting(lessons[index]['id'])

            raise #hata verdiriyoruz

        break
