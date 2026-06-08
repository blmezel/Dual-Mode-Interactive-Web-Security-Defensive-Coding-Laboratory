# Araştırma Lab: Olay Analizi (Incident Response & Case Studies)

Bu doküman, interaktif laboratuvar modüllerine teorik altyapı sağlaması amacıyla, kritik siber güvenlik olaylarının ve zafiyetlerinin mimari düzeyde analizini içermektedir.

## 1. Vercel Supply Chain Hack (Nisan 2026)

Tedarik zinciri (Supply Chain) saldırıları, modern CI/CD boru hatlarını (pipelines) hedef alan en yıkıcı vektörlerden biridir. Nisan 2026'da gerçekleşen bu olayda, üçüncü parti bağımlılıkların manipülasyonu yoluyla sistem bütünlüğü ihlal edilmiştir.

* **Saldırı Vektörü:** NPM (Node Package Manager) ekosistemine sızdırılan zararlı paketler (Malicious Typo-Squatting / Dependency Confusion).
* **Teknik Etki:** Geliştirme ortamlarına sızılması, `.env` dosyalarındaki kritik ortam değişkenlerinin (API anahtarları, DB şifreleri) dışarı sızdırılması (Data Exfiltration) ve sunucusuz (Serverless) fonksiyon çalışma zamanlarına müdahale.
* **Savunma Mimarisi Önerileri:**
  * Bağımlılıkların sıkı bir şekilde kilitlenmesi (Strict Dependency Locking).
  * CI/CD sürecinde düzenli SCA (Software Composition Analysis) araçlarının (Snyk, Dependabot vb.) kullanılması.
  * Zero-Trust (Sıfır Güven) mimarisi prensipleriyle servis hesaplarına "En Az Yetki" (Least Privilege) ilkesinin uygulanması.

---

## 2. React2Shell Vulnerability (Aralık 2025)

İstemci tarafı (Frontend) framework'lerinin sunucu tarafı işleme (Server-Side Rendering - SSR) süreçlerine entegrasyonunda oluşan zafiyetlerin en kritik örneklerinden biridir. Bu zafiyet, görünürde zararsız olan UI bileşenlerinin sunucuyu ele geçirmek için kullanılabileceğini kanıtlamıştır.

* **Zafiyetin Doğası:** React Server Components (RSC) mimarisinde, istemci tarafından gönderilen serileştirilmiş durum (serialized state) verilerinin sunucuda yeterli sanitizasyon işleminden geçirilmemesi.
* **Sömürü Yöntemi (Exploitation):** Saldırganın, gönderilen payload içerisine zararlı Node.js komutları enjekte etmesi ve bu komutların SSR parse aşamasında çalıştırılarak Uzaktan Kod Çalıştırma (Remote Code Execution - RCE) ve Reverse Shell elde edilmesi.
* **Sıkılaştırma Stratejisi:**
  * SSR katmanında katı veri tipi doğrulaması (Strict Input Validation) yapılması.
  * Sunucu bileşenlerinin çalıştırıldığı ortamların (Konteyner/Sandbox) yetkilerinin kısıtlanması.
  * Gelişmiş WAF (Web Application Firewall) kurallarının, JSON ve RSC payload'larındaki anomali kalıplarını algılayacak şekilde güncellenmesi.
