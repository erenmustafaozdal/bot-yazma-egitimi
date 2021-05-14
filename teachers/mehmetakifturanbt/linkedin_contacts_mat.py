"""
Linkedin sitesindeki bağlantıları kaydetmek
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import settings
import time

def page_scroll(second):
    SCROLL_PAUSE_TIME = second

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

driver = webdriver.Chrome(settings.driver_path)

driver.get("https://www.linkedin.com/")

driver.maximize_window()
time.sleep(1)

email = driver.find_element_by_xpath("//*[@id='session_key']")
password = driver.find_element_by_xpath("//*[@id='session_password']")

email.send_keys(settings.linkedin_mail)
password.send_keys(settings.linkedin_parola)
password.send_keys(Keys.ENTER)
time.sleep(2)

try:
    not_now_button = driver.find_element_by_xpath('//*[@id="remember-me-prompt__form-secondary"]/button')
    not_now_button.click()
except:
    print("Giriş yapılmış")

# Arama kutusu kullanma alıştırması
# search_bar = driver.find_element_by_xpath("//input[@placeholder='Arama Yap']")
# search_bar.send_keys("#python")
# search_bar.send_keys(Keys.RETURN)

driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")

# for i in range(1, 20):
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(3)

page_scroll(3)

contacts = driver.find_elements_by_class_name("mn-connection-card__details")
contactList=[]

for contact in contacts:
    contactList.append(contact.text)
    print(contact.text)
print(len(contactList))
with open("./txts/linkedin_contacts_mat.txt", "w", encoding="UTF-8") as file:
    for contact in contactList:
        file.write(contact + "\n")
time.sleep(5)

driver.quit()
















