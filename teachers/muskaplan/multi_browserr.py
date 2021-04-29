
"""
mustafa kaplan
multi_browser:  Birden çok tarayıcı ile işlem yapılan dosya
"""
# paketimizi içeri aktardık
from selenium import webdriver
import settings


# Chrome nesnesi oluşturalım
driver = webdriver.Chrome(executable_path=settings.driver_path)

# Firefox nesnesi oluşturalım
#driver = webdriver.Firefox(executable_path=settings.firefox_path)

# Internet Explorer nesnesi oluşturalım
#driver = webdriver.Ie(executable_path=settings.ie_path)

# multi_browser: birden çok tarayıcı ile işlem yapılan dosya

#paketimizi içeri aktaralım
import time


# bir adrese git
driver.get("https://istanbulakademi.meb.gov.tr/")


# bulunduğum adresi yazdıralım
print(driver.current_url)
time.sleep(2)

# opera nesnesi oluşturalım. Operayı kullanmak istemedigimden yorum yaptım
#driver = webdriver.Opera(executable_path=settings.drive_path)
#time.sleep(2)



# tarayıcıyı kapat
driver.close()


