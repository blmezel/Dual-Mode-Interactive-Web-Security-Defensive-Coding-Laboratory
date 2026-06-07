import os
import logging
from fastapi import HTTPException, status

logger = logging.getLogger("SandboxLab")

# Güvenli (Sandbox) klasörümüzün mutlak (absolute) yolunu belirliyoruz
SAFE_BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), "docs", "public_files"))

def ensure_safe_directory_exists():
    """Uygulama başlarken güvenli test klasörünü ve içine örnek bir belge oluşturur."""
    os.makedirs(SAFE_BASE_DIR, exist_ok=True)
    test_file = os.path.join(SAFE_BASE_DIR, "gizli_olmayan_belge.txt")
    if not os.path.exists(test_file):
        with open(test_file, "w") as f:
            f.write("Bu belge guvenli klasor icerisindedir.")

def read_file_vulnerable(filename: str):
    """
    Zafiyetli okuma (Attacker Mode): Girdiyi temizlemeden doğrudan işletim sistemine yollar.
    Path Traversal (Dizin Atlama) saldırısına %100 açıktır.
    """
    target_path = os.path.join(SAFE_BASE_DIR, filename)
    try:
        with open(target_path, "r") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Dosya okunamadı: {str(e)}")

def read_file_secure(filename: str):
    """
    Güvenli okuma (Defender Mode): open_basedir mantığını Python'da simüle eder.
    Dosya yolunu normalize eder ve sadece SAFE_BASE_DIR içinde mi diye kontrol eder.
    """
    # 1. Beklenen tam yolu oluştur ve '..' gibi hileli ifadeleri normalize et (çöz)
    target_path = os.path.abspath(os.path.join(SAFE_BASE_DIR, filename))
    
    # 2. Normalize edilmiş yol, bizim güvenli ana dizinimizle mi başlıyor kontrol et
    if not target_path.startswith(SAFE_BASE_DIR):
        logger.warning(f"PATH TRAVERSAL ENGELLENDİ! Hedef: {target_path}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Güvenlik İhlali: Korumalı alan (open_basedir) dışına çıkılamaz!"
        )
        
    try:
        with open(target_path, "r") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=404, detail="Dosya bulunamadı.")
