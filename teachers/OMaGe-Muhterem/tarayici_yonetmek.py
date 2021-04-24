"""
tarayıcı yönetimi: Tarayıcı ile ilgili bilgiler (genişlik, yükseklik,
üstten boşluk, soldan boşluk) alma veya tarayıcıyı  yönetme
(ekranı kaplama, küçültme, boyutlarını ayarlama, konumunu ayarlama)
işlemleri
"""
from selenium import webdriver
import settings
import time

# tarayıcı nesnesini oluşturalım. windows Chrome için webdriver.Chrome("chrome.exe nin yolu")
tarayc = webdriver.Chrome(settings.surucu_yolu)

# bir sayfaya gitmek için GET("bir internet sayfa adresi")
tarayc.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")

time.sleep(2)

# tarayıcının boyutunu alalım. Bu işlem için GET_WINDOW_SIZE() ile alınan sözlükten GET('width') GET('height')
boyutlar = tarayc.get_window_size()
genislik = boyutlar.get('width')
yukseklik = boyutlar.get('height')
print(f"Tarayıcının genişliği {genislik} px, yüksekliği {yukseklik} px'dir")

# tarayıcıya yeni bir boyut belirleyelim. Ayar SET_WINDOW_SIZE(a, b)
tarayc.set_window_size(500, 100)

time.sleep(2)

# tarayıcının konumunu alalım. Ekranda padding_left ve padding_top değerlerini almak için GET_WINDOW_POSITION()
position = tarayc.get_window_position()
x = position.get('x')       # soldan uzaklık
y = position.get('y')       # sağdan uzaklık
print(f"Tarayıcının soldan uzaklığı {x} px, üstten {y} px'dir")

time.sleep(2)

# tarayıcıya yeni konum belirleyelim.Yeni padding_left ve padding_top değerlerini vermek için SET_WINDOW_POSITION()
tarayc.set_window_position(960, 540)

time.sleep(2)

# tarayıcıyı ekranı kapla. Tam ekranı kaplaması için MAXIMIZE_WINDOW()
tarayc.maximize_window()

# tarayıcıyı ekrandan al. Ekranı indirmek için MINIMIZE_WINDOW()
tarayc.minimize_window()

# tarayıcının ekranı tamamen kaplaması. Tüm ekranı kaplaması için FULLSCREEN_WINDOW()
tarayc.fullscreen_window()

# ekran görüntüsü al. SAVE_SCREENSHOT("kaydedilecek klasör adresi")
tarayc.save_screenshot("./images/ekran-goruntusu.png")

time.sleep(2)

# tarayıcıyı kapat
tarayc.close()
