from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class EBA:
    """
    Her projede çalışan temel EBA işlemlerini yürütecek olan nesne
    """

    # EBA girişi hata sayfasını LOGIN_ERROR_URL değişkende saklıyoruz
    LOGIN_ERROR_URL = 'https://giris.eba.gov.tr/EBA_GIRIS/hata.jsp'

    # Gönderdiğimiz driver nesnesi parametre olarak geliyor
    def __init__(self, driver):
        """
        __init__ ile nesne oluşturulduğunda ilk tanımlama ve ayarlamalar yapılır

        :param driver: selenium webdriver tarayıcı nesnesi
        """

        # Gelen parametreden tarayıcı nesnesini oluşturuyoruz
        self.driver = driver

        # bekleme nesnesini tarayıcı nesnesinden 10s olarak 1 sn sıklıkla oluşturuyoruz
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    def left_menu_is_loaded(self):
        """
        "EBA yükleniyor" mesajının gitmemesi sorununun çözümü için sol menü yüklenene kadar bekle
        """

        try:
            self.wait.until(ec.visibility_of_element_located((By.ID, "vc-treeleftmenu")))
        except:
            print("Menünün yüklenmesi için çok bekledi. Sayfa yenileniyor...")
            self.driver.refresh()
            self.left_menu_is_loaded()

    def login(self, tc, password):
        """
        EBA'ya giriş yapma işlemini gerçekleştiren metot

        :param tc: kullanıcı e-devlet girişi için TC numarası
        :param password: kullanıcı e-devlet girişi için şifre
        """

        # Öğretmen girişi sayfasına git
        self.driver.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")

        # Eğer daha önceden giriş yapıldı ise fonksiyondan çık
        # 'VCollabPlayer' ifadesi EBA'ya giriş yaptıktan sonra
        # her URL'de olan ortak bir değerdir.
        # Geçerli URL içinde varlığı sorgulanarak,
        # giriş yapılıp yapılmadığı tespit edilir
        if 'VCollabPlayer' in self.driver.current_url:
            return

        # E-Devlet girişi tuşuna bas ve E-Devlet girişi sayfasına git
        self.driver.find_element_by_xpath("//button[@title='edevlet girişi']").click()

        # TC ve şifre yaz
        self.driver.find_element_by_css_selector("#tridField").send_keys(tc)
        self.driver.find_element_by_id("egpField").send_keys(password)

        # E-Devlet giriş formunu gönder.
        # Eğer sayfa yüklenemez veya başka bir hata alınırsa
        # giriş işlemini tekrar et.
        try:
            self.driver.find_element_by_xpath("//input[@name='submitButton']").click()
            current_url = self.driver.current_url

            #mevcut url sayfasında değişiklik oluncaya kadar ebliyor
            self.wait.until(ec.url_changes(current_url))

            # Eğer karşımıza "LOGIN_ERROR_URL" hata sayfası açılıyorsa tekrar giriş yapıyoruz
            if current_url == self.LOGIN_ERROR_URL:
                print('Hata sayfasına gitti. Tekrar giriş yapılacak.')
                self.login(tc, password) # Tekrar giriş yapıyoruz

            # Eğer canlı ders sayfası açılmışsa EBA'ya devam ediyoruz
            # Bunuda mevcut sayfada liveMiddleware yazısını kontrol ederek yapıyoruz
            elif 'liveMiddleware' in current_url:
                print("Canlı ders var. EBA'ya devam ediliyor.")
                #buton aktif oluncaya kadar bekliyor, ardından butonu tıklatıyoruz
                self.wait.until(ec.element_to_be_clickable((By.ID, "active-brand-button"))).click()
        except:
            print("Sayfa 20 saniyede yüklenemedi. Sayfa yenileniyor...")
            self.login(tc, password)
        else:
            # Eğer başarılı bir şekilde EBA'ya giriş
            # yapıldı ise sol menünün yüklenmesini bekle
            self.left_menu_is_loaded()

    def table_is_loaded(self):
        """
        Çeşitli EBA sayfalarında tablo satırlarının görünmesini bekleyen fonksiyon

        :return: Tablonun satırlarını döndürür
        """
        try:
            return self.wait.until(ec.visibility_of_all_elements_located(
                (By.XPATH, "//div[@class='body-container']/div[@role='row']")
            ))
        except:
            print("Tablo yüklenemedi. Sayfa yenileniyor...")
            self.driver.refresh()
            return self.table_is_loaded()
