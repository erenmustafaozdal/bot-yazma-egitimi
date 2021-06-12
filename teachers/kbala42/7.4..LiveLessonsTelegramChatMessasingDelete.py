"""
Kullanıcı, Telegram kullanıyorsa önceki 'CANLI DERS BAŞLIYOR' mesajlarını siiliyoruz
"""
# Telegram Modül ve Sınıfını içeri aktarıyoruz
from classes.telegram import Telegram

# setting içindeki users almak için import ediyoruz
import settings

#Ekranda daha düzgün bir şekilde yazması için pprint modülü ekliyoruz
import pprint
pp = pprint.PrettyPrinter(indent=4)

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
