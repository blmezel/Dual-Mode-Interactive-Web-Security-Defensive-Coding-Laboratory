# Modül 4: open_basedir & Dosya Sistemi Korumalı Alan

## 1. Path Traversal PoC (Öncesi / Sonrası)
- **Öncesi (Vulnerable):** `GET /lab04/vulnerable?filename=../../../../../../etc/passwd` işlemi başarıyla kök dizine ulaşıp sistem kullanıcılarını listeler.
- **Sonrası (Secure):** `GET /lab04/secure?filename=../../../../../../etc/passwd` işlemi `os.path.abspath` filtresine takılır ve HTTP 403 Forbidden hatası döner.

## 2. Üç Yaklaşım Karşılaştırması
| Yaklaşım | Avantajı | Dezavantajı |
|---|---|---|
| **Kod Seviyesi (os.path.abspath)** | Hızlı, uygulamaya entegre, ekstra araç gerektirmez. | Geliştirici hatasına açıktır, bir yerde unutulursa sistem hacklenir. |
| **open_basedir / chroot** | Dil/Sistem seviyesinde izolasyon sağlar. Daha güvenlidir. | Yapılandırması zordur, paylaşımlı kütüphaneleri bozabilir. |
| **Docker (Konteyner)** | Tamamen izole bir işletim sistemi çekirdeği sunar. En güvenlisidir. | Kaynak tüketimi fazladır, karmaşıklık yaratır. |

## 3. Seccomp Politika Tasarımı (Kavramsal)
Sistem çağrılarını (syscalls) sınırlandırmak için özel Docker Seccomp profilimiz:
- `open`, `openat`, `read`, `close` çağrılarına sadece belirli dizinler için izin verilir.
- `execve` (shell çalıştırma) ve `ptrace` (hata ayıklama) çağrıları saldırıyı engellemek için **tamamen bloklanmıştır**.
