"""
ALGORİTMA
- Kullanıcıları al. Her kullanıcı için aşağıdaki işlemleri yap.
    - Kullanıcı canlı dersler Excel dosyasından verileri al.
    - Her ders için aşağıdaki işlemleri yap.
        - Dersin Excel'deki "Durum" sütununa "bekliyor" yaz
        - Dersi Zoom'da kaydet
            - JWT Token oluştur
            - Varsayılan ders ayarlarını tanımla
            - İstenen ders ayarlarında kullanıcı ayarı değişikliği gerekiyorsa bu değişiklikleri yap
            - Ders kaydı sırasında bir hata döndürdü mü kontrol et
        - Ders Zoom'da kaydedildi ise Excel durumuna "zoom" yaz
        - Dersi EBA'da kaydet
            - "Canlı Dersler" sayfasına git
            - "Harici Canlı Ders Ekle" sayfasına git
            - Ders bilgilerini ekle
            - Konu ve Şube/Grup (birden fazla olabilir) seç
            - Öğrencileri listele
            - Dersi kaydet
        - Ders EBA'da kaydedildi ise Excel durumuna "eba" yaz
        - Ders için Telegram'da mesaj planla
        - Ders için mesaj planlandı ise durumuna "hazır" yaz

- Herhangi bir ders kaydı sırasında bir hata olursa durumunu kontrol et ve aşağıdaki işlemlerden birini yap.
    - "Durum = zoom" ise; Zoom'daki dersi sil
    - "Durum = eba" ise; Zoom'daki ve EBA'daki dersi sil
- Bütün dersler başarılı bir şekilde bittiyse; bir sonraki hafta için Excel'deki "Durum" sütununu boşalt
"""
