"""
Raporlar menüsünden Çalışma Raporlarını Tıklatıyoruz
"""
import settings
from classes.Eba import EBA
from classes.Browser import Browser

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

# tarayıcı nesnesini driver_path ile settings'de belirlenen yola göre oluşturuyoruz
browser = Browser(settings.driver_path)
# get metodu ile webdriver nesnesi oluşturuyoruz
driver = browser.get()

# eba nesnesini EBA sınıfından oluşturuyoruz
eba = EBA(driver)

# "EBA" sınıfında ki yazılan login metodu ile EBA'ya giriş apıyoruz
eba.login(settings.tc, settings.password)

# Sol menüden 'Raporlar' menüsüne tıklatıyoruz
reportsMenu = eba.wait.until(ec.element_to_be_clickable(
    (By.XPATH, "//div[@class='vc-lm-item-title '][normalize-space()='Raporlar']")
))
reportsMenu.click()

# 'Raporlar' sayfasında 'Çalışma Raporları' bağlantısını tıklatıyoruz
workReports = eba.wait.until(ec.element_to_be_clickable(
    (By.XPATH, "//div[text()='Çalışma Raporları']")
))
workReports.click()

# Bu sayfanın yüklendiğinden emin olmak için tablo satırları yüklenene kadar bekliyoruz
# Sayfada Çalışma raporları yoksa bu metot kullanılırsa sayfa sonsuz döngüye girer.
# Bu durumda bu satırı yorum satırı yapın.
# eba.table_is_loaded()

time.sleep(2)
