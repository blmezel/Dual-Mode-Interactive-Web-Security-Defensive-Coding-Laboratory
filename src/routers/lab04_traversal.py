from fastapi import APIRouter, Query
from src.security.file_sandbox import read_file_vulnerable, read_file_secure, ensure_safe_directory_exists

router = APIRouter(prefix="/lab04", tags=["Lab 04 - Path Traversal & Sandbox"])

# Başlangıçta klasörü garantiye al
ensure_safe_directory_exists()

@router.get("/vulnerable")
async def get_file_vulnerable(filename: str = Query(..., description="Örn: ../../../../../etc/passwd")):
    """
    Saldırgan (Attacker) Modu:
    Zafiyetli kod kullanıldığı için ana dizinin dışına çıkılarak Linux sistem dosyaları okunabilir.
    """
    content = read_file_vulnerable(filename)
    return {"filename": filename, "status": "Success", "content": content}

@router.get("/secure")
async def get_file_secure(filename: str = Query(..., description="Örn: ../../../../../etc/passwd")):
    """
    Savunma (Defender) Modu:
    Aynı saldırı kodu (payload) gönderilse bile Sandbox (open_basedir) koruması anında engeller.
    """
    content = read_file_secure(filename)
    return {"filename": filename, "status": "Secure", "content": content}
