"""
Zoom Kullanımı Örneği
"""
# Zoom Modül ve Sınıfını içeri aktarıyoruz
from classes.Zoom import Zoom

# setting içindeki users almak için import ediyoruz
import settings

#Ekranda daha düzgün bir şekilde yazması için pprint modülü ekliyoruz
import pprint
pp = pprint.PrettyPrinter(indent=4)

# setting içindeki users alıp users değişkeninde saklıyoruz
users=settings.users
user = users[0]

# Zoom sınıfından zoom_api_keyve zoom_api_secret parametreleri ile bir zoom nesnesi oluşturuyoruz
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