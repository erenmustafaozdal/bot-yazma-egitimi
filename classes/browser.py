from selenium import webdriver


class Browser:
    """
    Tarayıcı nesnesini oluşturan ve ilk ayarlarını yapan tarayıcı (browser) nesnesi
    """

    def __init__(self, driver_path):
        """
        Yapılandırma metodu

        :param driver_path: çalıştırılabilir tarayıcı yolu
        """

        self.driver = webdriver.Chrome(driver_path)
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
        self.driver.quit()
