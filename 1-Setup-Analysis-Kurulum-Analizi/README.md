# 1. Kurulum ve `install.sh` Siber Güvenlik Analizi

Hocanın Yönergesindeki Kritik Soru: "Yazılımın indirdiği kaynaklar ne kadar güvenli? Hash kontrolü yapılıyor mu?"

## 🔍 Analiz Yanıtı ve İspatlar
* Kurulum betikleri incelendiğinde `curl | bash` mantığının körü körüne (Blind Execution) çalıştırıldığı, `sha256sum` kontrollerinin eksik olduğu saptanmıştır.
* Bu durum, Man-in-the-Middle (MitM) saldırılarına zemin hazırlamaktadır.
# HTTP 403 Forbidden Denetimleri
