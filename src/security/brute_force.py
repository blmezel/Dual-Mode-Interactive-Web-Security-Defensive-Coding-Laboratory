import asyncio
from fastapi import HTTPException, status
import logging

# Saldırı simülasyonu loglaması için yapılandırma
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BruteForceLab")

async def apply_progressive_delay(attempts: int, username: str):
    """
    Auth Lab §10 kuralı: Kademeli gecikme ve kilitleme uygular.
    Saldırgan (Attacker) modunda hızın nasıl kesildiğini gösterir.
    """
    if attempts >= 10:
        logger.error(f"KİLİTLEME: {username} için hesap kilitlendi. E-posta uyarısı tetiklendi.")
        raise HTTPException(
            status_code=status.HTTP_423_LOCKED, 
            detail="Hesap kilitlendi. Kilit açma maili gönderildi."
        )
    elif attempts >= 7:
        logger.warning(f"GECİKME: Yüksek risk! {username} - 10 saniye uyutuluyor.")
        await asyncio.sleep(10)
    elif attempts >= 4:
        logger.info(f"GECİKME: Orta risk! {username} - 2 saniye uyutuluyor.")
        await asyncio.sleep(2)

async def process_login_attempt(username: str, ip: str, success: bool):
    """
    Başarılı/başarısız girişleri Redis'e kaydeder.
    Başarısız durumlarda kademeli gecikme fonksiyonunu çağırır.
    """
    from src.main import redis_client # Döngüsel hatayı önlemek için içe aktarma
    
    key = f"brute_force:{username}:{ip}"
    
    if success:
        # Başarılı girişte sayacı tamamen temizle
        if redis_client: await redis_client.delete(key)
        return True
        
    # Başarısız girişte sayacı artır ve 15 dk (900s) ceza süresi ver
    attempts = 1
    if redis_client:
        attempts = await redis_client.incr(key)
        if attempts == 1:
            await redis_client.expire(key, 900)
            
    # Sayaca göre gecikme veya kilitleme kuralını çalıştır
    await apply_progressive_delay(attempts, username)
    return False
