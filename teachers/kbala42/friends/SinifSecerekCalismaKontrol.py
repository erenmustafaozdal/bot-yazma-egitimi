"""
SinifSecerekCalismaKontrol
Aytaç Kula
"""
from selenium import webdriver
import settings
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def altincisinif():
    driver = webdriver.Chrome(settings.driver_path)
    driver.maximize_window()

    driver.set_page_load_timeout(10)

    try:
        driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
        driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()
        driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)
        driver.find_element_by_id("egpField").send_keys(settings.password)
        driver.find_element_by_xpath("//input[@name='submitButton']").click()
    except:
        print("Sayfa 10 saniyede yüklenemedi...")
        driver.refresh()

    while True:
        eba_wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
        try:
            eba_wait.until(ec.invisibility_of_element((By.ID, "generalPreloader")))
            break
        except:
            print("Çok bekledi. Sayfa yenileniyor...")
            driver.refresh()

    wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, "//div[@class='vc-lm-item-title '][normalize-space()='Raporlar']"))).click()
    time.sleep(2)

    driver.find_element_by_xpath(
        "//body/div[@id='indexBaseContainer']/div[@class='vc-fullHeight ng-scope']/div[@class='ng-scope']/div[@id='componentMainView']/div[@class='vc-fullHeight vc-background']/div[@id='componentMainSubView']/div[@role='main']/div[@class='vc-router-content ng-scope']/div[@id='vcReportsController']/div[@class='vc-layout-view-content-padding-headerless']/div[@class='p-w-xs']/div[@class='display-flow-root-class row']/div[1]/div[1]/div[1]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[@id='target1']//div[1]").click()
    time.sleep(5)

    driver.find_element_by_xpath("//div[contains(text(),'704')]").click()
    time.sleep(15)
    driver.find_element_by_xpath(
        "//i[@class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(text(),'848')]").click()
    time.sleep(15)
    driver.find_element_by_css_selector(
        "i[class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)

    driver.close()


def yedincisinif():
    driver = webdriver.Chrome(settings.driver_path)
    driver.maximize_window()

    driver.set_page_load_timeout(10)

    try:
        driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
        driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()
        driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)
        driver.find_element_by_id("egpField").send_keys(settings.password)
        driver.find_element_by_xpath("//input[@name='submitButton']").click()
    except:
        print("Sayfa 10 saniyede yüklenemedi...")
        driver.refresh()

    while True:
        eba_wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
        try:
            eba_wait.until(ec.invisibility_of_element((By.ID, "generalPreloader")))
            break
        except:
            print("Çok bekledi. Sayfa yenileniyor...")
            driver.refresh()

    wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, "//div[@class='vc-lm-item-title '][normalize-space()='Raporlar']"))).click()
    time.sleep(2)

    driver.find_element_by_xpath(
        "//body/div[@id='indexBaseContainer']/div[@class='vc-fullHeight ng-scope']/div[@class='ng-scope']/div[@id='componentMainView']/div[@class='vc-fullHeight vc-background']/div[@id='componentMainSubView']/div[@role='main']/div[@class='vc-router-content ng-scope']/div[@id='vcReportsController']/div[@class='vc-layout-view-content-padding-headerless']/div[@class='p-w-xs']/div[@class='display-flow-root-class row']/div[1]/div[1]/div[1]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[@id='target1']//div[1]").click()
    time.sleep(5)

    driver.find_element_by_xpath("//option[@label='7. Sınıf']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//option[@label='Fen Bilimleri']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//option[@label='Tüm Dersler']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[@class='text-left'][normalize-space()='1']").click()
    time.sleep(15)
    driver.find_element_by_css_selector(
        "i[class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(text(),'15')]").click()
    time.sleep(15)
    driver.find_element_by_css_selector(
        "i[class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(text(),'421')]").click()
    time.sleep(15)
    driver.find_element_by_css_selector(
        "i[class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(text(),'497')]").click()
    time.sleep(15)
    driver.find_element_by_css_selector(
        "i[class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)

    driver.close()


def sekizincisinif():
    driver = webdriver.Chrome(settings.driver_path)
    driver.maximize_window()

    driver.set_page_load_timeout(10)

    try:
        driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
        driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()
        driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)
        driver.find_element_by_id("egpField").send_keys(settings.password)
        driver.find_element_by_xpath("//input[@name='submitButton']").click()
    except:
        print("Sayfa 10 saniyede yüklenemedi...")
        driver.refresh()

    while True:
        eba_wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
        try:
            eba_wait.until(ec.invisibility_of_element((By.ID, "generalPreloader")))
            break
        except:
            print("Çok bekledi. Sayfa yenileniyor...")
            driver.refresh()

    wait = WebDriverWait(driver, timeout=3, poll_frequency=1)
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, "//div[@class='vc-lm-item-title '][normalize-space()='Raporlar']"))).click()
    time.sleep(2)

    driver.find_element_by_xpath(
        "//body/div[@id='indexBaseContainer']/div[@class='vc-fullHeight ng-scope']/div[@class='ng-scope']/div[@id='componentMainView']/div[@class='vc-fullHeight vc-background']/div[@id='componentMainSubView']/div[@role='main']/div[@class='vc-router-content ng-scope']/div[@id='vcReportsController']/div[@class='vc-layout-view-content-padding-headerless']/div[@class='p-w-xs']/div[@class='display-flow-root-class row']/div[1]/div[1]/div[1]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[@id='target1']//div[1]").click()
    time.sleep(5)

    driver.find_element_by_xpath("//option[@label='8. Sınıf']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//option[@label='Fen Bilimleri']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//option[@label='Tüm Dersler']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(text(),'172')]").click()
    time.sleep(15)
    driver.find_element_by_css_selector(
        "i[class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(text(),'440')]").click()
    time.sleep(15)
    driver.find_element_by_css_selector(
        "i[class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(text(),'77')]").click()
    time.sleep(15)
    driver.find_element_by_css_selector(
        "i[class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(text(),'83')]").click()
    time.sleep(15)
    driver.find_element_by_css_selector(
        "i[class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(text(),'838')]").click()
    time.sleep(15)
    driver.find_element_by_css_selector(
        "i[class='pull-left fa fa-3x fa-chevron-circle-left vc-ia-hand-cursor vc-color-blue m-r-sm']").click()
    time.sleep(5)

    driver.close()


while True:
    secim = int(input('''
    EBA Öğrenci Çalışma Raporlarına Bakma
    ---------------------------------------------------------------
    1 Altıncı Sınıf
    2 Yedinci Sınıf
    3 Sekizinci Sınıf 
    4 Tüm Sınıflar
    0 ÇIKIŞ
    Sınıf Seçiniz:

    '''))

    if secim == 0:
        break
    if secim == 1:
        altincisinif()
    if secim == 2:
        yedincisinif()
    if secim == 3:
        sekizincisinif()
    if secim == 4:
        altincisinif()
        yedincisinif()
        sekizincisinif()