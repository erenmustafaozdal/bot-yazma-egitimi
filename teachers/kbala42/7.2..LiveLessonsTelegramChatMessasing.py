"""
Telegram mesajlaşma
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

# Telegram sınıfından telegram_api_key ve telegram_api_secret parametreleri ile bir telegram nesnesi oluşturuyoruz
telegram = Telegram(user['telegram_api_id'], user['telegram_api_hash'])
# Kendimize mesaj atma
#telegram.send_message("me","Deneme")
# Numara ile mesaj atma
telegram.send_message("905325734222","Merhaba")
# telegram_chat_id kullanarak giriş. "telegram_chat_id" ilk önce çalıştı. Ancak güncellemeden sonra hiç çalışmadı.KB
#telegram.send_message(user['telegram_chat_id'],"Telegram id deneme")
# telegram_grupa adı kullanarak giriş
telegram.send_message('Deneme',"Merhaba Telegram 'Deneme' grubu")