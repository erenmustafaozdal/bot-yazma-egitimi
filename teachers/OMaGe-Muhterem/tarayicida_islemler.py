"""
tarayici_işlemleri: tarayıcıda bazı işlemler (tarayıcı nesnesi oluşturma,
bir internet adresine gitme, gidilen adresi yazma, yeni bir adrese gitme,
önceki sayfaya dönme, sonraki sayfaya gitme, sayfa başlığı yazma
ve tarayıcıyı kapatma) yapımı
"""

from selenium import webdriver
import settings
import time


# Tarayıcı işlemleri yapabilmek için bir nesne oluşturdum
tarayici = webdriver.Chrome(settings.surucu_yolu)

# Bir internet adresine gitme komutunu 'GET("https://gidilecek_adres")' kullandım
tarayici.get("https://istanbulakademi.meb.gov.tr")

# Gidilen adresi yazdırma komutunu tarayici.CURRENT_URL kullandım
print(tarayici.current_url)

time.sleep(2)   # 2 saniye beklettim

# yeni adrese git ve adresi yaz
tarayici.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
print(tarayici.current_url)

time.sleep(2)

# Bir önceki sayfaya dönmek için tarayici.BACK()
tarayici.back()

time.sleep(2)

# Bir sonraki sayfaya dönmek için tarayici.FORWARD()
tarayici.forward()

time.sleep(2)

#   Gidilen sayfanın başlığını almak için tarayici.TITLE
print(tarayici.title)

# Tarayıcıyı kapat
tarayici.close()