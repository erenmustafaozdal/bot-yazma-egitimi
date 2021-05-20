from selenium import webdriver
import os


class Browser:
    """
    Tarayıcı nesnesini oluşturan ve ilk ayarlarını yapan tarayıcı (browser) nesnesi
    """

    def __init__(self, driver_path, is_headless=False):
        """
        Yapılandırma metodu

        :param driver_path: çalıştırılabilir tarayıcı yolu
        """

        # chrome ayarları alınır ve yeni ayarlamalar yapılır
        # ayarlar hakkında bilgi alın: https://chromedriver.chromium.org/capabilities
        options = webdriver.ChromeOptions()
        # loglama iptal et
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # gizli mi çalışsın
        options.headless = is_headless
        # argümanların listesi: https://peter.sh/experiments/chromium-command-line-switches
        # tarayıcı profili belirlenir
        # Chrome varsayılan (Default) profilinizi "chrome://version" adresine giderek görebilirsiniz
        # "Profil Yolu" başlığı karşısındaki değer varsayılan profildir. Son klasör adı yerine yeni profil klasör adı yazılır
        options.add_argument(f"user-data-dir={os.getenv('USERPROFILE')}\\AppData\\Local\\Google\\Chrome\\User Data\\Bot Workshop")
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
