"""
multi_browser:  Birden çok tarayıcı ile işlem yapılan dosya
"""

from selenium import webdriver

import settings


#driver=webdriver.Chrome(executable_path=settings.driver_path)

firefox_driver=webdriver.Firefox(executable_path=settings.firefox_driver_path)

firefox_driver.get("https://istanbulakademi.meb.gov.tr/")  # websayfasını getir.


firefox_driver.close()