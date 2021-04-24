"""
elementleri_bulmak: İnternet sayfasında bulunan elementlere ulaşıp bu elementlerle ilgili işlemler
"""

from selenium import webdriver
import settings
import time


tarayc = webdriver.Chrome(settings.surucu_yolu)

tarayc.get("https://istanbulakademi.meb.gov.tr/")
tarayc.maximize_window()
#
# # Sayfada class adı ile eleman(lar)a ulaşmak için find_element_by_CLASS_NAME("sınıfın adı")
eleman = tarayc.find_element_by_class_name("btn-warning")
eleman.click()  # bu elaman bir buton olduğu için CLICK() tıkladık

# Sayfada id ile elemana ulaşmak için find_element_by_ID("id adı")
tarayc.get("https://istanbulakademi.meb.gov.tr/akademiler.php?pID=615")
formu_sec = tarayc.find_element_by_id("choice_form")
print(formu_sec)    # formdan id si 'choice_form' olan elemanı seçtim (NESNE)
print(formu_sec.text)   # seçtiğim nesnenin metnini yazdırdım


# Sayfada name özniteliği ile elemana ulaşmak için find_element_by_NAME("öznitelik adı")
anahtar_kelimeler = tarayc.find_element_by_name("keywords")
print(anahtar_kelimeler) # sayfanın meta etiketlerinden name özniteliği 'keywords' olan elemanı seçtim (nesne)
# ulaştığımız nesnenin diğer özniteliklerini alabiliriz. Bunun için nesne.GET_ATTRIBUTE("öznitelik adı")
print(anahtar_kelimeler.get_attribute("content"))


""" Sayfadaki bir bağlantı metni (link) ile elemana ulaşmak için LINK_TEXT("link için kullanılan metin") 
Ancak bu metin birebir aynısı (boşluk, - vb karakterler dahil) olmalı. Bunu aşmak için PARTIAL_LINK_TEXT """
link = tarayc.find_element_by_link_text("Teknoloji Akademisi")  # Bağlantıyı seçtim ve değişkene aktardım
link.click()    # Bağlantıyı tıklamak için değişken.CLICK()
time.sleep(2)

""" Bağlantı metninin bir kısmı (kısmi bağlantı metni) ile elemana ulaşmak için 
PARTIAL_LINK_TEXT("linke ait metnin bir kısmı")"""
link = tarayc.find_element_by_partial_link_text("Hata")
link.click()

# etiket adı ile elemana ulaşma
name = tarayc.find_element_by_tag_name("input")
name.send_keys("Eren Mustafa ÖZDAL")

# css seçici ile elemana ulaşma CSS_SELECTOR

email = tarayc.find_element_by_css_selector("#sender_email")
email.send_keys("ali@gmail.com")
time.sleep(2)
email.clear()
email.send_keys("eren.060737@gmail.com")

time.sleep(2)

# xpath seçici ile elemana ulaşma
address = tarayc.find_element_by_xpath('//ul[@class="v-list"]/li[1]')
print(address.text)



# tarayıcıyı kapat
tarayc.close()