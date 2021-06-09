from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class EOKUL:
    """
    Her projede çalışan temel E-okul işlemlerini yürütecek olan nesne
    """

    # Mebbis sayfası
    MEBBIS_URL = 'https://mebbis.meb.gov.tr'
    # Mebbis profil bilgisi DIV
    MEBBIS_PROFILE_ID = "ProfileInfoDiv"
    # Mebbis E-okul card
    EOKUL_CARD = "//img[contains(@src,'okul')]"
    # Mebbis E-okul link
    EOKUL_LINK_ID = "rptProjeler_ctl01_rptKullanicilar_ctl00_LinkButton1"
    # E-okul sol menü
    EOKUL_LEFT_MENU_ID = "modulMenuNew_menu"

    def __init__(self, driver):
        """
        __init__ ile nesne oluşturulduğunda ilk tanımlama ve ayarlamalar yapılır

        :param driver: selenium webdriver tarayıcı nesnesi
        """

        # tarayıcı nesnesi
        self.driver = driver
        # bekleme nesnesi
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    def login(self, tc, password):
        """
        Eokul'a giriş yapma işlemini gerçekleştiren metot

        :param tc: kullanıcı e-devlet girişi için TC numarası
        :param password: kullanıcı e-devlet girişi için şifre
        """

        # Mebbis'e git
        self.driver.get(self.MEBBIS_URL)

        # E-Devlet girişi tuşuna bas ve E-Devlet girişi sayfasına git
        self.driver.find_element_by_xpath("//a[contains(text(),'e-Devlet Girişi')]").click()

        # TC ve şifre yaz
        self.driver.find_element_by_css_selector("#tridField").send_keys(tc)
        self.driver.find_element_by_id("egpField").send_keys(password)

        # E-Devlet giriş formunu gönder.
        # Eğer sayfa yüklenemez veya başka bir hata alınırsa
        # giriş işlemini tekrar et.
        try:
            current_url = self.driver.current_url
            self.driver.find_element_by_xpath("//input[@name='submitButton']").click()

            self.wait.until(ec.url_changes(current_url))

        except:
            print("Sayfa yüklenemedi. Sayfa yenileniyor...")
            self.login(tc, password)
        else:
            # Mebbis yüklendi mi kontrol ediyoruz
            self.mebbis_is_loaded()

        self.go_to_eokul()

    def go_to_eokul(self):
        """
        Mebbiş'ten E-okul'a geçiş işlemini yapan metot
        """

        # başlangıçtaki sekmeler alınır. Daha sonra yeni eklenen tespit edilecek
        initial_windows = self.driver.window_handles

        # E-okul kartını çevir
        eokul_card = self.wait.until(ec.visibility_of_element_located(
            (By.XPATH, self.EOKUL_CARD)
        ))
        ActionChains(self.driver).move_to_element(eokul_card).perform()

        # E-okul bağlantısına tıkla
        self.wait.until(ec.visibility_of_element_located(
            (By.ID, self.EOKUL_LINK_ID)
        )).click()

        # yeni sekme açılana kadar bekle
        # self.wait.until(ec.number_of_windows_to_be(2))
        self.wait.until(ec.new_window_is_opened(initial_windows))

        # E-okul yeni sekmede açıldı. Mevcut sekmeyi kapat
        self.driver.close()

        # E-okul sekmesine geç
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # Sol menü tıklanılabilir olana kadar bekle
        self.wait.until(ec.element_to_be_clickable(
            (By.ID, self.EOKUL_LEFT_MENU_ID)
        ))


    def mebbis_is_loaded(self):
        """
        Mebbis profili bilgileri bölümü göründü mü?
        """
        try:
            self.wait.until(ec.visibility_of_element_located((By.ID, self.MEBBIS_PROFILE_ID)))
        except:
            print("Mebbis yüklenemedi. Sayfa yenileniyor.")
            self.driver.refresh()
            self.mebbis_is_loaded()
