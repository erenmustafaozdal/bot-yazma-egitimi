from selenium import webdriver
import settings
import time
driver=webdriver.Chrome(settings.driver_path)

driver.get("https://istanbulakademi.meb.gov.tr/")
a=driver.find_element_by_xpath("//button[normalize-space()='Kapat']")
a.click()
#driver.get("https://istanbulakademi.meb.gov.tr/yonetim/MemEtk1006.php?aid=d6ee8e291d366e19&pID=631")
time.sleep(3)

b=driver.find_element_by_xpath("//a[@class='box btn btn-info']")
b.click()
c=driver.find_element_by_xpath("//a[contains(text(),'Kullanıcı Girişi')]")
c.click()
time.sleep(3)
d=driver.find_element_by_xpath("//input[@id='login_name']")
d.send_keys(settings.tc)
e=driver.find_element_by_xpath("//input[@id='login_pass']")
e.send_keys(settings.password)
c=input("ekran resmini giriniz")
f=driver.find_element_by_xpath("//input[@id='login_code']")
f.send_keys(c)
a=driver.find_element_by_xpath("//span[@class='btn-label']")
a.click()
time.sleep(3)
driver.maximize_window()
a=driver.find_element_by_xpath("//a[@class='box btn btn-info']")
a.click()
ay=driver.find_element_by_xpath("//a[normalize-space()='Yönetici Paneli (YP)']")
time.sleep(3)
ay.click()
a=driver.find_element_by_xpath("//a[@class='btn btn-block btn-default text-left'][contains(text(),'F-106 Kura İşlemleri')]")
a.click()
time.sleep(3)
a=driver.find_element_by_xpath("//select[@id='pID']")
a.click()
#time.sleep(3)
a=driver.find_element_by_xpath("//option[@value='631']")
a.click()
b=driver.find_element_by_xpath("//button[normalize-space()='Seç']")
b.click()
time.sleep(3)


for i in range(4,30):
    dene=driver.find_element_by_xpath("//tbody/tr/td[10]/button[1]")
    dene.click()
    time.sleep(10)


time.sleep(3)
driver.close()
#driver.find_element_by_xpath()
