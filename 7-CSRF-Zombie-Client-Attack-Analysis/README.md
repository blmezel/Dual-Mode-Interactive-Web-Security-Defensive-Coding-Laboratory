# 7. İstemci Tarafı Oturum Hırsızlığı ve İzleme Analizi

Hocanın Yönergesindeki Kritik Soru: "Token hırsızlığı (Token Hijacking) ve replay attack risklerine karşı ne tür bir mantıksal kontrol kurdunuz?"

## 🔍 Analiz Yanıtı ve İspatlar
* Çalınan Refresh Token'ların tekrar oynatılması (Replay Attack) durumunda, "Token Reuse Detection" mekanizması tetiklenir.
* Sistem aynı token ailesinden üretilmiş tüm aktif oturumları (Zombie Clients) anında imha ederek HTTP 401 durumuna düşürür.
