from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Chrome(settings.driver_path)
driver.get("https://eba.gov.tr/")
driver.maximize_window()

driver.find_element_by_xpath("//a[contains(text(),'ÖĞRETMEN')]").click()
