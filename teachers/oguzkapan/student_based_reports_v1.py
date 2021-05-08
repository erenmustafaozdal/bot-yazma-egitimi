from selenium import webdriver
import settings
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


#pip install xlsxwriter

img_dir="./images/student-based-reports"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)


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


# tablo satırlarını al
def table_is_loaded():
    try:
       return wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='body-container']/div[@role='row']"))
            )
    except:
        print("Tablo yüklenemedi.")
        driver.refresh()
        return  table_is_loaded()



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


work_reports=wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Çalışma Raporları']"))
    )
work_reports.click()

# tablo satırlarını al
table_is_loaded()

student_based_reports_take=wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='ÖĞRENCİ BAZLI']")))
student_based_reports_take.click()
time.sleep(2)
driver.find_element_by_xpath("//option[contains(text(),'11. Sınıf')]").click()
time.sleep(2)
driver.find_element_by_xpath("//option[@label='AMP - 11. Sınıf / A Şubesi (BİLİŞİM TEKNOLOJİLERİ ALANI)']").click()
time.sleep(2)
driver.find_element_by_xpath("//option[@label='Grafik ve Animasyon']").click()
time.sleep(2)

""" 

//option[@label='Web Tasarım ve Programlama']

//option[text()='11. Sınıf']

//option[contains(text(),'11. Sınıf')]

"""


students=table_is_loaded()

student_count=len(students)

for student_i in range(student_count):
    students=table_is_loaded()
    students[student_i].click()

    #çalışma satırlarını al
    works=table_is_loaded()
    student_name=driver.find_element_by_xpath("//div[@class='vc-font-size-x-large m-l-sm ng-binding']").text

    completes=[]
    performances=[]

    for work_i in range(4):
       complete= works[work_i].find_element_by_xpath(".//div[@id='vcProgressBar']//span").text
       completes.append(int(complete.replace("%","")))
    performance=works[work_i].find_element_by_xpath(".//div[@id='multiColouredProgress']//span").text
    if performance!='-':
        performances.append(int(performance))
    complete_avg=sum(completes) / len(completes)
    performance_avg="performans yok";
    if len(performances)>0:
        performance_avg=sum(performances)/len(performances)

    img_path=f"{img_dir}/{student_name}.png"
    driver.find_element_by_xpath("//div[@class='vc-layout-view-content-padding']").screenshot(img_path)



    print("*"*50)
    print("Öğrenci : " ,student_name)
    print("--Tamamlama : ",complete_avg)
    print("--Performans : ", performance_avg)

    driver.back()




# //div[contains(@class,'vc-lm-item-title')][normalize-space()='Raporlar']

# div[id='3e4fc4a8-9d2f-3518-e3d2-5cf3f3bdb571'] div[class='vc-lm-item-title ']

# driver.find_element_by_xpath("//div[contains(@class,'vc-lm-item-title')][normalize-space()='Raporlar']").click()

time.sleep(2)
driver.close()