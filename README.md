# SecureSphere: Dual-Mode Interactive Web Security & Defensive Coding Laboratory

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Framework](https://img.shields.io/badge/framework-Flask-black.svg)
![Security Standard](https://img.shields.io/badge/compliance-OWASP%20Top%2010-red.svg)
![Academic Level](https://img.shields.io/badge/academic-Final%20Project-brightgreen.svg)

## 📌 1. Proje Hakkında (Executive Summary)
Bu proje, **İstinye Üniversitesi Bilgisayar Teknolojileri Bölümü Bilişim Güvenliği Teknolojisi** programı bünyesinde yer alan **Güvenli Web Yazılımı Geliştirme (Secure Web Development)** dersi final çalışması olarak geliştirilmektedir. 

Projenin ana amacı; modern web uygulamalarında sıkça karşılaşılan kritik güvenlik zafiyetlerini ve bu zafiyetlerin kaynak kod seviyesinde nasıl engelleneceğini (Defansif Kodlama) deneysel olarak gösteren **çift modlu (Dual-Mode)** etkileşimli bir laboratuvar yazılımı ortaya koymaktır. Proje, sadece zafiyetleri simüle etmekle kalmaz; aynı zamanda güvenli yazılım geliştirme prensiplerinin (OWASP Top 10) sisteme nasıl entegre edileceğini somut bir şekilde kanıtlar.

---

## 👥 2. Proje Ekibi & Akademik Bilgiler
* **Üniversite:** İstinye Üniversitesi
* **Bölüm:** Bilişim Güvenliği Teknolojisi (Önlisans)
* **Ders:** Güvenli Web Yazılımı Geliştirme
* **Dönem:** Bahar 2026
* **Proje Danışmanı:** Keyvan Arasteh
* **Geliştirici:** Ezel Balım Atik ([@blmezel](https://github.com/blmezel))

---

## 🎯 3. Proje Mimarisi & Modüller (OWASP Top 10 Mapping)

Uygulamanın merkezinde, çalışma zamanında (Runtime) değiştirilebilen global bir **`SECURITY_MODE`** anahtarı yer almaktadır. Sistem, gelen tüm HTTP isteklerini bu anahtara göre iki farklı mantıksal iş motoruna yönlendirerek katmanlı savunma (Defense-in-Depth) modelini simüle eder:

```text
                  [ Client HTTP Request ]
                             │
                             ▼
               ┌───────────────────────────┐
               │   Global Security Toggle  │
               └─────────────┬─────────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
     [ SECURITY_MODE: OFF ]        [ SECURITY_MODE: ON ]
     (Vulnerable Pipeline)         (Defensive Pipeline)
              │                             │
              ▼                             ▼
    • Raw SQL Queries              • Prepared Statements
    • Unsanitized Output           • HTML Context Encoding
    • Unrestricted Access          • Rate Limiting Enabled
    • Verbose Stack Traces         • Custom Error Catchers
Proje, laboratuvar modüllerindeki isterleri tam anlamıyla karşılamak adına birbiriyle ilişkili 3 ana güvenlik konusunu tek bir çatıda birleştirir:

Modül 1: Girdi Doğrulama Laboratuvarı (Input Validation Testing - Modül 11)
Zafiyet Odaklı Durum (OFF): Kullanıcı girdileri ham (raw) şekilde SQL motoruna ve DOM'a basılır. SQL Injection (SQLi) ve Reflected XSS zafiyetlerine zemin hazırlanır.

Defansif Savunma Durumu (ON): SQL sorguları parametrik (Prepared Statements) hale getirilir ve HTML çıktıları kurallı encode edilerek XSS riskleri tamamen sıfırlanır.

Modül 2: Kimlik Doğrulama & İstek Sınırlandırma (Auth Bypass & Rate Limiting - Modül 07 & 10)
Zafiyet Odaklı Durum (OFF): Giriş paneli kaba kuvvet (Brute-Force) ve kimlik doğrulama atlama saldırılarına karşı tamamen korumasızdır. Herhangi bir istek sınırı bulunmaz.

Defansif Savunma Durumu (ON): Flask-Limiter entegrasyonu ile IP tabanlı dinamik Rate Limiting mekanizması devreye alınır, brute-force engellenir ve güvenli oturum yönetimi uygulanır.

Modül 3: Hassas Veri İfşası & Güvenli Hata Yönetimi (Sensitive Data Exposure & Error Handling - Modül 13 & 09)
Zafiyet Odaklı Durum (OFF): Backend üzerinde oluşan istisnalar (Exceptions), ham veritabanı şemaları ve sunucu iç yolları (Stack Trace) doğrudan son kullanıcıya sızdırılır.

Defansif Savunma Durumu (ON): Global Error Handler mimarisi ile hatalar maskelenir. Detaylar güvenli log dosyalarına (security.log) yazılırken kullanıcıya jenerik mesaj döner.

🛠️ 4. Kullanılan Teknolojiler ve Araçlar
Backend Dil & Framework: Python 3.10+, Flask

Güvenlik Kütüphaneleri: Flask-Limiter, Werkzeug Security

Arayüz Katmanı: HTML5, CSS3 (Flexbox Tasarım)

Analiz ve Geliştirme Ortamı: Kali Linux / Ubuntu
📂 5. Proje Klasör Yapısı
GuvenliWebProjesi/
│
├── app.py                 # Core Engine: Flask uygulamasını başlatan ve global state'i yöneten ana dosya
├── README.md              # Teknik dökümantasyon ve akademik proje kılavuzu
│
├── modules/               # Core Security Modules (İş Mantığı Katmanı)
│   ├── __init__.py        # Python paket başlatıcısı
│   ├── girdi_kontrol.py   # SQL Injection ve XSS savunma/saldırı kod blokları
│   ├── auth_kontrol.py    # Oturum yönetimi, brute-force koruması ve Rate Limit yapılandırması
│   └── veri_kontrol.py    # Bilgi ifşasını önleyen merkezi hata yakalama (Global Error Handler) motoru
│
└── templates/             # Frontend Presentation Layer (Etkileşimli Arayüz Kataloğu)
    ├── base.html          # Dinamik Güvenlik Modu anahtarını ve genel layout'u barındıran üst şablon
    ├── index.html         # Laboratuvar ana karşılama ve kontrol paneli
    ├── login.html         # Kimlik doğrulama ve brute-force test simülasyon alanı
    └── arama.html         # Girdi doğrulama ve veri filtreleme test simülasyon arayüzü
🗺️ 6. Proje Yol Haritası & Kilometre Taşları (Commit Planı)
Proje geliştirme süreci boyunca GitHub üzerinde düzenli, anlamlı ve açıklayıcı commit'lerle ilerlenecektir. Ana geliştirme takvimi şu şekildedir:

[ ] Milestone 1: Repository yapısının kurulması ve README.md dökümantasyonunun tamamlanması (Başlangıç).

[ ] Milestone 2: Ana Flask motorunun (app.py) ve dinamik Güvenlik Modu (AÇIK/KAPALI) mimarisinin kurulması.

[ ] Milestone 3: Girdi Doğrulama (girdi_kontrol.py) modülünün SQLi ve XSS ofansif/defansif kodlarının yazılması.

[ ] Milestone 4: Kimlik Doğrulama ve Flask-Limiter ile Rate Limiting (auth_kontrol.py) altyapısının kodlanması.

[ ] Milestone 5: Global Hata Yakalayıcı ve loglama sisteminin (veri_kontrol.py) entegre edilmesi.

[ ] Milestone 6: Etkileşimli HTML arayüz şablonlarının (templates/) entegrasyonu ve tüm sistemin Kali üzerinde test edilmesi.

[ ] Milestone 7: Tüm testlerin başarıyla tamamlanarak nihai final projesinin canlıya alınması ve raporlanması.

⚠️ Yasal Uyarı: Bu proje tamamen eğitim amaçlı ve İstinye Üniversitesi bünyesindeki Güvenli Web Yazılımı Geliştirme dersi laboratuvar çalışmaları için geliştirilmiştir. Zararlı faaliyetler amacıyla kullanılamaz.
