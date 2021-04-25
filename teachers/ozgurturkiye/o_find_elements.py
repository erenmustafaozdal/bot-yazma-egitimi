import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import settings

driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
# driver = webdriver.Chrome(executable_path=settings.chrome_driver_path)

# driver = webdriver.Firefox(executable_path='./drivers/geckodriver2')
# driver = webdriver.Firefox(executable_path=settings.firefox_driver_path)


driver.maximize_window()


def close_modal(driver):
    print("close_modal func called")
    modal_button = driver.find_element_by_class_name("btn-warning")
    modal_button.click()


def get_btn_warning():
    print("get_btn_warning func called")
    driver.get('https://istanbulakademi.meb.gov.tr/')
    driver.maximize_window()
    modal_button = driver.find_element_by_class_name("btn-warning")
    # modal_button = driver.find_element(By.CLASS_NAME, "btn-warning")
    modal_button.click()
    # time.sleep(2)


def get_form_text_by_id():
    print("get_form_text func called")
    driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
    form = driver.find_element_by_id("choice_form")
    print("Form text:", form.text)


def get_element_by_name():
    print("get_element_by_name func called")
    driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
    close_modal(driver)
    page_keyword = driver.find_element_by_name("keywords")
    print("Page Keywords:", page_keyword.get_attribute("content"))


def get_element_by_link():
    print("get_element_by_link func called")
    driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
    close_modal(driver)
    link = driver.find_element_by_link_text("Teknoloji Akademisi")
    link.click()


def get_element_by_partial_link():
    print("get_element_by_partial_link func called.")
    driver.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
    close_modal(driver)
    link = driver.find_element_by_partial_link_text("Hata")
    link.click()


def get_element_by_tag_name():
    print("get_element_by_tag_name func called.")
    driver.get("https://istanbulakademi.meb.gov.tr/hata_bildir.php")
    close_modal(driver)
    element_name = driver.find_element_by_tag_name("input")
    element_name.send_keys("Ozgur By.")
    time.sleep(2)


def get_element_by_css_selector():
    print("get_element_by_css_selector func called.")
    driver.get("https://istanbulakademi.meb.gov.tr/hata_bildir.php")
    close_modal(driver)
    email = driver.find_element_by_css_selector("#sender_email")
    email.send_keys("ozgur@ozgur.com")
    time.sleep(2)


def take_screenshot():
    print("take_screenshot func called.")
    driver.get("https://istanbulakademi.meb.gov.tr/hata_bildir.php")
    close_modal(driver)
    driver.save_screenshot("./images/screenshot.png")


# get_btn_warning()
# get_form_text_by_id()
# get_element_by_name()
# get_element_by_link()
# get_element_by_partial_link()  # This function is not working correctly
# get_element_by_tag_name()
# get_element_by_css_selector()
take_screenshot()


driver.close()
print("Page closed...")