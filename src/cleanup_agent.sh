#!/bin/bash
# SecureSphere Otomatik Sandbox Temizlik Scripti
TARGET_DIR="/data/sandbox/uploads"
if [ -d "$TARGET_DIR" ]; then
    find "$TARGET_DIR" -type f -not -name "*.audit" -delete
    echo "[+] Güvenli temizlik tamamlandı: Politikaya uymayan sızma dosyaları silindi."
else
    echo "[-] Hata: Hedef dizin bulunamadı."
fi
