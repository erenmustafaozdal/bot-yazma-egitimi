from selenium import webdriver
import os

"""

Tarayıcı nesnesini oluşturan ve ilk ayarlarını yapan tarayıcı (browser) sınıfı

"""

class Browser:


    def __init__(self, driver_path, is_headless=False):
        """
        Browser sınıfımızın yapılandırma metodunu oluşturuyoruz

        :param driver_path: çalıştırılabilir tarayıcı yolu
        :param is_headless: gizli çaışma. Eğer tarayıcımızın gizli çalışmasını istiyorsak true parametresi girmeliyiz.
                             Tarayıcının açıktan çalışması istediğimiz durumda parametre girmemeize gerek yok
        """
        # ChromeOptions sınıfı tarayıcımızın ayarlamalarını alabileceğimiz ve üzerinde yeni ayarlamalar yapabileceğimiz sınıftır
        # https://chromedriver.chromium.org/capabilities ayrıntılara ulaşılabilir.
        # Selenium'un webdriver nesnesinin ChromeOptions() metodu üzerinden options adlı nesne üretiyoruz
        # Selenium api şu adresten incelenebilir: https://selenium-python.readthedocs.io/api.html
        options = webdriver.ChromeOptions()

        # loglama iptal et
        # https://joshuatz.com/posts/2020/selenium-webdriver-disabling-chrome-logging-messages/
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # gizli mi çalışsın
        # https://stackoverflow.com/questions/46920243/how-to-configure-chromedriver-to-initiate-chrome-browser-in-headless-mode-throug
        options.headless = is_headless

        # argümanların listesi: https://peter.sh/experiments/chromium-command-line-switches
        # tarayıcı profili belirlenir
        # Chrome varsayılan (Default) profilinizi "chrome://version" adresine giderek görebilirsiniz. Chrome adres satırına yazıldığında görülebilir
        # "Profil Yolu" başlığı karşısındaki değer varsayılan profildir. Son klasör adı yerine yeni profil klasör adı yazılır
        options.add_argument(f"user-data-dir={os.getenv('USERPROFILE')}\\AppData\\Local\\Google\\Chrome\\User Data\\Bot Workshop")
        # Taracnın maksimum boyutta çalışmasını istiyoroz
        options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(driver_path, options=options)
        self.driver.maximize_window()

        # sayfanın yüklemesini çok beklememesi için
        # 20 saniye beklemesini, yoksa hata vermesini belirliyoruz
        # hata verdiğinde bu hatayı yakalayıp
        # sayfanın yenilenmesini veya giriş işlemini tekrar etmesini sağlayacağız
        self.driver.set_page_load_timeout(20)

    def get(self):
        """
        :return: webdriver tarayıcı nesnesini geri döndürür
        """

        return self.driver

    def __del__(self):
        self.driver.close()