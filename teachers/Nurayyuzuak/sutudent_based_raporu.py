from  selenium import webdriver
import settings
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec # as ile takma isim oluşturuldu
from selenium.webdriver.common.by import By


# tarayıcı nesnesi oluştur
driver = webdriver.Chrome(settings.driver_path)
driver.maximize_window()

# sayfanın tüklenmesini 10 sn kadar bekle yüklenmezse hata ver
driver.set_page_load_timeout(10)

# EBA'ya giriş yap
try:
    driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
    driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()
    driver.find_element_by_xpath("//input[@id='tridField']").send_keys(settings.tc)
    driver.find_element_by_id("egpField").send_keys(settings.password)
    driver.find_element_by_xpath("//input[@name='submitButton']").click()
except:
    # tıklama sonrası sayfa 10 saniyede yüklenemedi ise
    print("Sayfa 10 saniyede yüklenemedi...")
    driver.refresh()

# SORUN ÇÖZÜMÜ: "EBA yükleniyor" mesajının gitmemesi (her sayfada karşılaşılabiliyor)
# "EBA yükleniyor" gidene kadar sayfayı yenileme döngüsü
while True:
    eba_wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
    try:
        eba_wait.until(ec.invisibility_of_element((By.ID, "generalPreloader")))
        break # gizlendi ise döngüden çık
    except:
        print("Çok bekledi. Sayfa yenileniyor...")
        driver.refresh()


wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
# //div[@class='vc-lm-item-title '][normalize-space()='Raporlar']
# time.sleep(30)
wait.until(ec.element_to_be_clickable(
    (By.XPATH, "//div[@class='vc-lm-item-title '][normalize-space()='Raporlar']"))
).click()

time.sleep(2)
#tarayıcıyı kapat
driver.close()