# BGT208: Güvenli Web Yazılımı Geliştirme - Final Projesi

<p align="center">
  <img src="<img width="600" height="600" alt="istinye-universitesi-logo-png_seeklogo-610039" src="https://github.com/user-attachments/assets/f5c03674-b542-4c14-904e-c4ad2ae47eab" />
">
</p>

# 🛡️ SecureSphere: Dual-Mode Interactive Web Security & Defensive Coding Laboratory

![Security](https://img.shields.io/badge/Security-Defensive-blue)
![OWASP](https://img.shields.io/badge/Compliance-OWASP%20Top%2010-red)
![Framework](https://img.shields.io/badge/Framework-Flask-black)
![Eğitmen](https://img.shields.io/badge/E%C4%9Fitmen-Keyvan%20Arasteh-purple)
![Ders](https://img.shields.io/badge/Ders%20Kodu-BGT208-green)

---

## 📝 İçindekiler (TOC)

1. [Proje ve Öğrenci Bilgileri](#-proje-ve-öğrenci-bilgileri)
2. [Projenin Amacı](#-projenin-amacı)
3. [Planlanan Analiz ve Geliştirme Aşamaları](#-planlanan-analiz-ve-geliştirme-aşamaları)
4. [🎯 Tespit Edilen Buglar ve Defansif Çözümler (Ek Puan)](#-tespit-edilen-buglar-ve-defansif-çözümler-ek-puan)
5. [Kullanılacak Teknolojiler](#-kullanılacak-teknolojiler)
6. [Gelişmiş Sistem Mimarisi ve DevSecOps](#-gelişmiş-sistem-mimarisi-ve-devsecops)
7. [Çıktılar ve Sonuç](#-çıktılar-ve-sonuç)

---

## 📋 Proje ve Öğrenci Bilgileri

| Kriter | Detay |
| :--- | :--- |
| **Öğrenci Adı Soyadı** | Ezel Balım Atik |
| **Üniversite & Bölüm** | İstinye Üniversitesi - Bilişim Güvenliği Teknolojisi (MYO) |
| **Ders Kodu & Adı** | BGT208 - Güvenli Web Yazılımı Geliştirme |
| **Dönem** | Bahar 2026 |
| **Eğitmen / Danışman** | Keyvan Arasteh |
| **Proje Deposu (Repo)** | [GitHub Reposuna Git (Hoca Davet Edildi)]() |
| **Seçilen Senaryo** | **Çift Modlu Etkileşimli Siber Güvenlik ve Defansif Kodlama Laboratuvarı** |

---

## 🎯 Projenin Amacı

Bu projenin amacı, modern web mimarilerinde en sık karşılaşılan kritik OWASP Top 10 zafiyetlerini simüle eden ve bu zafiyetlerin kaynak kod seviyesinde nasıl kapatılacağını (Defansif Kodlama) canlı olarak gösteren çift modlu (**Dual-Mode**) etkileşimli bir siber güvenlik laboratuvarı geliştirmektir.

Uygulama üzerinde global olarak kontrol edilebilen bir **`SECURITY_MODE`** anahtarı yer almaktadır:
* **Güvenlik Modu KAPALI (Vulnerable Mode):** Uygulama tüm katmanlarda polissiz, korumasız ve manipülasyona açık hale gelir.
* **Güvenlik Modu AÇIK (Secure Mode):** Aynı fonksiyonlar üzerinde çok katmanlı savunma prensipleri aktifleşir ve ataklar kod katmanında engellenir.

---

## 🔍 Planlanan Analiz ve Geliştirme Aşamaları

### 1️⃣ Girdi Doğrulama Laboratuvarı (Input Validation Testing - Modül 11)
* `girdi_kontrol.py` modülü altında form ve arama parametreleri işlenecektir.
* **Araştırma Sorusu:** Kullanıcıdan alınan ham veriler girdi temizleme (sanitization) işlemine tabi tutulmadığında veritabanı ve tarayıcı DOM katmanı nasıl manipüle edilebilir?
* **Planlanan Analizler:**
  * Raw SQL queries (Ham sorgular) ile SQL Injection tetikleme.
  * Unsanitized Output (Filtrelenmemiş çıktı) ile Reflected XSS simülasyonu.

### 2️⃣ Kimlik Doğrulama & İstek Sınırlandırma (Auth Bypass & Rate Limiting - Modül 07 & 10)
* `auth_kontrol.py` modülü ile oturum yönetimi ve giriş paneli güvenliği kurgulanacaktır.
* **Araştırma Sorusu:** Kimlik doğrulama sistemleri hangi katmanlarda ve hangi koruma politikalarıyla savunulmalıdır?
* **Planlanan Analizler:**
  * Brute-Force (Kaba Kuvvet) saldırılarına karşı korumasız durum analizi.
  * Mantıksal kontrolleri ve session mekanizmalarını atlatma (Auth Bypass) denemeleri.

### 3️⃣ Hata Yönetimi & Bilgi İfşası (Sensitive Data Exposure - Modül 13 & 09)
* `veri_kontrol.py` katmanında sistem hataları ve hassas veri yönetim altyapısı kurulacaktır.
* **Araştırma Sorusu:** Sistemde oluşan istisnalar (exceptions) dışarıya sızdırıldığında, saldırganlar bu verileri altyapı keşfi için nasıl kullanabilir?
* **Planlanan Analizler:**
  * Verbose Stack Traces (Detaylı hata yığınları) ile veritabanı şeması ve sunucu iç yollarının sızdırılması.
  * Açıkta bırakılan konfigürasyon ve log dosyalarının oluşturduğu risk analizi.

---

## 🪲 Tespit Edilen Buglar ve Defansif Çözümler (Ek Puan)

Analiz süreçlerinde ve laboratuvar testlerinde sistemin açık kaynak altyapısında aşağıdaki güvenlik zafiyetleri modellenmiş ve mimari defansif çözümler sunulmuştur:

* **Bug 1: Girdi Temizleme ve Parametrik Sorgu Eksikliği (Injection)**
  * *Bulgu:* Kullanıcı girdilerinin doğrudan sorgu dizileriyle birleştirildiği saptanmıştır.
  * *Defansif Çözüm:* **Parametrik Sorgular (Prepared Statements)** ve strictly-typed girdi kontrolleri zorunlu kılınmıştır. Çıktılar **HTML Context Encoding** işleminden geçirilmiştir.
* **Bug 2: Rate Limit Bypass ve Spoofing Riski**
  * *Bulgu:* İstek sınırlandırma uygulanırken sadece `X-Forwarded-For` başlığına güvenildiği saptanmıştır.
  * *Defansif Çözüm:* `Flask-Limiter` katmanlı kontrol mantığıyla entegre edilerek gerçek istemci IP doğrulaması devreye alınmıştır.
* **Bug 3: Detaylı Hata İfşası (Verbose Error Handling)**
  * *Bulgu:* Hata durumlarında ham hata mesajlarının ve veritabanı yollarının istemciye sızdırıldığı tespit edilmiştir.
  * *Defansif Çözüm:* **Global Error Handler** mimarisi kurulmuştur. Kritik sistem hataları maskelenerek `security.log` dosyasına kaydedilirken kullanıcılara jenerik hata mesajları gösterilmesi sağlanmıştır.

---

## 🛠️ Kullanılacak Teknolojiler

* **Yazılım Dili ve Framework:** Python 3.10+, Flask
* **Siber Güvenlik Kütüphaneleri:** Flask-Limiter, Werkzeug Security
* **İzole Analiz ve İşletim Sistemi:** Linux (Kali / Ubuntu)
* **Otomasyon & DevSecOps:** GitHub Actions

| Gün | Aşama | Yapılacak İş |
| :--- | :--- | :--- |
| **1** | Kurulum | Proje mimarisinin kurulması ve Flask iskeletinin oluşturulması |
| **2** | Research | `research/` klasöründe derin siber güvenlik literatür taraması |
| **3** | Ofansif Kodlama | Güvenlik modu KAPALI iken zafiyetli pipeline kodlarının yazılması |
| **4** | Defansif Kodlama | Güvenlik modu AÇIK iken savunma katmanlarının yazılması |
| **5** | DevSecOps | Dockerize süreçleri ve GitHub Actions güvenlik pipeline entegrasyonu |
| **6** | Analiz & Test | Test sonuçlarının ve log çıktılarının `test_results.md` içerisine işlenmesi |
| **7** | Final | Nihai kod doğrulaması ve projenin hocaya teslimi |

---

## 🏗️ Gelişmiş Sistem Mimarisi ve DevSecOps

Bu proje sadece temel zafiyet senaryolarıyla sınırlı kalmamış, kurumsal seviyede bir DevSecOps mimarisiyle desteklenmiştir:

* 🐳 **Docker Konteynerizasyonu (Dockerfile):** Uygulamanın izole ve güvenli bir ortamda çalışması amacıyla hafif ve güvenli bir Alpine Linux tabanlı Docker imaj mimarisi kurgulanmıştır.
* ⚙️ **CI/CD Pipeline (`.github/workflows/security.yml`):** Projeye yapılan her yeni kod eklemesinde (push), GitHub Actions üzerinden otomatik güvenlik taramaları (Security Scan) tetiklenecek şekilde otomasyon sağlanmıştır.
* 📁 **Güvenli Dosya Yönetimi:** Hassas verilerin sızmasını engellemek amacıyla `.env` dosyası kesinlikle repoya eklenmemiş, bunun yerine güvenli pratik olan `.env.example` şablonu kullanılmıştır.

---

## 📦 Beklenen Çıktılar

* 📊 **Güvenlik Risk Analizi ve Test Raporu:** `research/test_results.md` altında güvenli/güvensiz kod karşılaştırmalı çıktıları.
* 📚 **Akademik Literatür Taraması:** `research/literature_review.md` altında OWASP standartları analizi.
* 🧩 **Defansif Yazılım Mimarisi Şeması:** Çok katmanlı savunma hattını gösteren akış şeması.
* ⚙️ **Teknik README ve Dökümantasyon:** Standartlara tam uyumlu canlı repo rehberi.

> **Projenin Katkısı:** Bu çalışma sayesinde gerçek dünya web uygulamalarının güvenlik mimarisi uçtan uca simüle edilmiş, teorik defansif bilgilerin kaynak kod seviyesindeki pratik karşılıkları başarıyla gösterilmiştir. Repo profesyonelliği kapsamında hassas sırlar gizlenmiş, kod mimarisi tamamen modüler hale getirilmiş ve CI/CD süreçleriyle tam otomatik bir DevSecOps ortamı yaratılmıştır.

---

## 👨‍🏫 Eğitmen Bilgisi

* **Instructor:** Keyvan Arasteh

---

⚠️ *Yasal Uyarı: Bu proje tamamen eğitim amaçlı ve İstinye Üniversitesi bünyesindeki BGT208 kodlu Güvenli Web Yazılımı Geliştirme dersi laboratuvar çalışmaları için geliştirilmiştir. Zararlı faaliyetler amacıyla kullanılamaz.*
