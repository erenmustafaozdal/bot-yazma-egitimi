from selenium import webdriver
import settings
driver = webdriver.Chrome(settings.driver_path)
driver.get("https://tr.tradingview.com/chart/LNar1yW5/")
driver.maximize_window()
driver.save_screenshot("./images/ekran-goruntusu.png")
driver.close()
