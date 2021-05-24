from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class EBA:
    """
    Her projede çalışan temel EBA işlemlerini yürütecek olan nesne
    """

    # EBA girişi hata sayfası
    LOGIN_ERROR_URL = 'https://giris.eba.gov.tr/EBA_GIRIS/hata.jsp'

    def __init__(self, driver):
        """
        __init__ ile nesne oluşturulduğunda ilk tanımlama ve ayarlamalar yapılır

        :param driver: selenium webdriver tarayıcı nesnesi
        """

        # tarayıcı nesnesi
        self.driver = driver
        # bekleme nesnesi
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

            self.wait.until(ec.url_changes(current_url))

            # hata sayfası ise tekrar giriş yap
            if current_url == self.LOGIN_ERROR_URL:
                print('Hata sayfasına gitti. Tekrar giriş yapılacak.')
                self.login(tc, password)

            # canlı ders sayfası ise EBA'ya devam et
            elif 'liveMiddleware' in current_url:
                print("Canlı ders var. EBA'ya devam ediliyor.")
                self.wait.until(ec.element_to_be_clickable((By.ID, "active-brand-button"))).click()
        except:
            print("Sayfa 20 saniyede yüklenemedi. Sayfa yenileniyor...")
            self.login(tc, password)
        else:
            # Eğer başarılı bir şekilde EBA'ya giriş
            # yapıldı ise sol menünün yüklenmesini bekle
            self.left_menu_is_loaded()

    def login_mebbis(self, tc, password):
        """
        EBA'ya giriş yapma işlemini gerçekleştiren metot

        :param tc: kullanıcı mebbis girişi için TC numarası
        :param password: kullanıcı mebbis girişi için şifre
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

        # MEBBİS ile giriş tuşuna bas ve Mebbis girişi sayfasına git
        self.driver.find_element_by_xpath("//button[@title='MEBBİS ile giriş']").click()
        # TC ve şifre yaz
        self.driver.find_element_by_css_selector("#txtKullaniciAd").send_keys(settings.tc)
        self.driver.find_element_by_xpath("//input[@id='txtSifre']").send_keys(settings.password)

        # Eğer sayfa yüklenemez veya başka bir hata alınırsa
        # giriş işlemini tekrar et.
        try:
            guvenlik_kodu = input("Güvenlik Kodunu Giriniz: ")
            self.driver.find_element_by_xpath("//input[@id='txtGuvenlikKod']").send_keys(guvenlik_kodu)
            self.driver.find_element_by_css_selector("#btnGiris").click()
            self.driver.find_element_by_xpath("//input[@name='submitButton']").click()
            current_url = self.driver.current_url

            self.wait.until(ec.url_changes(current_url))

            # hata sayfası ise tekrar giriş yap
            if current_url == self.LOGIN_ERROR_URL:
                print('Hata sayfasına gitti. Tekrar giriş yapılacak.')
                self.login(tc, password)

            # canlı ders sayfası ise EBA'ya devam et
            elif 'liveMiddleware' in current_url:
                print("Canlı ders var. EBA'ya devam ediliyor.")
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
