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
import settings

import pprint
pp = pprint.PrettyPrinter(indent=4)



users = settings.users
user = users[0]

zoom = Zoom(user['zoom_api_key'], user['zoom_api_secret'])
result = zoom.create_meeting({
    "topic": "Deneme Dersi",
    "start_time": "2021-05-24T09:10:00",
    "password": "123456",
    "agenda": "Deneme bilgi dersinin açıklaması",
    "settings": {
        "host_video": True,
        "participant_video": True,
        "auto_recording": "local",
        "request_permission_to_unmute_participants": True
    }
})

# zoom.delete_meeting("72767793179")

telegram = Telegram(user['telegram_api_id'], user['telegram_api_hash'])
chat = telegram.get_chat_ids('Arama Metni')
pp.pprint(chat)
# telegram.send_message(user['telegram_chat_id'], "Deneme", file='./images/student-based-reports/20210508-53 NİSANUR DAYLAN.png')

# Todo: Canlı ders eklerken işimize yarayacak seçiciler (XPATH vb.)

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


# Todo: Kullanıcıları al. Her kullanıcı için aşağıdaki işlemleri yap. (Kullanıcılar döngüsü)

# Todo: Telegram nesnesi oluştur

# Todo: Geçmiş ders mesajları sil

# Todo: Kullanıcı canlı dersler Excel dosyasından verileri al.

    # Todo: Zoom nesnesi oluştur

    # Todo: Tarayıcı nesnesi oluştur

    # Todo: EBA nesnesi oluştur

    # Todo: EBA'ya giriş yap

    # Todo: Canlı dersler sayfasına git

    # Todo: Durumu "hazır" olmayan her ders için aşağıdaki işlemleri yap. (Kullanıcının dersleri döngüsü)

        # Todo: Dersin başlama tarihini düzelt
        #  Zoom ve Telegram'da kullanmak için dersin tarihini ve saat aralığını birleştir

            # Todo: Dersi Zoom'da kaydet (try başlangıcı)
            #  Zoom'dan gelen id, password ve join_url bilgilerini lessons içindeki ders bilgisine ekle

            # Todo: Ders Zoom'da kaydedildi ise durumuna "zoom" yaz

            # Todo: Dersi EBA'da kaydet (EBA işlemleri başlagıcı: Burası bir fonksiyon içine alınabilir)

            # Todo: Harici canlı ders ekleme sayfasına git

            # Todo: Canlı dersin meta verilerini ekle (Ders başlığı ve sınıf)

            # Todo: Canlı dersin tarihini seç

            # Todo: Canlı dersin zaman aralığını seç

            # Todo: Canlı dersin açıklamasını ekle

            # Todo: Canlı dersin Zoom bilgilerini ekle

            # Todo: Canlı dersi seç

            # Todo: Canlı dersin yapılacağı şube ve grupları seç
            #  Birden fazla seçim yapılabilir
            #  Excel çalışma kitabında virgül (,) ile ayrılarak eklenebilir

            # Todo: Öğrenci listele tıklanır

            # Todo: Öğrenci listele tıkla

            # Todo: Canlı dersi gönder tıkla

            # Todo: Tamam tıkla

            # Todo: Ders EBA'da kaydedildi ise durumuna "eba" yaz

            # Todo: Ders için Telegram'da mesaj planla

            # Todo: Ders için mesaj planlandı ise durumuna "hazır" yaz

        # Todo: Herhangi bir ders kaydı sırasında hata olursa durumunu kontrol et ve aşağıdaki işlemlerden birini yap.

            # Todo: "Durum = zoom" ise; Zoom'daki dersi sil

            # Todo: "Durum = eba" ise; Zoom'daki ve EBA'daki dersi ve Telegram mesajını sil

            # Todo: Hata sonrası Excel dosyasın bitenleri yaz
            #  "Durum" sutünuna her ders için durumu yaz
            #  Bir sonraki çalıştırmada durumu "hazır" olanlar dışındaki dersler oluşturulacak

    # Todo: Herhangi bir hata olmadı ve ders kayıtları bittiyse tüm derslerin durumunu temizle
