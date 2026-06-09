# 6. Middleware Boru Hattı Sıralama Güvenliği

Hocanın Yönergesindeki Kritik Soru: "Bulduğunuz auth mekanizmasına dışarıdan nasıl saldırılabilir? Sıralama doğruluğu neden kritik?"

## 🔍 Analiz Yanıtı ve İspatlar
* Hız Sınırlandırıcı (Rate Limiter) ara yazılımı, Kimlik Doğrulama (Auth) middleware katmanından ÖNCE çalışmak zorundadır.
* Sıralamanın ters olması durumunda, saldırganlar geçerli bir token araması yaparken sunucu kaynaklarını (CPU/RAM) kaba kuvvet saldırılarıyla tüketebilir ve DoS durumuna yol açabilir.
