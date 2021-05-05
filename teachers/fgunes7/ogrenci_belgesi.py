# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import settings
import time

# Yazdırma işlemi yapmak için "--kiosk-printing" ayarı
chorme_ayarla = webdriver.ChromeOptions()
chorme_ayarla.add_argument('--kiosk-printing')

while True:
    # Öğrenci numarasını iste
    ogrNumarasi = input("Öğrenci Numarasını Giriniz: ")

    # Mebbise bağlan
    driver = webdriver.Chrome(options=chorme_ayarla, executable_path=settings.driver_path)
    driver.maximize_window()
    driver.get("https://mebbis.meb.gov.tr/")

    # Kullanıcı adı ve parola girişi
    driver.find_element_by_id("txtKullaniciAd").send_keys(settings.kullaniciAdi)
    driver.find_element_by_id("txtSifre").send_keys(settings.kullaniciSifre + Keys.ENTER)

    # E-okul bölümüne giriş
    # E-okul logosunun üzerine gelme
    eokul = driver.find_element_by_xpath("//*[@id='team']/div/div/div[2]/div/div/div[1]/div/div/p/a/img")
    hover = ActionChains(driver).move_to_element(eokul).perform()

    # E-okul linkine tıklama
    driver.find_element_by_id("rptProjeler_ctl01_rptKullanicilar_ctl00_LinkButton1").click()
    driver.close()

    # Açılan pencereye geçiş
    driver.switch_to.window(driver.window_handles[-1])

    # İlkokul-ortaokul öğrenci işlemleri
    driver.get("https://e-okul.meb.gov.tr/IlkOgretim/OGR/IOG01001.aspx")

    # Öğrenci numarası girişi
    driver.find_element_by_id("OGRMenu1_txtTC").send_keys(ogrNumarasi)

    # Öğrenci ara
    driver.find_element_by_id("OGRMenu1_btnAra").click()

    # Öğrenciyi kontrol et
    # öğrenci bulunursa e-okulun ürettiği url https://e-okul.meb.gov.tr/IlkOgretim/OGR/IOG02001.aspx
    # öğrenci bulunumazsa e-okulun ürettiği url https://e-okul.meb.gov.tr/IlkOgretim/OGR/IOG01001.aspx

    url = "https://e-okul.meb.gov.tr/IlkOgretim/OGR/IOG01001.aspx"
    if url == driver.current_url:
        print("Bu numarada öğrenci bulunamadı...")
    else:
        # rapor al
        driver.find_element_by_xpath('//*[@id="IOMToolbarActive1_print_b"]/img').click()
        driver.close()

        driver.switch_to.window(driver.window_handles[-1])
        driver.maximize_window()
        time.sleep(1)

        # pdf göstericiyi seç
        driver.find_element_by_xpath('//*[@id="gosterici"]/option[1]').click()

        # öğrenci belgesi al
        driver.find_element_by_xpath('//*[@id="tableRaporlar"]/tbody/tr[2]/td[1]/img').click()
        time.sleep(2)

        # öğrenci belgesini iframe dışında aç
        driver.get("https://reporteokul.meb.gov.tr/rdcrptserver.aspx?viewer=java&vfmt=encp&vgen=304&pversion=3&language=tr-TR&promptOnRefresh=1&cmd=exportd&export_fmt=crxf_pdf:0")

        # öğrenci belgesini yazdır
        driver.execute_script('window.print();')
        time.sleep(5)
        print("Öğrenci belgesi yazdırılıyor...")

    # tarayıcıyı kapat
    driver.quit()



