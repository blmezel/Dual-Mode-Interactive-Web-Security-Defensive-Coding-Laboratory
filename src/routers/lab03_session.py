from fastapi import APIRouter, Request, Header
from pydantic import BaseModel
import uuid
from src.security.session_monitor import create_secure_session, verify_session_integrity

router = APIRouter(prefix="/lab03", tags=["Lab 03 - Session Hijacking"])

class SessionCreateResponse(BaseModel):
    session_id: str
    message: str

@router.post("/create-session", response_model=SessionCreateResponse)
async def initialize_session(request: Request):
    """
    Savunma (Defender) modunda güvenli bir oturum başlatır.
    İsteği yapanın IP ve User-Agent bilgisini parmak izi olarak kaydeder.
    """
    client_ip = request.client.host
    user_agent = request.headers.get("User-Agent", "Unknown")
    
    # Rastgele bir oturum ID'si üret
    session_id = str(uuid.uuid4())
    
    # Oturum bilgilerini Redis'e kaydet
    await create_secure_session(session_id, client_ip, user_agent)
    
    return {"session_id": session_id, "message": "Oturum başarıyla oluşturuldu."}

@router.get("/access-data")
async def access_sensitive_data(request: Request, x_session_id: str = Header(..., description="Oturum ID")):
    """
    Saldırgan (Attacker) çalınan bir oturum ID'si ile bu uç noktaya erişmeye çalışır.
    Oturum hırsızlığı motoru, IP veya UA uyuşmazlığında erişimi reddeder.
    """
    # Oturum bütünlüğünü kontrol et
    await verify_session_integrity(request, x_session_id)
    
    return {"message": "Doğrulama başarılı. Hassas verilere erişildi."}
