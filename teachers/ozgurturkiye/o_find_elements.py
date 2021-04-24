import time
from selenium import webdriver
import settings

# driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
driver = webdriver.Chrome(executable_path=settings.chrome_driver_path)

# driver = webdriver.Firefox(executable_path='./drivers/geckodriver2')
# driver = webdriver.Firefox(executable_path=settings.firefox_driver_path)

driver.get('http://www.python.org')
driver.maximize_window()
time.sleep(2)

driver.close()
