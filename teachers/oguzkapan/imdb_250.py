"""
find_elements:  sayfa elemanlarını bulup işlemler yapacağız
"""
from selenium import webdriver
import settings
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(settings.driver_path)
url="https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start="


page_count=1
tum_bilgiler=[]
while page_count<=250:
    new_page = url + str(page_count)
    browser.get(new_page)
    elements = browser.find_elements_by_css_selector("div.lister-item-content")
    for element in elements:
        print("***************************")
        ## print(element.text)
        """
        print(element.find_element_by_tag_name("h3").text)
        print(element.find_element_by_css_selector("span.runtime").text)
        print(element.find_element_by_css_selector("div.inline-block.ratings-imdb-rating").text)
        """
        film_name=element.find_element_by_tag_name("h3>a").text
        sure=element.find_element_by_css_selector("span.runtime").text
        oran=element.find_element_by_css_selector("div.inline-block.ratings-imdb-rating").text
        bilgi=str(page_count)+"-"+film_name+"- süre:"+sure+"- oran:"+oran
        print(bilgi)
        tum_bilgiler.append(bilgi)
        page_count+=1


page_count = 1
with open("imdb_top_250.txt", "w", encoding="UTF-8") as file:
    for top_250_film_bilgi in tum_bilgiler:
        file.write(top_250_film_bilgi + "\n")
        file.write("****************************************\n")
        page_count += 1

browser.close()
