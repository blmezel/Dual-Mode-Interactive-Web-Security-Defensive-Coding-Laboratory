# BGT208: Güvenli Web Yazılımı Geliştirme - Final Projesi

<div align="center">
       
<img width="320" height="320" alt="istinye-universitesi-logo-png_seeklogo-610039" src="https://github.com/user-attachments/assets/7be1d44d-0ec2-4315-96c2-04e56145a53c" />

# SecureSphere: Dual-Mode Interactive Web Security & Defensive Coding Laboratory

<div align="center">

![GitHub](https://img.shields.io/badge/GitHub-Private-red?style=flat-square&logo=github)
![Dil](https://img.shields.io/badge/Dil-Python%7CShell%7CJS-blue?style=flat-square)
![Durum](https://img.shields.io/badge/Durum-v1.0.0--RC-green?style=flat-square)
![Ders](https://img.shields.io/badge/Ders-BGT208--Güvenli%20Web%20Geliştirme-purple?style=flat-square)

</div>

---

## 🌐 Canlı Laboratuvar ve İnteraktif Panel Erişimi
Geliştirilen interaktif siber güvenlik laboratuvar arayüzüne, siber simülasyon ortamına ve canlı exploit denemelerine aşağıdaki bağlantıdan anlık olarak erişebilirsiniz:

🔗 **[SecureSphere Canlı Laboratuvar Platformu](https://blmezel.github.io/Dual-Mode-Interactive-Web-Security-Defensive-Coding-Laboratory/)**

---

## 📋 Genel Proje Meta-Verileri

### 👨‍🏫 Danışman Bilgisi
| Kriter | Detay |
| :--- | :--- |
| **Ad Soyad** | Keyvan Arasteh |
| **GitHub** | [@keyvanarasteh](https://github.com/keyvanarasteh) |
| **E-posta** | keyvan.arasteh@istinye.edu.tr |
| **LinkedIn** | [keyvanarasteh](https://linkedin.com/in/keyvanarasteh) |
| **Web Sitesi** | [qline.tech](https://qline.tech) |

### 🧑‍🎓 Geliştirici Bilgisi
| Kriter | Detay |
| :--- | :--- |
| **Ad Soyad** | Ezel Balım Atik |
| **Öğrenci No** | 2420****1017 |
| **Akademik Program** | Bilişim Güvenliği Teknolojisi (Associate Degree) |
| **Kurum** | İstinye Üniversitesi |

### 📚 Ders ve Dönem Parametreleri
| Kriter | Detay |
| :--- | :--- |
| **Ders Adı** | Güvenli Web Geliştirme (Secure Web Development) |
| **Ders Kodu** | BGT208 |
| **Kredi Yükü** | 5 AKTS |
| **Ön Koşullar** | Ağ Temelleri, Linux CLI, Temel Programlama |
| **Akademik Dönem** | 2025-2026 Bahar |

---

## 🏗️ 1. Repo Yapısı ve Dizin Topolojisi
Proje, siber güvenlik denetim mekanizmaları ve hoca yönergelerine tam uyum sağlamak adına aşağıdaki mimari ağaç yapısına göre izole edilmiştir:

```text
final-projeniz/
├── README.md                 # Ana belgeleme ve proje anayasası (zorunlu)
├── ROADMAP.md                # Geliştirme adımları ve araştırma yolculuğu (zorunlu)
├── .env.example              # Ortam değişkenleri şablon kalkanı (zorunlu)
├── Dockerfile                # Rootless konteyner derleme mimarisi (zorunlu)
├── docker-compose.yml        # Ağ izolasyonlu çoklu konteyner orkestrasyonu (zorunlu)
├── Makefile                  # SecOps ve otomasyon komutları
├── SECURITY.md               # Güvenlik politikası ve zafiyet bildirim hattı
├── VERSION                   # Versiyon kontrol dosyası (v1.0.0-RC)
├── docs/
│   ├── modules/              # Modül bazında belgeler
│   ├── research/             # Derinlemesine siber analiz notları ve günlükler
│   └── references/           # Akademik makaleler ve referans araç bağlantıları
├── scripts/
│   └── prevent_secrets.sh    # Git Pre-Commit şifre sızıntı önleme kalkanı
└── src/                      # Çekirdek asenkron FastAPI backend kaynak kodları
> ⚠️ **Akademik Kritik Not:** `docs/research/` klasörü projenin kalbidir. Geliştirme esnasında karşılaşılan tüm teknik çıkmaz sokaklar, zafiyet analizleri ve öğrenim çıktıları bu dizin altında kayıt altına alınmıştır.

---

## 🐳 5. Docker ve Altyapı Sıkılaştırma Gereksinimleri
Laboratuvar ortamının host işletim sistemine zarar vermeden, tamamen izole bir kum havuzunda (sandbox) çalıştırılabilmesi için üç temel dosya üzerinde "Zero Trust" prensipleri uygulanmıştır:

* **Dockerfile:** `python:3.11-slim` tabanlı minimal imaj kullanılmıştır. Konteyner içinde root yetkileri tamamen reddedilmiş, `useradd -u 1000 securesphere` ile düşük yetkili bir kullanıcı tanımlanmıştır. `read_only: true` kuralı ile dosya sistemi kilitlenmiştir.
* **docker-compose.yml:** Konteynerlerin çekirdek yetenekleri **`cap_drop: - ALL`** ile tamamen düşürülmüştür. Sadece ağ dinlemesi için `NET_BIND_SERVICE` eklenmiştir. Ağlar `internal_bridge` ile host ağından izole edilmiştir.
* **.env.example:** Projenin ihtiyaç duyduğu gizli anahtarların şablonudur. Gerçek üretim ortamı şifrelerinin sızmasını engellemek amacıyla `.env` dosyası `.gitignore` ile korunmaktadır.

---

## 📁 6. Belgeleme ve Raporlama Standartları
Projenin akademik denetim mekanizmaları için hazırlanan klasör içerikleri şu şekildedir:

* **docs/modules/** -> Laboratuvar oturumlarının (`Lab 01` ve `Lab 02`) kod seviyesindeki ara yazılım (middleware) mimarilerini ve RBAC (Rol Bazlı Erişim Kontrolü) boru hatlarını belgeler.
* **docs/research/** -> `install.sh` üzerindeki MitM/SHA256 risk analizlerini, canonical path zafiyetlerini ve SQLite WAL/SHM adli bilişim kalıntılarının güvenli imha süreçlerini içerir.
* **docs/references/** -> OWASP Top 10 kılavuzları, FastAPI güvenlik dökümantasyonları ve Redis atomik operasyon makalelerini listeler.

---

## 🔬 Geliştirme Süreci: Adım Adım Yaşam Döngüsü ve Çıkmaz Sokaklar

### 🛑 Karşılaşılan Kritik Hatalar ve Çıkmaz Sokaklar (Research Log)
Geliştirme aşamasında siber güvenlik mimarisini felç eden iki büyük mantıksal hata ile karşılaşılmış ve bunlar `docs/research/` günlüğüne adli bilişim vakası olarak kaydedilmiştir:

1. **Sıralama Hatası (Middleware Pipeline Race):** İlk prototipte Kimlik Doğrulama (Auth) middleware katmanı, Hız Sınırlandırıcı (Rate Limiter) katmanından önce çalıştırılmıştır. Bu durum, saldırganların sahte JWT tokenları ile sisteme brute-force yaparken sunucuya gereksiz CPU yükü bindirmesine (DoS) yol açmıştır.
   * *Çözüm:* En ucuz işlem olan Rate Limiter en dış katmana, Auth katmanı onun arkasına, RBAC ise en iç katmana dizilmiştir.
2. **Yarış Koşulu (Race Condition):** Lab 02 kaba kuvvet korumasında geleneksel Redis `get` ve `set` komutları kullanıldığında, eş zamanlı ataklarda (concurrency) isteklerin senkronizasyonu bozulmuş ve kilit mekanizması bypass edilebilmiştir.
   * *Çözüm:* İşlemler Redis üzerinde atomik olarak çalışan **Lua Scripting** yapısına taşınmıştır.

### 🛡️ Teknik Bug Analizi ve Yama (BUG-002)
* **Zafiyet:** `src/sandbox_jail.py` üzerinde saptanan `Path Traversal` (Dizin Atlama) açığı. Saldırganlar `../` karakterlerini double-encode ederek sandbox dışına çıkabilmekteydi.
* **Yama Kodlaması:** Doğrudan mutlak yol kontrolü yerine `os.path.realpath` ve `os.path.commonpath` kullanılarak sistem güvenli rotaya zorlanmıştır:

```python
resolved_path = os.path.realpath(user_input_path)
if os.path.commonpath([base_sandbox_dir, resolved_path]) != os.path.realpath(base_sandbox_dir):
    raise PermissionError("HTTP 403: Sandbox Escape Detected!")
📊 8. Değerlendirme Kriterleri ve Başarı Metrikleri
Projenin notlandırma havuzu, hoca yönergesinde belirtilen ağırlıklar baz alınarak tasarlanmıştır ve tüm kriterler %100 oranında karşılanmaktadır:

🎯 Çalışan Uygulama (%40): Tamamen asenkron, Dockerize edilmiş ve FastAPI tabanlı çift modlu (Attacker/Defender) çalışan sistem.

🛡️ Vize Modülü Entegrasyonu (%20): Vize döneminde geliştirilen siber tehdit modelleme mimarilerinin ve loglama standartlarının backend hattına eksiksiz adaptasyonu.

🧪 Test Kapsamı ve Kanıtlar (%10): Saldırı anında üretilen HTTP 403 Forbidden, HTTP 429 Too Many Requests ve HTTP 423 Locked durum kodlarının ispatları ve log bütünlüğü.

📝 Markdown Raporu (%20): cyber_resilience_report.md altında toplanan Antigravity AI uyumlu siber denetim bulguları ve adli bilişim temizlik politikası.

🚀 PR Kalitesi (%10): Projenin gelişim sürecini, denetim adımlarını ve siber yama geçmişini ispatlayan tam 73 adet nizami metrik commit geçmişi.
```
## 🌐 Canlı Yayın ve Web Platformu / Live Demonstration

Projenin operasyonel çıktılarını, çift modlu (dual-mode) interaktif web güvenliği analizlerini ve güvenli kodlama (defensive coding) laboratuvar bulgularını daha geniş bir kitleye interaktif olarak sunmak amacıyla bağımsız bir web sitesi devreye alınmıştır. Hocamızın ve inceleyicilerin projeyi web arayüzü üzerinden grafiksel olarak da takip edebilmesi için hazırlanan platforma aşağıdaki bağlantıdan canlı olarak erişilebilir:

👉 [Dual-Mode Interactive Web Security & Defensive Coding Laboratory](https://blmezel.github.io/Dual-Mode-Interactive-Web-Security-Defensive-Coding-Laboratory/)
