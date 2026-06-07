import json
import logging
from fastapi import Request, HTTPException, status

logger = logging.getLogger("SessionMonitorLab")

async def verify_session_integrity(request: Request, session_id: str):
    """
    Oturum hırsızlığı tespiti (Auth Lab §11).
    Gelen isteğin IP ve User-Agent bilgilerini, oturumun orijinal bilgileriyle karşılaştırır.
    """
    from src.main import redis_client
    
    if not redis_client:
        return True # Redis yoksa geçişe izin ver
        
    session_data_str = await redis_client.get(f"session:{session_id}")
    
    if not session_data_str:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Oturum bulunamadı veya süresi dolmuş."
        )
        
    session_data = json.loads(session_data_str)
    
    # Güncel istekteki bilgileri al
    current_ip = request.client.host
    current_ua = request.headers.get("User-Agent", "Unknown")
    
    # Anomali kontrolleri
    anomalies = []
    if session_data.get("ip") != current_ip:
        anomalies.append(f"IP Değişimi tespit edildi: {session_data.get('ip')} -> {current_ip}")
        
    if session_data.get("user_agent") != current_ua:
        anomalies.append("User-Agent değişimi tespit edildi.")
        
    # Anomali varsa oturumu anında iptal et ve hata fırlat
    if anomalies:
        logger.error(f"OTURUM HIRSIZLIĞI TESPİTİ: {session_id} - Nedenler: {', '.join(anomalies)}")
        # Oturumu Redis'ten sil
        await redis_client.delete(f"session:{session_id}")
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Güvenlik ihlali tespit edildi. Oturumunuz iptal edildi. Lütfen yeniden giriş yapın."
        )
        
    return True

async def create_secure_session(session_id: str, ip: str, user_agent: str):
    """
    Yeni bir oturum oluşturulduğunda cihaz parmak izini Redis'e kaydeder.
    """
    from src.main import redis_client
    
    if redis_client:
        session_data = {
            "ip": ip,
            "user_agent": user_agent,
            "status": "active"
        }
        # Oturumu 30 dakika (1800 saniye) geçerli olacak şekilde kaydet
        await redis_client.setex(f"session:{session_id}", 1800, json.dumps(session_data))
        logger.info(f"Yeni güvenli oturum oluşturuldu: {session_id}")
