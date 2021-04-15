from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\lenovo\\Desktop\\driver\\chromedriver.exe")

driver.get("https://istanbulakademi.meb.gov.tr/")

driver.close()