"""
mustafa kaplan
browser_management: Tarayıcı yönetimi
"""
from selenium import webdriver
import settings
import time

# tarayıcı nesnesini oluşturalım
driver = webdriver.Chrome(settings.driver_path)

# bir sayfaya git
driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")

time.sleep(2)

# tarayıcının boyutunu alalım
# size = driver.get_window_size()
# width = size.get('width')
# height = size.get('height')
# print("Tarayıcının genişliği {} px, yüksekliği {} px'dir".format(width, height))

# tarayıcıya yeni bir boyut belirleyelim
driver.set_window_size(500, 100)

time.sleep(2)

# tarayıcının konumunu alalım
position = driver.get_window_position()
x = position.get('x')
y = position.get('y')
print("Tarayıcının soldan uzaklığı {} px, üstten {} px'dir".format(x, y))

time.sleep(2)

# tarayıcıya yeni konum belirleyelim
driver.set_window_position(960, 540)

time.sleep(2)

# tarayıcıyı ekranı kapla
driver.maximize_window()

# ekran görüntüsü al
driver.save_screenshot("./images/ekran-goruntusu.png")

time.sleep(2)

# tarayıcıyı kapat
driver.close()
