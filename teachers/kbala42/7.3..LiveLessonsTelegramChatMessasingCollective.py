"""
Telegram Toplu mesajlaşma
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


# Telegram sınıfından telegram_api_key ve telegram_api_secret parametreleri ile bir telegram nesnesi oluşturuyoruz
telegram = Telegram(user['telegram_api_id'], user['telegram_api_hash'])

# 5 adet mesaj göndermek için döngü oluşturuyoruz
for i in range(5):
    # mesaj sırasını göstermek için değişen
    index=i+1
    message = GetLessonMessage({
        'Canlı Ders Başlığı':f'{index}. ders başlığı',
        'id':index,
        'join_url':'https://us04web.zoom.us/j/79148691449?pwd=eGxrTWxTTVptWlk2MkthWE5iMmdiZz09',
        'password':'şifre'

    })
    # Direkt telefona mesaj atıyoruz
    #telegram.send_message("905325734222", message)
    # telegram_chat_id adında ki Deneme grubuna mesaj atıyoruz id sayısıyla
    #telegram.send_message(user['telegram_chat_id'], message)
    # "Dememe adında ki gruba message atıyoruz (grup adıyla)
    telegram.send_message("Deneme",message)
