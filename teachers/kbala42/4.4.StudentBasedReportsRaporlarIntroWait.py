"""
Raporlar sayfasına girişte bekleme işlemini çözmek için selenium içinden ekleme yapıyoruz

https://www.selenium.dev/documentation/en/webdriver/waits/

"""

from selenium import webdriver
import settings
import  time

# Bekleme olayını çözmek için eklediğimiz sınıf
from selenium.webdriver.support.ui import WebDriverWait

# Şart sağlamayı kontrol için yineseleniumdan sınıf ekliyoruz
# expected_conditions için ec kısaltmasını kullanıyoruz
from selenium.webdriver.support import expected_conditions as ec

#By nesnesini eklemek için ekleme yapıyoruz
from selenium.webdriver.common.by import By

# nesne olştur ve değişkene at
driver = webdriver.Chrome(settings.driver_path)
# sayfayı maksimize yapıyoruz
driver.maximize_window()

#10 saniye bekle hata üret
driver.set_page_load_timeout(10)

try:
    # EBA' ya giriş yap
    driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")

    # e-devlet butonu dallanma elmanını selector ile tespit edip e-devlet sayfasına gidiyoruz
    driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()

    # TC no giriş kutusunu seçip oraya settings içindeki tc'yi giriyoruz
    driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)

    # e-devlet Şifresi alanını bularak  settings içindeki password'ü giriyoruz
    driver.find_element_by_id("egpField").send_keys(settings.password)

    # Giriş Yap butonunu tespit edip tıklatarak giriş yapıyoruz
    driver.find_element_by_xpath("//input[@name='submitButton']").click()
except:
    # tıklama sonrasısayfa 10 saniyede yüklenmedi
    print("Sayfa 10 saniyede yüklenmedi...")
    driver.refresh()

# SORUN ÇÖZÜMÜ: "EBA yükleniyor" mesajının gitmemesi (her sayfada karşılaşılabiliyor)
# "EBA yükleniyor" gidene kadar sayfayı yenile döngüsü

while True:

    # WebDrverWait sınıfından driver sayfasında 3 sn bekleyen 1 sık aralıkla kontrol yapan wait nesnesi üretiyoruz
    ebaWait= WebDriverWait(driver,timeout=5,poll_frequency=1)

    try:
        # generalPreloader elemanı kayboluncaya kadar 3 sn bekle
        ebaWait.until(ec.invisibility_of_element((By.ID,"generalPreloader")))
        break # gizlendi ise çık
    except:
        print("Çok ebledi. Sayfa yenileniyor...")
        driver.refresh()

wait= WebDriverWait(driver,timeout=3,poll_frequency=1)

# Bekleme işlemini şart sağlanana kadar devam ettiriyoruz
wait.until(
    # ec nesnesi tıklanabilir oluncaya kadar
    ec.element_to_be_clickable(
        (By.XPATH, "//div[@class='vc-lm-item-title][normalize-space()='Raporlar']"))
).click() # Bu satırda hata verdi. Diğer kısımlar normal. 5. güne bırakıldı

# 2 saniye bekletiyoruz
time.sleep(2)

# Sayfayı kapatıyoruz
driver.close()