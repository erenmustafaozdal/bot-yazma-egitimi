"""
BrowserManagement: Tarayıcı yönetimi
"""
from selenium import webdriver
import settings
import time

# driver adında bir Chrome nesnesi oluşturuyoruz
driver = webdriver.Chrome(settings.driver_path)

# Girilen adrese gidiyoruz
driver.get("https://istanbulakademi.meb.gov.tr")

# Tarayıcının boyutlarını alıp size değişkeninde saklıyoruz
size= driver.get_window_size()
# Aldığımız boyutları console penceresinde yazdırıyoruz
print(size)
# Taraycının geniliğini alıp width değişkeninde saklıyoruz
width = size.get("width")
# Tarayıcının yüksekliğini alıp height değişkeninde saklıyoruz
height = size.get("height")
# Elde ettiğimiz değişkenleri formata uygun olarak console penceresinde yazdırıyoruz
print("Tarayıcının genişliği {} px, yüksekliği {} px dir".format(width,height))

# tarayıcıya yeni boyut belirliyoruz
driver.set_window_size(500,100)
time.sleep(2)

# tarayıcının konumunu alıyoruz
position= driver.get_window_position()
# Elde ettiğimiz konumu console penceresinde yazdırıyoruz
print(position)
# Taraycının x pozisyonunu alıp x değişkeninde saklıyoruz
x = position.get("x")
# Taraycının y pozisyonunu alıp y değişkeninde saklıyoruz
y = position.get("y")
# Elde ettiğimiz değişkenleri formata uygun olarak console penceresinde yazdırıyoruz
print("Tarayıcının soldan uzaklığı {} px, üstten uzaklığı {} px dir".format(x,y))
time.sleep(2)

# Tarayıcımıza yeni bir konum belirliyoruz
driver.set_window_position(500,420)
time.sleep(2)

# Tarayıcımıza ekranı kaplatıyoruz
driver.maximize_window()

# Ekran görüntüsünü alıp images klasöründe ekran_goruntusu.png adıyla kaydediyoruz
driver.save_screenshot("./images/ekran_goruntusu.png")
time.sleep(2)


# Tarayıcımızı kapatıyoruz
driver.close()
