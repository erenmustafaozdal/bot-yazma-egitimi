"""
3. Aşamada E-devlet'ten giriş yaptıktan sonra EBA sayfasına dönüyoruz.

"""

from selenium import webdriver
import settings
import  time

# nesne olştur ve değişkene at
driver = webdriver.Chrome(settings.driver_path)
# sayfayı maksimize yapıyoruz
driver.maximize_window()

#EBA' ya giriş yap
driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")

# e-devlet butonu dallanma elmanını selector ile tespit edip e-devlet sayfasına gidiyoruz
driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()

#TC no giriş kutusunu seçip oraya settings içindeki tc'yi giriyoruz
driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)

# e-devlet Şifresi alanını bularak  settings içindeki password'ü giriyoruz
driver.find_element_by_id("egpField").send_keys(settings.password)

# Giriş Yap butonunu tespit edip tıklatarak giriş yapıyoruz
driver.find_element_by_xpath("//input[@name='submitButton']").click()

# 2 saniye bekletiyoruz
time.sleep(5)



# Sayfayı kapatıyoruz
driver.close()