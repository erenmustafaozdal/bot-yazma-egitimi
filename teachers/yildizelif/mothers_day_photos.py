from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(settings.driver_path)
driver.get("https://tr.pixiz.com/template/4677")
#class Document(models.Model):
#docfile = models.FileField(upload_to='documents/', max_length=5234,blank=True, null=True,)

driver.find_element_by_xpath("//label[@class='upload-popup-button tooltip tooltipstered']").click()
driver.find_element_by_css_selector("#pop-import-button").click()


#time.sleep(5)
#driver.close()

