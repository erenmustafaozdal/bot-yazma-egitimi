"""
multi_browser:  Birden çok tarayıcı ile işlem yapılan dosya
"""

from selenium import webdriver

import settings


driver=webdriver.Chrome(executable_path=settings.driver_path)

driver.get("https://istanbulakademi.meb.gov.tr/") # websayfasını getir.


driver.close()