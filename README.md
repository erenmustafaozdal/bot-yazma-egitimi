# BOT YAZMA EĞİTİMİ ATÖLYESİ

İstanbul Öğretmen Akademileri "Python ile Eğitim Ortamlarında Verimliliği Artırma / BOT Yazma Eğitimi - EBA Örnekleri" atölyesi kod örneklerinin bulunduğu depo

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


## Bazı Gerekli Adresler

- [Selenium resmi web sitesi](https://www.selenium.dev)
- [Selenium komutları ve diğer dokümantasyonlar](https://www.selenium.dev/documentation/en)
- [Atölyemizin Google Drive Klasörü](https://drive.google.com/drive/folders/1P6b4wvA9Guqq7ODGiU7MHOsOSjc_oHne?usp=sharing)
- [openpyxl - Python Excel kütüphanesi dokümantasyonu](https://openpyxl.readthedocs.io)

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
| **1. HAFTA**<br> <ul><li>Web otomasyon nedir?</li><li>Geliştirme ortamının hazırlanması</li></ul> |  [![1. HAFTA](https://img.youtube.com/vi/aUqnZrpmPHU/0.jpg)](https://youtu.be/aUqnZrpmPHU) |
| **2. HAFTA**<br><ul><li>Git teknolojisinin önemi ve kullanımı *(senaryo üzerinden)*</li><li>Farklı tarayıcı sürücülerinin indirilmesi ve kullanımı</li><li>Basit Selenium komutları</li></ul> | [![2. HAFTA](https://img.youtube.com/vi/BX8_AuvE-fs/0.jpg)](https://youtu.be/BX8_AuvE-fs) |
| **3. HAFTA**<br> <ul><li>HMTL elemanları nedir?</li><li>HTML elemanları Selenium ile nasıl seçilir ve kullanılır?</li><li>HTML elemanlarını daha kolay seçmek için tarayıcı eklentileri</li><li>BOT yazma atölyesinde GitHub projemizde geliştirme iş akışımız *(çalışma düzenimiz)*</li></ul> | [![3. HAFTA](https://img.youtube.com/vi/ZAChGQz3wfY/0.jpg)](https://youtu.be/ZAChGQz3wfY) |
| **4. HAFTA**<br> <ul><li>Git iş akışımız üzerine sohbet</li><li>EBA öğrenci bazlı çalışma raporlarını kontrol etme projemizin ilk adımı <ol><li>EBA'ya giriş</li><li>"Raporlar" menüsüne tıklama</li></ol></li></ul> | [![4. HAFTA](https://img.youtube.com/vi/_KtvP_fBBH8/0.jpg)](https://youtu.be/_KtvP_fBBH8) |
| **4. HAFTA EK - 1**<br> <ul><li>4. hafta dersi esnasından alınan hataların düzeltilmesi</li></ul> | [![4. HAFTA EK - 1](https://drive.google.com/uc?export=view&id=1vWyhhxAZTVfkyKLmYyYaGuonTZw11Njm)](https://drive.google.com/file/d/14IGINTzeLw3GClHOn9lSQQv5kYIz1Jw3/view) |
| **5. HAFTA** <br> <ul><li>EBA öğrenci bazlı çalışma raporlarını kontrol etme projemizin devamı <ol><li>"Çalışma Raporları" sayfasına gitme</li><li>"Öğrenci Bazlı" sayfasına gitme</li><li>Her öğrencinin tamamlama ve performans ortalamalarının alınıp ekrana yazdırılması</li><li>Öğrenci bazlı raporların ekran görüntüsünün kaydedilmesi</li></ol></li></ul> | [![5. HAFTA](https://img.youtube.com/vi/OpCIDBkmfc4/0.jpg)](https://youtu.be/OpCIDBkmfc4) |
| **5. HAFTA EK - 1** <br> <ul><li>Öğrenci çalışma bilgilerini Excel dosyasına kaydetme</li></ul> | [![5. Hafta - 1 - Öğrenci Çalışma Bilgilerini Excele Kaydetme](https://drive.google.com/uc?export=view&id=1ZYoQGzn7bzzdxdatt-MbTRloi6ljGMx0)](https://drive.google.com/file/d/1zNUL2ScjZk9wIJvDVwyzb-ktPM4UVzwY/view) |
| **5. HAFTA EK - 2** <br> <ul><li>**Projelerimizi Çalıştırmak İçin Kısayol Oluşturma** *(Her proje için kullanılabilir)*</li></ul> | [![5. Hafta - 2 - Projelerimizi Çalıştırmak İçin Kısayol Oluşturma](https://drive.google.com/uc?export=view&id=154Tg6VEctxPjEQ78PoFXN8o5V1GWDAkI)](https://drive.google.com/file/d/10PnPVxeS3_c0lDCIorg4VtWtCZvDdjvn/view) |
| **5. HAFTA EK - 3** <br> <ul><li>**Projelerimizi Otomatik Çalıştırmak İçin Zamanlama** *(Her proje için kullanılabilir)*</li></ul> | [![5. Hafta - 3 - Projelerimizi Otomatik Çalıştırmak İçin Zamanlama](https://drive.google.com/uc?export=view&id=1Z9uka24AHzJMs1dMZGFaBwqzv7Lt95Tm)](https://drive.google.com/file/d/1HSJOFsOCcWsbWiN6A8LTPYYQRlG4jA7W/view) |
| **6. HAFTA** | BEKLENİYOR... 😊|

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*

---

## Örnek Çalışmalar

| AÇIKLAMA | VİDEO BAĞLANTISI |
|:-|:-:|
| **Eleman Seçme Dersinin Etkileşimli Tekrarı** <br> 3. haftada öğrendiğimiz eleman seçme konusunun [@mehmetakifturanbt](https://github.com/mehmetakifturanbt) tarafından geliştirilen etkileşimli tekrarı  | [![3. Hafta - Örnek 1 - mehmetakifturanbt (Etkileşimli eleman seçme dersi tekrarı)](https://drive.google.com/uc?export=view&id=1mjwc2gb-4tS8NB82LYZ23HJbcEegpbau)](https://drive.google.com/file/d/1C1AGptQF-_I-Lzl0p2NiqHH_OUurBu9n/view) |
| **Öğrenci Belgesi Yazdırma** <br> [@fgunes7](https://github.com/fgunes7) tarafından geliştirilen projede öğrenci numarası verilen öğrencinin belgesi otomatik yazdırılıyor | [![3. Hafta - Örnek 2 - fgunes7 (Öğrenci belgesi yazdırma)](https://drive.google.com/uc?export=view&id=1vXGY6xCPsBm0CNBZTIydLqe6YuM1fK_3)](https://drive.google.com/file/d/1CfxVKasZvKkoUxsbeDLwc5UMtZMEJAfz/view) |
| **4. Hafta Çalışması Örneği ve Paylaşım Yapma&Silme** <br> [@Aytac-Kula](https://github.com/Aytac-Kula) tarafından geliştirilen projede 4. haftada yapılan işlemler yapılmış ve gitmek istenen sayfaya gidilmesi işlemi tamamlanmıştır. Ek olarak paylaşım yapma ve silme örnekleri gösterilmiştir. | [![4. Hafta - Örnek 3 - Aytac-Kula (EBA'da paylaşım yapma ve silme)](https://drive.google.com/uc?export=view&id=1b28DCk77ZxfOv5HZKYmOltQXtA7szx9N)](https://drive.google.com/file/d/1f0zTYKgj1gG1HoMcgMkA49S_q6fVbtpd/view) |
| **IMDB Top 250** <br> [@oguzkapan](https://github.com/oguzkapan) tarafından geliştirilen projede IMDB'de en iyi 250 film bilgileri TXT dosyasına kaydediliyor. | [![4. Hafta - Örnek 4 - oguzkapan (IMDB Top 250)](https://drive.google.com/uc?export=view&id=18OQIV4cc3JtdbJmBJsDJbwlPqPjNtpuA)](https://drive.google.com/file/d/1uWef7VQo7dPymqOsyA8kxUeKQt-hfBMC/view) |
| **EBA Tek Kullanımlık Şifre Alma** <br> [@mfatiharslan](https://github.com/mfatiharslan) tarafından geliştirilen öğrenci numarası verildikten sonra, otomatik TC bilgisini alıp, EBA tek kullanımlık şifre oluşturup TXT dosyasına yazan çalışma  | [![4. Hafta - Örnek 5 - mfatiharslan (EBA tek kullanımlık şifre oluşturma)](https://drive.google.com/uc?export=view&id=12mTmsTHNjjtP8w1V3Y7iDK8l8ghzfc6g)](https://drive.google.com/file/d/1wvvPoubyGNaDEHtdI8vSneVEyVoDK6ut/view) |

*[İçindekiler bölümüne dön!](#i%CC%87%C3%A7i%CC%87ndeki%CC%87ler)*
