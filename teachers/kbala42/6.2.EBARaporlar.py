"""
Raporlar menüsüne geçiyoruz
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

time.sleep(2)
