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
# Modül ve Sınıfları içeri aktarıyoruz
from classes.Zoom import Zoom

# setting içindeki users almak için import ediyoruz
import settings

import pprint
pp = pprint.PrettyPrinter(indent=4)

# setting içindeki users alıp users değişkeninde saklıyoruz
users=settings.users
user = users[0]

zoom = Zoom(user['zoom_api_key'], user['zoom_api_secret'])
result = zoom.create_meeting({
     "topic": "Deneme Dersi",
     "start_time": "2021-05-25T09:16:30",
     "password": "123456",
     "agenda": "Deneme dersinin açıklaması",
     "settings": {
         "host_video": True,
         "participant_video": True,
         "auto_recording": "local",
         "request_permission_to_unmute_participants": True
     }
 })

pp.pprint(result)
#zoom.delete_meeting("72767793179")