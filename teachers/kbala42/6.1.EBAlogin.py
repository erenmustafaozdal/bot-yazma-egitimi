"""
Yeni üretilen sınıflardan sade bir şekilde giriş nasıl yapıldığı gösterilmiştir.
İşlemin başarılı olduğunu göstermek için time eklenmiştir
"""
# Aynı şekilde settings değerlerini okuyoruz
import settings
# Eaa dosyasından EBA sınıfını alıyoruz
from classes.Eba import EBA
# Browser dosyasından Browser sınıfını alıyoruz
from classes.Browser import Browser
import time

# tarayıcı nesnesini driver_path ile settings'de belirlenen yola göre oluşturuyoruz
browser = Browser(settings.driver_path)
# get metodu ile webdriver nesnesi oluşturuyoruz
driver = browser.get()

# eba nesnesini EBA sınıfından oluşturuyoruz
eba = EBA(driver)

# "EBA" sınıfında ki yazılan login metodu ile EBA'ya giriş apıyoruz
eba.login(settings.tc, settings.password)

# 2. saniye web sayfasını bekletiyoruz
time.sleep(2)