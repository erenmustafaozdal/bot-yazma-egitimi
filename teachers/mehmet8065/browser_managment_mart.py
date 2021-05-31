"""
browser_management: Tarayıcı yönetimi
"""
from selenium import webdriver
import settings_example
import time

# tarayıcı nesnesini oluştıralım
driver= webdriver.Chrome(settings_example.driver_path)
# bir sayfaya git
driver.get("https://wordwall.net/tr/myactivities")
time.sleep(2)
# Tarayıcının boyutunu belirleyelim
size = driver.get_window_size()
width= size.get("width")
height= size.get("height")
print("Tarayıcının genişliği= {} pxl Yüksekliği {} pxl'dir.".format(width,height))

# Pencere boyutu ayarlayalım
driver.set_window_size(500,100)
time.sleep(2)

# Tarayıcıya konum öğrenelim
position = driver.get_window_position()
x= position.get("x")
y= position.get("y")
print("Tarayıcının soldan uzaklığı= {} pxl üstten yüksekliği {} pxl'dir.".format(x,y))

# Tarayıcıya yeni konum belirle
driver.set_window_position(900,540)
time.sleep(3)

# Tarayıcıya ekranı kaplat
driver.maximize_window()

# Ekran görüntüsü al
driver.save_screenshot("./images/ekran-goruntusu.png")
time.sleep(2)


# tarayıcıyı kapat
driver.close()