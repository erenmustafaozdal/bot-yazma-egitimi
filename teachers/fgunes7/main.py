from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import settings
import time

driver = webdriver.Chrome(settings.driver_path)
driver.maximize_window()
driver.get("https://mebbis.meb.gov.tr/")

KulllaniciAdi = driver.find_element_by_id("txtKullaniciAd").send_keys("41266429914")

Parola = driver.find_element_by_id("txtSifre").send_keys("Atg+5858" + Keys.ENTER)

Eokul = driver.find_element_by_xpath("//*[@id='team']/div/div/div[2]/div/div/div[1]/div/div/p/a/img")
hover = ActionChains(driver).move_to_element(Eokul).perform()

link = driver.find_element_by_id("rptProjeler_ctl01_rptKullanicilar_ctl00_LinkButton1").click()

time.sleep(1)

driver.get("https://e-okul.meb.gov.tr/IlkOgretim/OGR/IOG01001.aspx")
driver.switch_to.window(driver.current_window_handle)
time.sleep(1)

Ogrenci_No = driver.find_element_by_id("OGRMenu1_txtTC").send_keys("12")
ara = driver.find_element_by_id("OGRMenu1_btnAra").click()
rapor = driver.find_element_by_xpath('//*[@id="IOMToolbarActive1_print_b"]/img').click()
driver.switch_to.window(driver.current_window_handle)
time.sleep(1)
driver.get("https://reporteokul.meb.gov.tr/rapor_arayuz.aspx")
sec = driver.find_element_by_xpath('//*[@id="gosterici"]/option[1]').click()
belge = driver.find_element_by_xpath('//*[@id="tableRaporlar"]/tbody/tr[2]/td[1]/img').click()
time.sleep(10)
yazdir = driver.find_element_by_xpath('//*[@id="print"]').click()






