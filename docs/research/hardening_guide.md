# Config Lab: Sunucu ve Altyapı Sıkılaştırma (Hardening) Rehberi

Bu doküman, web uygulamalarının barındırıldığı sunucu altyapılarının ve yönetim panellerinin güvenliğini sağlamak amacıyla uygulanan sıkılaştırma (hardening) prosedürlerini detaylandırmaktadır.

## 1. PHP Sunucu Sıkılaştırma (PHP Hardening)

PHP tabanlı uygulamalarda, varsayılan yapılandırmalar genellikle güvenlikten ziyade uyumluluğa odaklıdır. Kritik üretim (production) ortamlarında şu adımlar uygulanmalıdır:

* **Sürüm Gizleme:** `php.ini` dosyasında `expose_php = Off` yapılandırması ile PHP sürüm bilgisinin HTTP başlıklarından sızdırılması engellenmelidir.
* **Tehlikeli Fonksiyonların Devre Dışı Bırakılması:** `disable_functions` yönergesi kullanılarak `exec`, `passthru`, `shell_exec`, `system`, `proc_open` gibi işletim sistemi seviyesinde komut çalıştırabilen fonksiyonlar kapatılmalıdır.
* **Dizin Kısıtlaması (Sandbox):** `open_basedir` direktifi ile PHP scriptlerinin sadece belirtilen dizinlerdeki dosyalara erişmesi sağlanarak "Path Traversal" (Dizin Atlama) zafiyetleri önlenmelidir (Bkz: Laboratuvar Modül 04).

## 2. Modern Altyapı Güvenliği (Next.js, Docker, Nginx)

* **Nginx (Reverse Proxy):** İstemci ile uygulama sunucusu (Next.js/Node) arasında bir kalkan olarak konumlandırılmalıdır. `server_tokens off;` ile Nginx sürümü gizlenmeli, HSTS (HTTP Strict Transport Security), X-Frame-Options ve X-Content-Type-Options gibi güvenlik başlıkları (Security Headers) Nginx üzerinden zorlanmalıdır.
* **Docker:** Konteynerler asla `root` yetkisiyle çalıştırılmamalıdır (Rootless Docker). İmajlar düzenli olarak zafiyet taramasından (Trivy vb.) geçirilmeli ve `docker-compose.yml` dosyalarında servisler arası ağ izolasyonu (Network Isolation) sağlanmalıdır.
* **Next.js:** İstemci tarafına sızabilecek `.env` değişkenleri (`NEXT_PUBLIC_` öneki almayanlar) sıkı denetlenmeli ve Content Security Policy (CSP) başlıkları ile XSS saldırıları hafifletilmelidir.

## 3. Yönetim Paneli ve İşletim Sistemi Güvenliği (cPanel & VPS)

* **VPS (Sanal Özel Sunucu):** SSH erişimi varsayılan 22 portundan farklı bir porta taşınmalı, şifreli giriş kapatılarak sadece "Public/Private Key" (Anahtar Tabanlı) kimlik doğrulama zorunlu kılınmalıdır. UFW veya iptables ile sıkı güvenlik duvarı kuralları yazılmalıdır.
* **Brute Force Koruması:** SSH ve diğer servisler için Fail2Ban kurularak, ardışık hatalı girişlerde IP adresleri otomatik olarak banlanmalıdır.
* **cPanel/WHM:** Root erişimi için İki Faktörlü Kimlik Doğrulama (2FA) zorunlu tutulmalı, cPanel'in sunduğu "Security Advisor" modülü düzenli çalıştırılarak zayıf yapılandırmalar tespit edilmelidir.
