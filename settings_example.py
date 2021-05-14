# Chrome driver tam yolu
# Örnek: C:\\Development\\drivers\\chromedriver.exe
driver_path = ""
# Firefox driver tam yolu
# Örnek: C:\\Development\\drivers\\geckodriver.exe
firefox_path = ""
# Internet Explorer tam yolu
# örnek: C:\\Development\\drivers\\IEDriverServer.exe
ie_path = ""

# 29 Nisan 2021 Eklemesi
# ----------------------
# E-devlet girişi için TC
tc = ""
# E-devlet girişi için şifre
password = ""

# 20 Mayıs 2021 Eklemesi
# ----------------------
# Birden fazla kullanıcı ile işlem yapmak için tanımlanmıştır
# Kullanıcı bilgileri çoğaltılarak birden fazla kullanıcı için işlemler yapılabilir.
users = [
    # 1. kullanıcı bilgileri
    # Not: Eğer birden fazla kullanıcı olacaksa;
    # süslü parantezler dahil çoğaltılır ve aralara virgül konur
    {
        # EBA girişi için kullanıcı TC
        "tc":"",
        # EBA girişi için kullanıcı şifre
        "password":"",
        # Zoom işlemleri için api key
        "zoom_api_key":"",
        # Zoom işlemleri için api secret
        "zoom_api_secret":"",
        # canlı derslerin olduğu excel dosyası yolu
        "live_lessons_xl":""
    }
]
