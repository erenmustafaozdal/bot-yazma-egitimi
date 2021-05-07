from selenium import webdriver
import settings
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




def left_menu_is_loaded():
    try:
        wait.until(EC.visibility_of_all_elements_located((By.ID,"vc-treeleftmenu")))
    except:
        print("Menu yüklenirken çok bekledi. Sayfa yenileniyor...")
        driver.refresh()
        left_menu_is_loaded()

def login(tc,password):
    driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
    if 'VCollabPlayer' in driver.current_url:
        return
    driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()
    driver.find_element_by_css_selector("#tridField").send_keys(settings.tc)
    driver.find_element_by_id("egpField").send_keys(settings.password)
    try:
        driver.find_element_by_xpath("//input[@name='submitButton']").click()
    except:
      print("Bazı hatalar:D::D - Özetle giriş yapılamadı")
      login(tc,password)
    else:
        left_menu_is_loaded()


driver=webdriver.Chrome(settings.driver_path)
driver.maximize_window()
driver.set_page_load_timeout(10)


# poll_frequbcey ne kadarda bir deneme yapılacak
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

login(settings.tc,settings.password)

reports_menu=wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'vc-lm-item-title')][normalize-space()='Raporlar']"))
    )
reports_menu.click()


# //div[contains(@class,'vc-lm-item-title')][normalize-space()='Raporlar']

# div[id='3e4fc4a8-9d2f-3518-e3d2-5cf3f3bdb571'] div[class='vc-lm-item-title ']

# driver.find_element_by_xpath("//div[contains(@class,'vc-lm-item-title')][normalize-space()='Raporlar']").click()

time.sleep(2)
driver.close()

driver.close()