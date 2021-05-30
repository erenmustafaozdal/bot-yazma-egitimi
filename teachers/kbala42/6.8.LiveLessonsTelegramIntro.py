"""
Telegram API Kullanımı Örneği
"""
# Telegram Modül ve Sınıfını içeri aktarıyoruz
from classes.telegram import Telegram

# setting içindeki users almak için import ediyoruz
import settings

#Ekranda daha düzgün bir şekilde yazması için pprint modülü ekliyoruz
import pprint
pp = pprint.PrettyPrinter(indent=4)

# setting içindeki users alıp users değişkeninde saklıyoruz
users=settings.users
user = users[0]

# modül kurulu değilse telegram sınıfından uyarı alıyorsanız
# pip install python-dateutil
# komutu ile sınıfı kurunuz
# Telegram sınıfından telegram_api_key ve telegram_api_secret parametreleri ile bir telegram nesnesi oluşturuyoruz
telegram = Telegram(user['telegram_api_id'], user['telegram_api_hash'])
#Mesaj gönderme
# telegram.send_message(user["telegram_chat_id"],"Deneme", file='')
#mesajları okuma
chat=telegram.get_chat_ids('Deneme')
pp.pprint(chat)