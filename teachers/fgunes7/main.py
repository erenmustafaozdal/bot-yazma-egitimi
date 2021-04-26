from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import settings
import time

# Öğrenci numarasını iste
Ogrenci_Numarası = input("Öğrenci Numarasını Giriniz: ")

# Mebbise bağlan
driver = webdriver.Chrome(settings.driver_path)
driver.maximize_window()
driver.get("https://mebbis.meb.gov.tr/")

# Kullanıcı adı ve parola girişi
KulllaniciAdi = driver.find_element_by_id("txtKullaniciAd").send_keys("41266429914")
Parola = driver.find_element_by_id("txtSifre").send_keys("Atg+5858" + Keys.ENTER)

# E-okul bölümüne giriş
Eokul = driver.find_element_by_xpath("//*[@id='team']/div/div/div[2]/div/div/div[1]/div/div/p/a/img")
hover = ActionChains(driver).move_to_element(Eokul).perform()
EokulLink = driver.find_element_by_id("rptProjeler_ctl01_rptKullanicilar_ctl00_LinkButton1").click()
driver.close()

# Açılan pencereye geçiş
driver.switch_to.window(driver.window_handles[-1])

# İlkokul-ortaokul öğrenci işlemleri
Ogrenci_Islemleri = driver.find_element_by_xpath('//*[@id="mdlIOO"]').click()

# Öğrenci numarası girişi
Ogrenci_No = driver.find_element_by_id("OGRMenu1_txtTC").send_keys(Ogrenci_Numarası)

# Öğrenci ara
ara = driver.find_element_by_id("OGRMenu1_btnAra").click()

# Öğrenciyi kontrol et
url = "https://e-okul.meb.gov.tr/IlkOgretim/OGR/IOG01001.aspx"
if url == driver.current_url:
    print("Bu numarada öğrenci bulunamadı...")
else:
    # rapo al
    rapor = driver.find_element_by_xpath('//*[@id="IOMToolbarActive1_print_b"]/img').click()
    driver.close()

    driver.switch_to.window(driver.window_handles[-1])
    driver.maximize_window()
    time.sleep(1)

    # pdf göstericiyi seç
    sec = driver.find_element_by_xpath('//*[@id="gosterici"]/option[1]').click()

    # öğrenci belgesi al
    belge = driver.find_element_by_xpath('//*[@id="tableRaporlar"]/tbody/tr[2]/td[1]/img').click()
    time.sleep(2)

    # öğrenci belgesini aç
    driver.get("https://reporteokul.meb.gov.tr/rdcrptserver.aspx?viewer=java&vfmt=encp&vgen=304&pversion=3&language=tr-TR&promptOnRefresh=1&cmd=exportd&export_fmt=crxf_pdf:0")

    # öğrenci belgesini yazdır
    yazdir = driver.execute_script('window.print();')
    time.sleep(5)

driver.quit()



