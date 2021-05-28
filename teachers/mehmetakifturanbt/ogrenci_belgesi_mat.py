from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import settings
import time

# Yazdırma işlemi yapmak için "--kiosk-printing" ayarı
chrome_ayarla = webdriver.ChromeOptions()
chrome_ayarla.add_argument('--kiosk-printing')

# Öğrenci numarasını iste
ogrNumarasi = input("Öğrenci Numarasını Giriniz: ")

# Mebbise bağlan
driver = webdriver.Chrome(options=chrome_ayarla, executable_path=settings.driver_path)
driver.maximize_window()
driver.get("https://mebbis.meb.gov.tr/")
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

# Kullanıcı adı ve parola girişi
kullaniciAdi = driver.find_element_by_id("txtKullaniciAd").send_keys(settings.tc)
kullaniciSifre = driver.find_element_by_id("txtSifre").send_keys(settings.password + Keys.ENTER)

# E-okul bölümüne giriş
# E-okul logosunun üzerine gelme
eokul = driver.find_element_by_xpath("//*[@id='team']/div/div/div[2]/div/div/div[1]/div/div/p/a/img")
hover = ActionChains(driver).move_to_element(eokul).perform()

# E-okul linkine tıklama
eokulLink = driver.find_element_by_id("rptProjeler_ctl01_rptKullanicilar_ctl00_LinkButton1").click()
driver.close()

# Açılan pencereye geçiş
driver.switch_to.window(driver.window_handles[-1])

# Ortaoöğretim öğrenci işlemleri
ogrenciIslemleri = driver.find_element_by_xpath('//*[@id="mdlOOO"]').click()

# Öğrenci numarası girişi
ogrNo = driver.find_element_by_xpath("//input[@id='txtOkulNo']").send_keys(ogrNumarasi)

# Öğrenci ara
ogrAra = driver.find_element_by_xpath("//button[normalize-space()='Ara']").click()
time.sleep(1)

# Öğrenciyi kontrol et
bilgi_mesaj = driver.find_element_by_xpath("//div[@id='tbPageDataTable_info']").get_attribute("innerHTML")
print(bilgi_mesaj)
if bilgi_mesaj == "Görüntülecek Kayıt Bulunamadı":
    print("Bu numarada öğrenci bulunamadı...")
    time.sleep(2)
else:
    # rapor al
    # Sayfayı kaydırmadan öğrenci ismine tıklanmıyor.
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    ogrenci_sayfa = wait.until(ec.element_to_be_clickable(
        (By.XPATH, "//i[@class='fas fa-folder']")
    ))
    ogrenci_sayfa.click()

    ogrRapor = driver.find_element_by_xpath("//img[@alt='Yazdır']").click()
    driver.close()

    driver.switch_to.window(driver.window_handles[-1])
    driver.maximize_window()
    time.sleep(1)

    # pdf göstericiyi seç
    sec = driver.find_element_by_xpath('//*[@id="gosterici"]/option[1]').click()

    # öğrenci belgesi al
    ogrBelge = driver.find_element_by_xpath('//*[@id="tableRaporlar"]/tbody/tr[2]/td[1]/img').click()
    time.sleep(2)

    # öğrenci belgesini iframe dışında aç
    driver.get("https://reporteokul.meb.gov.tr/rdcrptserver.aspx?viewer=java&vfmt=encp&vgen=304&pversion=3&language=tr-TR&promptOnRefresh=1&cmd=exportd&export_fmt=crxf_pdf:0")

    # öğrenci belgesini yazdır
    driver.execute_script('window.print();')
    time.sleep(30)

# tarayıcıyı kapat
driver.quit()



