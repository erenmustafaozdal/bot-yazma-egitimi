# BOT YAZMA EĞİTİMİ ATÖLYESİ

İstanbul Öğretmen Akademileri "Python ile Eğitim Ortamlarında Verimliliği Artırma / BOT Yazma Eğitimi - EBA Örnekleri" atölyesi kod örneklerinin bulunduğu depo

> **❗❗❗ DİKKAT:** **Bot Yazma Eğitimi atölyemiz bitmiştir.** Sonradan yapılan çalışmaların değişmesine engel olmak amacıyla depo arşive alınmıştır. Çalışmalarınıza devam etmek için <u>_Fork_</u> işlemi ile çatallayıp, kendi hesabınız üzerinde devam edebilirsiniz.

---

## İÇİNDEKİLER

- [Web Otomasyon Nedir?](#web-otomasyon-nedir)
- [NASIL BAŞLANIR?](#nasil-başlanir)
    - [Python Kurun](#python-kurun)
    - [Selenium Kurun](#selenium-kurun)
    - [PyCharm Kurun](#pycharm-kurun)
    - [GitHub'a Başlangıç Yapın](#githuba-başlangıç-yapın)
        - [Geliştirme Esnasında Kullanacağınız Tarayıcının Sürücüsünü İndirin](#geliştirme-esnasında-kullanacağınız-tarayıcının-sürücüsünü-i̇ndirin)
    - [Excel işlemleri için openpyxl paketini yükleyin](#excel-işlemleri-için-openpyxl-paketini-yükleyin)
    - [Zoom API ile canlı dersleri oluşturma](#zoom-api-ile-canl%C4%B1-dersleri-olu%C5%9Fturma)
        - [Zoom’da JWT uygulaması oluşturun](#zoomda-jwt-uygulamas%C4%B1-olu%C5%9Fturun)
        - [Zoom Api uygulaması bilgileri](#zoom-api-uygulaması-bilgileri)
        - [JWT Token üretmek için pyjwt paketinin yüklenmesi](#jwt-token-%C3%BCretmek-i%C3%A7in-pyjwt-paketinin-y%C3%BCklenmesi)
        - [Canlı ders oluşturma](#canl%C4%B1-ders-olu%C5%9Fturma)
    - [Telethon kütüphanesiyle Telegram BOT Api kullanılarak mesaj gönderme](#telethon-kütüphanesiyle-telegram-bot-api-kullanılarak-mesaj-gönderme)
        - [Telegram BOT Api uygulaması oluşturma](#telegram-bot-api-uygulaması-oluşturma)
- [Bazı Gerekli Adresler](#bazı-gerekli-adresler)
- [Proje İçinde Nasıl Geliştirme Yaparsınız](#proje-i̇çinde-nasıl-geliştirme-yaparsınız)
    - [Geliştirme yaparken aşağıdaki adımları takip etmek çok önemlidir.](#geli%C5%9Ftirme-yaparken-a%C5%9Fa%C4%9F%C4%B1daki-ad%C4%B1mlar%C4%B1-takip-etmek-%C3%A7ok-%C3%B6nemlidir)
- [Atölye Ders Videoları](#atölye-ders-videoları)
- [Örnek Çalışmalar](#örnek-çalışmalar)

---


## Web Otomasyon Nedir?


> İnternet üzerindeki iş ve işlemlerin yazılım aracılığıyla otomatik 
> yapılmasıdır. Size izin verilen işlemleri daha hızlı, daha kolay ve 
> daha hatasız yapmanızı sağlar. **Web sitelerini "hack’lemek" *(kırmak)*** 
> **değildir.** Sistemin size izin vermediği işlemleri yapamazsınız.

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---


## NASIL BAŞLANIR?

1. Python programlama dilini bilgisayarınıza indirin ve kurun. [🔗](#python-kurun)
2. Python Selenium paketini bilgisayarınıza yükleyin. [🔗](#selenium-kurun)
3. Kodlama yapacağınız geliştirme ortamınızı kurun/hazırlayın. Eğitimde PyCharm kullanılmıştır. [🔗](#pycharm-kurun)
4. Eğer yoksa GitHub hesabı oluşturun. GitHub Desktop uygulamasını indirin ve kurun. [🔗](#githuba-başlangıç-yapın)

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

### Python Kurun
[https://www.python.org/downloads](https://www.python.org/downloads) adresine giderek Python `3.x` *(3.4 ve üzeri bir sürüm olabilir.)* versiyonunu indirin ve kurun.

> Nasıl yapılacağını videonun ilgili bölümünü izleyerek görebilirsiniz <br> 👉 [https://youtu.be/aUqnZrpmPHU?t=2085](https://youtu.be/aUqnZrpmPHU?t=2085)

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---


### Selenium Kurun
Bilgisayarınızda komut istemini *(CMD)* açın ve aşağıdaki kod ile Selenium'u kurun.

```pip install U selenium```

> Nasıl yapılacağını videonun ilgili bölümünü izleyerek görebilirsiniz <br> 👉 [https://youtu.be/aUqnZrpmPHU?t=2802](https://youtu.be/aUqnZrpmPHU?t=2802)

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

### PyCharm Kurun
[https://www.jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download) adresinden PyCharm geliştirme ortamının ücretsiz versiyonunu indirip, kurun. Bu isteğe bağlı bir seçenektir. Başka geliştirme ortamı da *(IDE)* kullanabilirsiniz.

> Nasıl yapılacağını videonun ilgili bölümünü izleyerek görebilirsiniz <br> 👉 [https://youtu.be/aUqnZrpmPHU?t=3203](https://youtu.be/aUqnZrpmPHU?t=3203)

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

### GitHub'a Başlangıç Yapın
İlk başta eğer yoksa GitHub hesabınızı oluşturun.

> Nasıl yapılacağını videonun ilgili bölümünü izleyerek görebilirsiniz <br> 👉 [https://youtu.be/aUqnZrpmPHU?t=3966](https://youtu.be/aUqnZrpmPHU?t=3966)

Ardından [https://desktop.github.com](https://desktop.github.com) adresine giderek GitHub Desktop uygulamasını indirin ve kurun.

> Nasıl yapılacağını videonun ilgili bölümünü izleyerek görebilirsiniz <br> 👉 [https://youtu.be/aUqnZrpmPHU?t=4387](https://youtu.be/aUqnZrpmPHU?t=4387)

Bu yazıyı okuduğunuza göre **"Bot Yazma Eğitimi"** kod havuzumuza erişme davetini kabul etmiş oluyorsunuz.

Şimdi bilgisayarınızda istediğiniz konuma projeyi klonlayın.

> Nasıl yapılacağını videonun ilgili bölümünü izleyerek görebilirsiniz <br> 👉 [https://youtu.be/aUqnZrpmPHU?t=4642](https://youtu.be/aUqnZrpmPHU?t=4642)

Artık klonladığınız projeyi geliştirme ortamınızda *(PyCharm veya başkası)* proje olarak tanımlayın.

> Nasıl yapılacağını videonun ilgili bölümünü izleyerek görebilirsiniz <br> 👉 [https://youtu.be/aUqnZrpmPHU?t=4872](https://youtu.be/aUqnZrpmPHU?t=4872)

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

#### Geliştirme Esnasında Kullanacağınız Tarayıcının Sürücüsünü İndirin
Chrome, Opera, Mozilla Firefox, Edge, Internet Explorer veya Safari... Seçiminize göre kullanacağınız tarayıcı sürücüsünü *(driver)* indirin.

[https://www.selenium.dev/downloads](https://www.selenium.dev/downloads) adresine giderek istediğiniz sürücüyü indirebilirsiniz.

> Nasıl yapılacağını videonun ilgili bölümünü izleyerek görebilirsiniz <br> 👉 [https://youtu.be/BX8_AuvE-fs?t=1010](https://youtu.be/BX8_AuvE-fs?t=1010)

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

### Excel işlemleri için openpyxl paketini yükleyin
Bilgisayarınızda komut istemini *(CMD)* açın ve aşağıdaki kod ile **openpyxl** paketini yükleyin.

```pip install openpyxl```

Bu paket ile Excel dosyasına yazma ve Excel dosyasından okuma işlemleri yapılabilmektedir. Detaylı bilgi için [Bazı Gerekli Adresler](#baz%C4%B1-gerekli-adresler) başlığı altında bulunan openpyxl dokümantasyonu adresini ziyaret edebilirsiniz.

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

### Zoom API ile canlı dersleri oluşturma
[Zoom Api](https://marketplace.zoom.us/docs/api-reference/introduction) kullanılarak Zoom içinde canlı dersleri oluşturabiliriz. Ardından bu dersleri EBA'da tanımlayabiliriz.

> Burada kullanılacak tüm adresler **[Bazı Gerekli Adresler](#baz%C4%B1-gerekli-adresler)** başlığı altında da listelenmiştir. Zoom API hakkında daha fazla bilgi almak için Zoom API dokümantasyonunu inceleyebilirsiniz.

Zoom Api'sini kullanırken bazı kullanım limitleri vardır. Bu limitler hakkında bilgi almak için [Zoom Api rate limits](https://marketplace.zoom.us/docs/api-reference/rate-limits) sayfasını inceleyebilirsiniz.

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

#### Zoom'da JWT uygulaması oluşturun
[Zoom uygulaması oluşturma sayfası](https://marketplace.zoom.us/develop/create?source=devdocs)na gidin. Burada **JWT** seçeneği altındaki `Create` tuşuna basın. Gelen ekranda **Basic Information** ve **Developer Contact Information** başlıkları altında bulunan aşağıdaki zorunlu alanları doldurun.

- [x] **App Name:** Uygulamanıza istediğiniz bir isim verin.
- [x] **Company Name:** Şirket adı belirleyin. ***EBA**, **MEB** veya istediğiniz başka bir isim verebilirsiniz.*
- [x] **Name:** Geliştirici adı olarak kendi adınızı yazabilirsiniz.
- [x] **Email Address:** Geliştirici e-posta adresi olarak yine kendi e-posta adresinizi yazabilirsiniz.

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

#### Zoom Api uygulaması bilgileri
Zoom JWT uygulamanızın `API Key`, `API Secret` ve bu iki bilgiden oluşan `JWT TOKEN` bilgilerini almamız gerekiyor. Bunun için JWT uygulamanızın **App Credentials** menüsüne tıklayarak ilgili sayfaya gidin. Burada bulunan `API Key` ve `API Secret` bilgilerini bir yere not edin.

> **❗ DİKKAT:** `API Key` ve `API Secret` bilgileri çok önemli bilgilerdir. **Uygulama güvenliği için bu bilgileri hiç kimse ile paylaşmayın.** Atölyemiz içinde yapacağımız çalışmalarda bu bilgileri `settings.py` dosyasında tutarak, GitHub ile eşitlenmesini engelleyeceğiz.

Bu sayfada bulunan `JWT Token` bilgisini, Zoom Api dokümantasyonu içinde test amaçlı kullanacağız. **Uygulama güvenliği için bu JWT Token bilgisini geliştirdiğimiz kod içine almayacağız**. Kodlamamızda JWT Token'ı otomatik oluşturacağız.

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

#### JWT Token üretmek için pyjwt paketinin yüklenmesi
Aşağıdaki kod ile [pyjwt](https://github.com/jpadilla/pyjwt) paketini yükleyin.

```
pip install PyJWT
```

Paketin GitHub sayfasındaki örneği ele alarak Zoom Api için aşağıdaki şekilde JWT Token oluşturacağız.

```python
import jwt

jwt_token = jwt.encode({"iss": zoom_api_key, "exp": expire_time}, zoom_api_secret, algorithm="HS256")
```

Bu kodda bulunan `expire_time` değerini Python ile üreteceğiz.

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

#### Canlı ders oluşturma
Canlı ders oluşturmak için Zoom Api dokümantasyonu içindeki [Meeting Create](https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingcreate) bölümünü kullanacağız. İstek *(request)* parametresi olarak sadece `userId` verilecek. Kendi adımıza ders oluşturacağımız için bu değer `me` şeklinde olabilir. İsteğin gövdesinde *(request body)* ise ders hakkında ayar parametreleri gönderilecek.

> Sayfanın en altında bulunan **Send a Test Request** bölümünde test edebilirsiniz.

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

### Telethon kütüphanesiyle Telegram BOT Api kullanılarak mesaj gönderme

Aşağıdaki kod ile [Telethon](https://github.com/LonamiWebs/Telethon) kütüphanesini yükleyin.

```
pip install telethon
```

Doğru yüklendiğini kontrol etmek için aşağıdaki kodu çalıştırabilirsiniz.

``` shell
python -c "import telethon; print(telethon.__version__)"
```

Eğer kütüphanenin doğru versiyon numarası göründüyse her şey yolundadır.

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

#### Telegram BOT Api uygulaması oluşturma

Telegram'ın BOT Api'siyle çalışmadan önce, kendi Api `id` ve `hash` bilgilerinizi almanız gerekir:

1. Kullanacağınız geliştirici hesabının telefon numarasıyla [Telegram hesabınıza giriş yapın](https://my.telegram.org/).
2. **"API development tools"** bağlantısına tıklayın.
3. Bir yeni uygulama oluştur penceresi görünecektir. Başvuru bilgilerinizi doldurun. Herhangi bir _URL_ girmeye gerek yoktur ve yalnızca iki alan **(App title ve Short name)** daha sonra değiştirilebilir.
4. Sonunda _Create application_'a tıklayın. Api `id` ve `hash` bilgileriniz çok gizlidir. Telegram bu bilgileri değiştirmenize veya iptal etmenize izin vermez. Bu bilgileri kimse ile paylaşmayın!

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

## Bazı Gerekli Adresler

- [Selenium resmi web sitesi](https://www.selenium.dev)
- [Selenium komutları ve diğer dokümantasyonlar](https://www.selenium.dev/documentation/en)
- [Atölyemizin Google Drive klasörü](https://drive.google.com/drive/folders/1P6b4wvA9Guqq7ODGiU7MHOsOSjc_oHne?usp=sharing)
- [openpyxl - Python Excel kütüphanesi dokümantasyonu](https://openpyxl.readthedocs.io)
- [Zoom Api dokümanı](https://marketplace.zoom.us/docs/api-reference/introduction)
    - [Zoom Api uygulama oluşturma](https://marketplace.zoom.us/develop/create?source=devdocs)
    - [Zoom Api kullanım sınırları (rate limits)](https://marketplace.zoom.us/docs/api-reference/rate-limits)
    - [Zoom Api ile ders oluşturma dokümanı (meeting create)](https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingcreate)
- [Telethon Telegram kütüphanesi](https://docs.telethon.dev/en/latest/)
    - [Telegram Api uygulaması oluşturmak için hesabınız](https://my.telegram.org/)

Web elemanlarını bulmak için özellikle CSS ve XPATH seçicilerini belirlemede bize yardımcı olacak bazı eklentiler var. Bunlar için aşağıdaki adresleri ziyaret edebilirsiniz.
- [ChroPath Chrome eklentisi](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo)
- [SelectorsHub Chrome eklentisi](https://chrome.google.com/webstore/detail/selectorshub/ndgimibanhlabgdgjcpbbndiehljcpfh)
- [SelectorsHub resmi web sitesi](https://selectorshub.com/)

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

## Proje İçinde Nasıl Geliştirme Yaparsınız

Her öğretmen için [teachers](https://github.com/erenmustafaozdal/bot-yazma-egitimi/tree/main/teachers) klasörü içinde kendine özel bir klasör oluşturulmuştur. Bu klasörler her öğretmenin GitHub kullanıcı adı ile isimlendirilmiştir.

Ayrıca her öğretmenin GitHub kullanıcı adı ile ana dal'dan ***(main)*** ayrı bir geliştirme dalı vardır. Bu dal ana dalın bir kopyasını barındırmaktadır.

> **❗ NOT:** Kendi bilgisayarınıza özel bilgiler (tarayıcı sürücülerinin yolları ve ön bellek dosyaları gibi) 
> ve kişisel bilgiler (tc, şifre gibi) `settings.py` dosyasında saklanması çok önemlidir. 
> Ana proje klasörü dahil, her öğretmen klasöründe `settings.py` dosyaları 
> `.gitignore` ile gizlenmiştir. Yani hiçbir bilgisayar ile eşitleme yapılmaz ve GitHub'a gönderilmez.

> **❗❗❗ DİKKAT:** Her öğretmen kendi klasöründe ve kendi dalında geliştirme yapmalıdır. 
> Ana dal sadece eğitim veren Eren Mustafa Özdal tarafından kontrol edilecektir. 
> Diğer dallardan gelen çekme istekleri ***(pull request)*** kontrol edildikten sonra 
> değişiklikler ana dala ***(main)*** yansıtılacaktır.

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

#### Geliştirme yaparken aşağıdaki adımları takip etmek çok önemlidir.

1. Kodlamaya başlamadan önce ana **`(main)`** dala geç. Yapılan değişiklik var mı? Karşılaştır **`(fetch)`**.
2. Eğer varsa değişiklikleri kendi bilgisayarındaki ana dala **`(main)`** çek. **`(pull)`**
3. Kendi dalına geç
4. Ana dalda **`(main)`** yapılan değişiklikleri kendi dalına birleştir. **`(merge)`**
5. Kendi dalında kodlamanı yap. Kodlama basamaklarını işle. **`(commit)`**
6. Biten geliştirmeni Github’a it. **`(push)`**
7. Gönderdiğin değişikliğin ana dala birleşmesi için çekme isteği oluştur **`(pull request)`**. **Çekme isteği gönderdikten sonra birleştirme işlemini `(merge)` siz yapmayın. Kontrol edildikten sonra yapılacaktır.**
8. Bütün bu işlemleri, her kodlama öncesi tekrarla.

✅ 8 adımlık iş akışını aşağıdaki görselden de inceleyebilirsiniz.

![GitHub Geliştirme İş Akışı](https://drive.google.com/uc?export=view&id=1ag6s2hycf-DAjHuc6jyZAPoXy3_SNcoB)


> Bu adımların nasıl atılacağını videonun ilgili bölümünü izleyerek görebilirsiniz <br> 👉 [https://youtu.be/ZAChGQz3wfY?t=5618](https://youtu.be/ZAChGQz3wfY?t=5618)

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

## Atölye Ders Videoları

| AÇIKLAMA | VİDEO BAĞLANTISI |
|:-|:-:|
| **1. HAFTA**<br> <ul><li>Web otomasyon nedir?</li><li>Geliştirme ortamının hazırlanması</li></ul> |  [![Web Otomasyon Nedir? - Python ile Bot Yazma Eğitimi Hafta #1](https://img.youtube.com/vi/aUqnZrpmPHU/maxresdefault.jpg)](https://youtu.be/aUqnZrpmPHU) |
| **2. HAFTA**<br><ul><li>Git teknolojisinin önemi ve kullanımı *(senaryo üzerinden)*</li><li>Farklı tarayıcı sürücülerinin indirilmesi ve kullanımı</li><li>Basit Selenium komutları</li></ul> | [![Git'in Önemi ve Kullanımı, Basit Selenium Komutları - Python ile Bot Yazma Eğitimi Hafta #2](https://img.youtube.com/vi/BX8_AuvE-fs/maxresdefault.jpg)](https://youtu.be/BX8_AuvE-fs) |
| **3. HAFTA**<br> <ul><li>HMTL elemanları nedir?</li><li>HTML elemanları Selenium ile nasıl seçilir ve kullanılır?</li><li>HTML elemanlarını daha kolay seçmek için tarayıcı eklentileri</li><li>BOT yazma atölyesinde GitHub projemizde geliştirme iş akışımız *(çalışma düzenimiz)*</li></ul> | [![Git'in Önemi ve Kullanımı, Basit Selenium Komutları - Python ile Bot Yazma Eğitimi Hafta #3](https://img.youtube.com/vi/ZAChGQz3wfY/maxresdefault.jpg)](https://youtu.be/ZAChGQz3wfY) |
| **4. HAFTA**<br> <ul><li>Git iş akışımız üzerine sohbet</li><li>EBA öğrenci bazlı çalışma raporlarını kontrol etme projemizin ilk adımı <ol><li>EBA'ya giriş</li><li>"Raporlar" menüsüne tıklama</li></ol></li></ul> | [![Öğrenci Bazlı Raporları Kontrol Etme Projesi - Python ile Bot Yazma Eğitimi Hafta #4](https://img.youtube.com/vi/_KtvP_fBBH8/maxresdefault.jpg)](https://youtu.be/_KtvP_fBBH8) |
| **4. HAFTA EK - 1**<br> <ul><li>4. hafta dersi esnasından alınan hataların düzeltilmesi</li></ul> | [![4. Haftada Alınan Hataların Düzeltilmesi - Python ile Bot Yazma Eğitimi Hafta #4 - Ek 1](https://img.youtube.com/vi/yRAqBt9K3yA/maxresdefault.jpg)](https://youtu.be/yRAqBt9K3yA) |
| **5. HAFTA** <br> <ul><li>EBA öğrenci bazlı çalışma raporlarını kontrol etme projemizin devamı <ol><li>"Çalışma Raporları" sayfasına gitme</li><li>"Öğrenci Bazlı" sayfasına gitme</li><li>Her öğrencinin tamamlama ve performans ortalamalarının alınıp ekrana yazdırılması</li><li>Öğrenci bazlı raporların ekran görüntüsünün kaydedilmesi</li></ol></li></ul> | [![Öğrenci Bazlı Raporları Kontrol Etme Projesi Devamı - Python ile Bot Yazma Eğitimi Hafta #5](https://img.youtube.com/vi/OpCIDBkmfc4/maxresdefault.jpg)](https://youtu.be/OpCIDBkmfc4) |
| **5. HAFTA EK - 1** <br> <ul><li>Öğrenci çalışma bilgilerini Excel dosyasına kaydetme</li></ul> | [![Öğrenci Çalışma Bilgilerini Excel Dosyasına Kaydetme - Python ile Bot Yazma Eğitimi Hafta #5 - Ek 1](https://img.youtube.com/vi/rBJKP4wXPYY/maxresdefault.jpg)](https://youtu.be/rBJKP4wXPYY) |
| **5. HAFTA EK - 2** <br> <ul><li>**Projelerimizi Çalıştırmak İçin Kısayol Oluşturma** *(Her proje için kullanılabilir)*</li></ul> | [![Projelerimizi Çalıştırmak İçin Kısayol Oluşturma - Python ile Bot Yazma Eğitimi Hafta #5 - Ek 2](https://img.youtube.com/vi/Wfc65XFRqJM/maxresdefault.jpg)](https://youtu.be/Wfc65XFRqJM) |
| **5. HAFTA EK - 3** <br> <ul><li>**Projelerimizi Otomatik Çalıştırmak İçin Zamanlama** *(Her proje için kullanılabilir)*</li></ul> | [![Projelerimizi Otomatik Çalıştırmak İçin Zamanlama - Python ile Bot Yazma Eğitimi Hafta #5 - Ek 3](https://img.youtube.com/vi/txkqv5D_LHQ/maxresdefault.jpg)](https://youtu.be/txkqv5D_LHQ) |
| **6. HAFTA** <br> <ul><li>Canlı dersleri otomatik tanımlama projesi başlangıcı<ol><li>Zoom Api tanıtımı</li><li>Telegram Api tanıtımı</li><li>EBA, Tarayıcı, Excel dosyası, Zoom Api ve Telegram Api işlemlerini yönetecek sınıfların tanıtımı </li></ol></li></ul> | [![Zoom Api ve Telegram Api Tanıtımı - Python ile Bot Yazma Eğitimi Hafta #6](https://img.youtube.com/vi/E0MprCpuXUc/maxresdefault.jpg)](https://youtu.be/E0MprCpuXUc) |
| **7. HAFTA** <br> <ul><li>Zoom ve Telegram API kullanılarak canlı dersleri kaydetme ve mesajını zamanlama işleminin yapılması. Ayrıca bu derslerin EBA'da tanımlanmasının da otomatikleştirilmesi.</li></ul> | [![Canlı Dersleri Kaydetme ve Mesajlarını Zamanlama - Python ile Bot Yazma Eğitimi Hafta #7](https://img.youtube.com/vi/_3DMAN6vPuQ/maxresdefault.jpg)](https://youtu.be/_3DMAN6vPuQ) |
| **7. HAFTA EK - 1** <br> <ul><li>Zoom ve Telegram API kullanılarak canlı dersleri kaydetme, EBA'da tanımlama ve mesajlarının zamanlaması işlemlerinin devamı.</li></ul> | [![Canlı Dersleri Kaydetme ve Mesajlarını Zamanlama - Python ile Bot Yazma Eğitimi Hafta #7 - Ek 1](https://img.youtube.com/vi/LuS_a2MvYqA/maxresdefault.jpg)](https://youtu.be/LuS_a2MvYqA) |
| **8. HAFTA** <br> <ul><li>Bot yazma eğitimi atölyesinin 8. haftasında otomatik yaprak test ve sınav oluşturma işlemleri anlatılmış ve canlı yayında kodlaması yapılmıştır.</li></ul> | [![Yaprak Test ve Sınav Oluşturma - Python ile Bot Yazma Eğitimi Hafta #8](https://img.youtube.com/vi/yUkG99yOEJA/maxresdefault.jpg)](https://youtu.be/yUkG99yOEJA) |
| **9. HAFTA** <br> <ul><li>Bot yazma eğitimi atölyesinin son haftası olan 9. haftasında öğrencilerin e-okul bilgilerini otomatik güncelleme işlemleri anlatılmış ve canlı yayında kodlaması yapılmıştır.</li></ul> | [![E-Okul Öğrenci Bilgilerini Güncelleme - Python ile Bot Yazma Eğitimi Hafta #9](https://img.youtube.com/vi/Sw3xnXhIeMM/maxresdefault.jpg)](https://youtu.be/Sw3xnXhIeMM) |

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

## Örnek Çalışmalar

| AÇIKLAMA | VİDEO BAĞLANTISI |
|:-|:-:|
| **Eleman Seçme Dersinin Etkileşimli Tekrarı** <br> 3. haftada öğrendiğimiz eleman seçme konusunun [@mehmetakifturanbt](https://github.com/mehmetakifturanbt) tarafından geliştirilen etkileşimli tekrarı  | [![Eleman Seçme Dersinin Etkileşimli Tekrarı - Python ile Bot Yazma Eğitimi Uygulaması](https://img.youtube.com/vi/6M25RwGawe0/maxresdefault.jpg)](https://youtu.be/6M25RwGawe0) |
| **Öğrenci Belgesi Yazdırma** <br> [@fgunes7](https://github.com/fgunes7) tarafından geliştirilen projede öğrenci numarası verilen öğrencinin belgesi otomatik yazdırılıyor | [![Öğrenci Belgesi Yazdırma - Python ile Bot Yazma Eğitimi Uygulaması](https://img.youtube.com/vi/Ye8lJq9hTdE/maxresdefault.jpg)](https://youtu.be/Ye8lJq9hTdE) |
| **2. ve 3. Hafta Ders Çalışmaları Ayrı Dosyalarda** <br> [@kbala42](https://github.com/kbala42) tarafından 2. ve 3. hafta çalışmalarımız ayrı dosyalarda anlamlı parçalara ayrılmış | [![2. ve 3. Hafta Ders Çalışmaları Ayrı Dosyalarda - Python ile Bot Yazma Eğitimi Uygulaması](https://img.youtube.com/vi/vtBRXQOoEy0/maxresdefault.jpg)](https://youtu.be/vtBRXQOoEy0) |
| **4. Hafta Çalışması Örneği ve Paylaşım Yapma&Silme** <br> [@Aytac-Kula](https://github.com/Aytac-Kula) tarafından geliştirilen projede 4. haftada yapılan işlemler yapılmış ve gitmek istenen sayfaya gidilmesi işlemi tamamlanmıştır. Ek olarak paylaşım yapma ve silme örnekleri gösterilmiştir. | [![4. Hafta Çalışması Örneği ve Paylaşım Yapma&Silme - Python ile Bot Yazma Eğitimi Uygulaması](https://img.youtube.com/vi/PSco4Fz0wnw/maxresdefault.jpg)](https://youtu.be/PSco4Fz0wnw) |
| **IMDB Top 250** <br> [@oguzkapan](https://github.com/oguzkapan) tarafından geliştirilen projede IMDB'de en iyi 250 film bilgileri TXT dosyasına kaydediliyor. | [![IMDB Top 250 Film Bilgilerini Alma - Python ile Bot Yazma Eğitimi Uygulaması](https://img.youtube.com/vi/RasKfYTMW1Y/maxresdefault.jpg)](https://youtu.be/RasKfYTMW1Y) |
| **EBA Tek Kullanımlık Şifre Alma** <br> [@mfatiharslan](https://github.com/mfatiharslan) tarafından geliştirilen öğrenci numarası verildikten sonra, otomatik TC bilgisini alıp, EBA tek kullanımlık şifre oluşturup TXT dosyasına yazan çalışma  | [![EBA Tek Kullanımlık Şifre Alma - Python ile Bot Yazma Eğitimi Uygulaması](https://img.youtube.com/vi/VCfyaVp5jjc/maxresdefault.jpg)](https://youtu.be/VCfyaVp5jjc) |
| **Linkedin Bağlantı Bilgilerini Toplama** <br> [@mehmetakifturanbt](https://github.com/mehmetakifturanbt) tarafından geliştirilen projede kullanıcının Linkedin bağlantı bilgileri Excel dosyasına, metin (txt) dosyasına yazdırılmış ve ekran görüntüleri kaydedilmiştir  | [![Linkedin Bağlantı Bilgilerini Toplama - Python ile Bot Yazma Eğitimi Uygulaması](https://img.youtube.com/vi/_EgF7AqLx8Q/maxresdefault.jpg)](https://youtu.be/_EgF7AqLx8Q) |
| **Öğrenci Bazlı Çalışmaları Kontrol Etme** <br> [@Aytac-Kula](https://github.com/Aytac-Kula) tarafından geliştirilen projede öğrenci bazlı çalışmalar otomatik olarak kontrol edilmiştir. Ayrıca kontrol edilen öğrenci bilgileri Excel dosyasına yazdırılmış ve ekran görüntüleri kaydedilmiştir  | [![Öğrenci Bazlı Çalışmaları Kontrol Etme - Python ile Bot Yazma Eğitimi Uygulaması](https://img.youtube.com/vi/u94AujH41bY/maxresdefault.jpg)](https://youtu.be/u94AujH41bY) |
| **Excel Dosyasındaki Öğrencilerin Şifrelerini Oluşturma** <br> [@oguzkapan](https://github.com/oguzkapan) tarafından geliştirilen projede Excel dosyasındaki öğrenci bilgileri ile EBA'da her öğrenci için tek kullanımlık şifre oluşturulup Excel dosyasına kaydediliyor. | [![Excel Dosyasındaki Öğrencilerin Şifrelerini Oluşturma - Python ile Bot Yazma Eğitimi Uygulaması](https://img.youtube.com/vi/L-RE1dXOj0o/maxresdefault.jpg)](https://youtu.be/L-RE1dXOj0o) |
| **Not Listesi Alma** <br> [@ecevahir](https://github.com/ecevahir) tarafından geliştirilen projede E-okul'daki öğrenci not bilgileri alınıp Excel dosyasına kaydediliyor. | [![Not Listesi Alma - Python ile Bot Yazma Eğitimi Uygulaması](https://img.youtube.com/vi/OhxbOrsDHe0/maxresdefault.jpg)](https://youtu.be/OhxbOrsDHe0) |

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*
