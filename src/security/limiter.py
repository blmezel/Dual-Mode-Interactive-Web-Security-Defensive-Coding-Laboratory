from fastapi import Request, HTTPException, status

async def verify_rate_limit(request: Request):
    """
    Gelen isteğin IP adresine göre hız sınırını kontrol eder.
    Saldırgan (Attacker) çok fazla istek atarsa anında bloklanır.
    """
    # Redis istemcisini main modülünden içeri aktarıyoruz
    from src.main import redis_client
    
    # Redis bağlantısı henüz kurulmadıysa güvenli geçiş ver
    if not redis_client:
        return True
        
    client_ip = request.client.host
    redis_key = f"rate_limit:{client_ip}"
    
    # Sınır kontrolü (Laboratuvar için dakikada 5 istek simüle ediyoruz)
    await process_rate_limit(redis_client, redis_key, limit=5, window=60)
    return True

async def process_rate_limit(redis, key: str, limit: int, window: int):
    """
    Redis üzerindeki sayacı artırır ve TTL (yaşam süresi) belirler.
    Eğer limit aşılmışsa anında HTTP 429 hatası fırlatır.
    """
    current = await redis.get(key)
    
    # Eğer limit aşıldıysa engelleme senaryosunu tetikle
    if current and int(current) >= limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit aşıldı. Engellendiniz."
        )
        
    # Sayacı 1 artır ve süresini (pencereyi) güncelle
    await redis.incr(key)
    await redis.expire(key, window)
