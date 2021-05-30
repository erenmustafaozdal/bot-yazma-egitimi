"""
Telegram Chat Id tespiti
"""
# Telegram Modül ve Sınıfını içeri aktarıyoruz
from classes.telegram import Telegram

# setting içindeki users almak için import ediyoruz
import settings

# setting içindeki users alıp users değişkeninde saklıyoruz
users=settings.users
user = users[0]

# Telegram sınıfından telegram_api_key ve telegram_api_secret parametreleri ile bir telegram nesnesi oluşturuyoruz
telegram = Telegram(user['telegram_api_id'], user['telegram_api_hash'])

# Telegramda oluşturduğumuz Deneme grunun id öğrenmek için chat nesnesi oluturuyoruz ve öğrendiğimiz Id'yi setting'de yerine yazıyoruz
#Bu aşamada mutlaka telegram'ın oluşturduğu .session dosyası için .gitignore'a
# .session eklemeliyiz
chat=telegram.get_chat_ids('Deneme')
