# Telegram BOT Api'si için kullanılacak olan Telethon kütüphanesi
# bu kütüphaneyi yüklemek için: pip install telethon
from telethon.sync import TelegramClient
from telethon import functions as func
# telegram mesajını zamanlarken kendi zaman dilimimize göre ayarlama yapmak için kullanılan modül
# modül kurulu değilse pip install python-dateutil omutu ile kurunuz
from dateutil import tz


class Telegram:
    """
    Telegram işlemlerini yönetecek olan nesne
    """

    def __init__(self, api_id, api_hash):
        """
        __init__ ile nesne oluşturulduğunda ilk tanımlama ve ayarlamalar yapılır

        :param api_id: Kullanıcının Telegram api_id
        :param api_hash: Kullanıcının Telegram api_hash
        """

        # işlemleri yapacağımız nesne oluşturulur
        if api_id and api_hash:
            self.__client = TelegramClient('telegram',api_id, api_hash)
        else:
            self.__client = None

    def ready(self):
        """
        Telegram bağlantısının hazır olup olmadığını döndürür. Telegram kullanıcı bilgisi eksik olanlar için False döndürür

        :return: boolean
        """

        return self.__client is not None

    def send_message(self, chat_id, message, date=None, link_preview=False, file=None):
        """
        __async_send_message metodunun işlemi tamamlanana kadar döngüde kalan metot

        :param chat_id: integer şeklinde sohbet id
        :param message: gönderilecek mesaj
        :param date: eğer zamanlanacaksa tarih bilgisi
        :param link_preview: bağlantı önizlemesi olsun mu?
        """

        # eğer gelen tarih varsa, kendi zaman dilimimize çevir
        if date is not None:
            date = date.astimezone(tz.tzlocal())

        with self.__client as cli:
            cli.loop.run_until_complete(
                self.__async_send_message(chat_id, message, date, link_preview, file)
            )

        if date is not None:
            print(f"Telegram mesajı {date.strftime('%d.%m.%Y %H:%M')} tarihi için zamanladı.")
        else:
            print("Telegram mesajı gönderildi")


    async def __async_send_message(self, chat_id, message, date=None, link_preview=False, file=None):
        """
        Sohbet mesajı gönderme veya zamanlama işlemi yapar

        :param chat_id: integer şeklinde sohbet id
        :param message: gönderilecek mesaj
        :param date: eğer zamanlanacaksa tarih bilgisi
        :param link_preview: bağlantı önizlemesi olsun mu?
        """

        await self.__client.send_message(
            chat_id,
            message,
            link_preview=link_preview,
            file=file,
            schedule=date
        )

    def get_chat_ids(self, keywords=""):
        """
        __async_get_chat_ids metodunun işlemi tamamlanana kadar döngüde kalan metot

        :param keywords: Sohbet adında varlığı sorgulanacak anahtar kelimeler. Boş olursa bütün sohbetleri döndürür
        :return: liste şeklinde sohbetleri döndürür {'chat':dialog.name, 'id':dialog.id}
        """

        with self.__client as cli:
            return cli.loop.run_until_complete(self.__async_get_chat_ids(keywords))

    async def __async_get_chat_ids(self, keywords=""):
        """
        Aranan kelimelere göre sohbet adını ve id'sini döndürür. Kullanılacak sohbetin id'sini bulmak için kullanılabilir.

        :param keywords: Sohbet adında varlığı sorgulanacak anahtar kelimeler. Boş olursa bütün sohbetleri döndürür
        :return: liste şeklinde sohbetleri döndürür {'chat':dialog.name, 'id':dialog.id}
        """

        chats = []
        async for dialog in self.__client.iter_dialogs():
            # eğer aranan anahtar kelimeler (keywords) sohbet adında varsa listeye ekle
            if keywords in dialog.name:
                chats.append({
                    'chat': dialog.name,
                    'id': dialog.id,
                })
        return chats

    def delete_messages(self, chat_id, keywords=""):
        """
        Belirli bir sohbetteki aranan ifade ile eşleşen mesajları siler.

        :param chat_id: integer şeklinde sohbet id
        :param keywords: Mesaj içinde aranacak ifade
        """

        with self.__client as cli:
            for message in cli.iter_messages(entity=chat_id, search=keywords):
                message.delete()

        if keywords:
            print(f"'{keywords}' ifadesi geçen mesajlar silindi")
        else:
            print("Tüm mesajlar silindi")

    def delete_scheduled_messages(self, chat_id, keywords=""):
        """
        Belirli bir sohbetteki aranan ifade ile eşleşen zamanlanmış mesajları siler.

        :param chat_id: integer şeklinde sohbet id
        :param keywords: Mesaj içinde aranacak ifade
        """

        with self.__client as cli:
            # zamanlanmış mesajlar alınır
            sch_messages = cli(func.messages.GetScheduledHistoryRequest(peer=chat_id, hash=0))

            # silinecek mesajlar belirlenir
            deletes = []
            for message in sch_messages.messages:
                if keywords in message.message:
                    deletes.append(message.id)

            # mesajlar silinir
            cli(func.messages.DeleteScheduledMessagesRequest(peer=chat_id, id=deletes))

        if keywords:
            print(f"'{keywords}' ifadesi geçen zamanlanmış mesajlar silindi")
        else:
            print("Tüm zamanlanmış mesajlar silindi")
