# HTTP istekleri göndermek için modülümüzü import ediyoruz
import http.client
# Zoom'un istediği TOKEN'i (jeton) "Api Key" ve "Api Secret" değerlerinden
# oluşturmak için "jwt" modülünü import ediyoruz.
# Bu paketi yüklemek için: pip install PyJWT
import jwt
# tarih işlemleri için datetime
# belirli bir tarihe belirli bir süre eklemek için timedelta
from datetime import datetime, timedelta
# dictionary (json) veri türünü string değere dönüştürmek için kullanılıyor
import json


class Zoom:
    """
    Zoom'da toplantı oluşturma, silme ve ayarları alıp, güncelleme işlemleri için yardımcı nesne
    """

    def __init__(self, api_key, api_secret):
        """
        __init__ ile nesne oluşturulduğunda ilk tanımlama ve ayarlamalar yapılır

        :param api_key: Kullanıcının Zoom api key
        :param api_secret: Kullanıcının Zoom api secret
        """

        self.api_key = api_key
        self.api_secret = api_secret

        # varsayılan ders ayarları
        self.__default_meeting = {
            "topic": "",  # toplantı başlığı
            "type": 2,  # scheduled meeting
            "start_time": "",  # toplantı başlangıcı (yyyy-MM-ddTHH:mm:ss)
            "duration": 30,  # toplantı süresi
            "timezone": "Europe/Istanbul",  # saat dilimi
            "password": "",  # toplantı için şifre (boş olursa otomatik oluşturur)
            "agenda": "",  # toplantı açıklaması
            "settings": {
                "use_pmi": False,  # kişisel toplantı id (sabit id) kullanılsın mı?
                "host_video": False,  # başlangıçta toplantı sahibi kamerası açılsın mı?
                "participant_video": False,  # başlangıçta katılımcıların kameraları açılsın mı?
                "join_before_host": False,  # toplantı başlamadan katılımcılar katılabilsin mi? (bekleme odası açılırsa bu iptal olur)
                "mute_upon_entry": True,  # girişte katılımcılar sessize alınsın mı?
                "auto_recording": "none",  # toplantı video olarak kaydedilsin mi? (local, none)
                "waiting_room": False,  # girişte bekleme odası etkinleştirilsin mi?
                "request_permission_to_unmute_participants": False  # ses açma izni başlangıçta alınsın mı?
            }
        }

        # her ders oluşturma isteği sırasında ayarları tekrar sorgulama yapmamak için kullanıcının ayarlarını sınıf içinde saklayacağız
        self.__user_settings = {
            "in_meeting": {
                "request_permission_to_unmute_participants": None
            },
            "recording": {
                "local_recording": None,
                "auto_recording": "",  # local, none
            }
        }

        # bağlantıyı oluştur ve sınıf içindeki değişkende tut
        self.__conn = http.client.HTTPSConnection("api.zoom.us")

    def __get_jwt(self):
        """
        JWT oluşturup geri döndürür

        :return: string türünde JWT değerini geri döndürür
        """

        # 5 saniye sonrası için son bulma tarihi oluşturuyoruz
        expire_time = datetime.now() + timedelta(seconds=5)

        # 5 saniye sonra sona erecek JWT oluşturup döndürüyoruz
        return jwt.encode({
            "iss": self.api_key,
            "exp": expire_time.timestamp()
        }, self.api_secret, algorithm="HS256")

    def __send_request(self, method, url, body=None):
        """
        Zoom'a HTTP isteği gönderme işlemini yapar

        :param method: isteğin metodu (GET, POST, PUT, PATCH vb.)
        :param url: isteğin gönderileceği adres
        :param body: eğer varsa istekte bulunan gövde parametreleri
        :return: 200 cinsinden bir durum ile başarılı olursa yanıtı geri döndürür
        """

        # isteğin başlık bilgisini oluştur
        headers = {
            'authorization': "Bearer " + self.__get_jwt(),
            'content-type': "application/json"
        }

        # isteği gönder
        self.__conn.request(method, url, json.dumps(body), headers)

        # gelen yanıtı al
        response = self.__conn.getresponse()

        # eğer 200 cinsinden bir yanıt durumu gelmediyse hata oluştur
        if not 200 <= response.status < 300:
            raise Exception(f"Yanıt Durumu: {response.status} - Mesaj: {response.read().decode('utf-8')}")

        return response

    def create_meeting(self, meeting):
        """
        Yeni toplantı oluşturur

        :param meeting: Toplantı ayar ve bilgileri
        :return: oluşturulan toplantının id, şifre ve bağlantısını döndürür
        """

        # kullanıcının toplantı ayarları, varsayılan toplantı ayarlarının üzerine yazarak birleştirilir
        body = {**self.__default_meeting, **meeting}

        # auto_recording ve request_permission_to_unmute_participants ayarları zoom kullanıcı ayarlarından açıldığında çalışır
        # bu sebeple bu ayarlardan birisi açılması istenmişse zoom kullanıcı ayarlarını güncelleyelim
        if body['settings']['auto_recording'] == "local" or body['settings']['request_permission_to_unmute_participants']:
            self.update_settings(body['settings'])


        # ders oluşturma isteği gönderilir ve yanıt ayrıştırılır
        response = self.__send_request("POST", "/v2/users/me/meetings", body)
        data = json.loads(response.read().decode("utf-8"))

        print("Zoom toplantısı oluşturuldu.")

        # toplantı id, şifre ve katılım adresleri geri döndürülür
        return {
            "id" : data["id"],
            "password" : data["password"],
            "join_url" : data["join_url"],
        }

    def delete_meeting(self, meeting_id):
        """
        Toplantıyı siler

        :param meeting_id: toplantı id'si
        """
        self.__send_request("DELETE", f"/v2/meetings/{meeting_id}")

        print(f"'{meeting_id}' ID'li Zoom toplantısı silindi.")

    def update_settings(self, settings):
        """
        Zoom'daki kullanıcı ayarlarını günceller. Güncelleme isteğini sürekli göndermemek için nesne içindeki kullanıcı ayarlarındaki eşitliği kontrol eder

        :param settings: Toplantı ayarları
        """

        body = self.to_user_settings(settings)

        # nesne içindeki kullanıcı ayarları ile toplantı ayarları eşleşiyorsa dön
        if self.__user_settings == body:
            return

        # Zoom'daki kullanıcı ayarları ile toplantı ayarları eşleşiyorsa dön
        if self.get_settings() == body:
            return

        # ayarları güncelleme isteği gönderilir
        self.__send_request("PATCH", "/v2/users/me/settings", body)

        # güncellenen ayarlar ile nesne içindeki kullanıcı ayarlarını güncelle
        self.__user_settings = body

        print("Zoom ayarları güncellendi.")

    def get_settings(self):
        """
        Zoom'dan gelen kullanıcı ayarları ile nesnedeki kullanıcı ayarlarını günceller ve döndürür

        :return: kullanıcı ayarlarını döndürür
        """

        response = self.__send_request("GET", "/v2/users/me/settings?custom_query_fields=auto_recording,local_recording,request_permission_to_unmute_participants")
        self.__user_settings = json.loads(response.read().decode("utf-8"))

        print("Zoom kullanıcı ayarları getirildi.")

        return self.__user_settings

    def to_user_settings(self, settings):
        """
        Toplantı ayarlarını, kullanıcı ayarları formatına dönüştürür

        :param settings: toplantı ayarları
        :return: gerekli ayarları kullanıcı ayarı formatında döndürür
        """

        settings = {
            "in_meeting": {
                "request_permission_to_unmute_participants": settings[
                    "request_permission_to_unmute_participants"]
            },
            "recording": {
                "local_recording": True if settings["auto_recording"] == "local" else False,
                "auto_recording": settings["auto_recording"]
            }
        }
        return settings

    def __del__(self):
        """
        Nesne silindiğinde bağlantıyı kapatır
        """

        self.__conn.close()
