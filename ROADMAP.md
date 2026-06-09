# SecureSphere Geliştirme Yol Haritası (Roadmap)

## 🟩 Aşama 1: Tamamlanan Katmanlar
* [x] FastAPI ve Starlette Middleware Pipeline tasarımı
* [x] Redis Kayar Pencere (Sliding Window) entegrasyonu
* [x] Path Traversal için Canonical Path doğrulaması

## 🟨 Aşama 2: Yakındaki Güncellemeler
* [ ] Orijinal TLS/SSL sertifikasyon yapısının Nginx üzerine gömülmesi
* [ ] JWT Token ailesi için otomatik rotasyon mekanizması testleri
* [ ] WebSockets el sıkışma aşaması için durumsal doğrulama kalkanı.
      # 🗺️ SecureSphere: Geliştirme Yol Haritası ve Süreç Felsefesi

> "Önce anla, sonra kodla." Her problemi küçük, sıralı parçalara böl. Bir dedektif gibi düşün: gözlemle, ham veriyi çevir, desenleri tespit et, raporla.

---

## 🏁 Faz 0: Yazmadan Önce Anla
- **Gözlem ve Planlama:** Web uygulamasındaki boru hattı (Middleware Pipeline) mimarisi kodlamaya geçilmeden önce teorik olarak şemalandırılmıştır.
- **Tehdit Modellemesi:** Hız sınırlandırıcı (Rate Limiter), Kimlik Doğrulama (Auth) ve Rol Bazlı Erişim Kontrolü (RBAC) katmanlarının sıralama stratejisi sunucu yükünü ve DoS risklerini minimize edecek şekilde tasarlanmıştır.

## 🔬 Faz 1: Araştırma ve Keşif
- **Zafiyet Taraması:** Kurulum betiklerindeki (`install.sh`) körü körüne çalıştırma riskleri incelenmiş, SHA256 imza kontrol entegrasyonu araştırılmıştır.
- **Dizin Atlama Analizi:** `src/sandbox_jail.py` üzerinde double-url encode edilmiş girdilerin yaratabileceği Path Traversal atak vektörleri ve Canonical Path süzgeçleri (`os.path.commonpath`) simüle edilmiştir.
- **Raporlama:** Tüm teorik bulgular siber güvenlik araştırma günlüğü olarak `docs/research/` dizini altında kayıt altına alınmıştır.

## ⚙️ Faz 2: Ortam Kurulumu
- **İzolasyon Hattı:** Uygulamanın ana host işletim sistemine zarar vermesini engellemek üzere `Dockerfile` ve `docker-compose.yml` yapılandırmaları kurgulanmıştır.
- **Sıkılaştırma:** Konteyner süreçlerinin root yetkilerini tamamen düşüren `cap_drop: - ALL` kuralı ve salt-okunur dosya sistemi (`read_only: true`) altyapısı yerel test ortamında başarıyla ayağa kaldırılmıştır.

## 💻 Faz 3: Uygulama (Modül Başına ≤10 Adım)
- **Lab 01 (Middleware & RBAC):** Asenkron FastAPI ve Starlette boru hattı sıralı filtreleme yapısıyla kodlanmıştır. Yetkisiz admin istekleri `HTTP 403 Forbidden` ile bloklanmıştır.
- **Lab 02 (Progressive Brute Force):** Ardışık kaba kuvvet ataklarına karşı üstel geciktirme faktörü uygulayan atomik Redis Lua Script mimarisi entegre edilmiştir. Hesap kilitlenmeleri `HTTP 423 Locked` durum kodu ile haritalandırılmıştır.

## 🧪 Faz 4: Test ve Raporlama
- **Siber Denetim:** Geliştirilen savunma kalkanları ofansif scriptlerle (Attacker Mode) test edilmiş, üretilen HTTP durum kodları ve durumsal loglar doğrulanmıştır.
- **Yapay Zeka Audit Raporu:** Antigravity AI Agent standartlarına tam uyumlu statik kod analizi ve adli bilişim log imha süreçleri `cyber_resilience_report.md` dosyası olarak ana dizine mühürlenmiştir.

## 🏁 Faz 5: Teslim Kontrol Listesi
- [x] `README.md` ana belgeleme ve akademik meta-veriler eksiksiz tamamlandı.
- [x] `Dockerfile` ve `docker-compose.yml` Zero Trust kurallarına göre sıkılaştırıldı.
- [x] `docs/research/` ve `docs/modules/` klasör hiyerarşisi kuruldu.
- [x] Toplam commit geçmişi siber yama adımlarıyla birlikte 70+ seviyesine (73 Commit) ulaştırıldı.
