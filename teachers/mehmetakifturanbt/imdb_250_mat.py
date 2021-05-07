from selenium import webdriver
import settings


browser = webdriver.Chrome(settings.driver_path)
url="https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start="


page_count=1
tum_bilgiler=[]
while page_count<=50:
    new_page = url + str(page_count)
    browser.get(new_page)
    elements = browser.find_elements_by_css_selector("div.lister-item-content")
    for element in elements:

        # print(element.text)
        """
        print(element.find_element_by_tag_name("h3").text)
        print(element.find_element_by_css_selector("span.runtime").text)
        print(element.find_element_by_css_selector("div.inline-block.ratings-imdb-rating").text)
        """
        film_name=element.find_element_by_tag_name("h3>a").text
        sure=element.find_element_by_css_selector("span.runtime").text
        oran=element.find_element_by_css_selector("div.inline-block.ratings-imdb-rating").text
        degerler = [len(film_name),len(sure),len(oran)]
        maximum = (max(degerler))
        bilgi=str(page_count)+" | "+film_name+" | Süre : "+sure+" | Oran : "+oran
        bilgi2=f"{page_count} | {((maximum+7)-(len(str(page_count))))*'~'}\nFilm\t: {film_name}\nSüre\t: {sure}\nOran\t: {oran}"
        print(len(bilgi)*"~")
        print(bilgi)
        tum_bilgiler.append(bilgi2)
        page_count+=1


page_count = 1
with open("imdb_top_250_mat.txt", "w", encoding="UTF-8") as file:
    for top_250_film_bilgi in tum_bilgiler:
        file.write(top_250_film_bilgi + "\n")
        bolum = top_250_film_bilgi.split("\n")
        #print(bolum[0])
        file.write(len(bolum[0])*"~"+"\n\n")
        page_count += 1

browser.close()
