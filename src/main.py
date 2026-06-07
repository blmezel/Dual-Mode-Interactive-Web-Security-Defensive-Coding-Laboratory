from fastapi import FastAPI
from contextlib import asynccontextmanager
import redis.asyncio as redis
import os
from dotenv import load_dotenv

# Çevre değişkenlerini güvenli bir şekilde yüklüyoruz
# Load environment variables securely
load_dotenv()

# Global Redis istemcisi tanımlaması (Bağımlılık enjeksiyonu için)
redis_client = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Uygulama yaşam döngüsü yöneticisi.
    Sistem başlarken Redis bağlantısını kurar, kapanırken temizler.
    """
    global redis_client
    
    # .env dosyasından Redis yapılandırmalarını alıyoruz
    host = os.getenv("REDIS_HOST", "127.0.0.1")
    port = int(os.getenv("REDIS_PORT", 6379))
    
    # Redis asenkron bağlantısını başlatıyoruz
    redis_client = redis.Redis(host=host, port=port, decode_responses=True)
    
    yield # Uygulama bu noktada çalışmaya başlar
    
    # Uygulama kapanırken kaynak sızıntısını önlemek için bağlantıyı kapatıyoruz
    await redis_client.close()

# FastAPI uygulamasını tanımlıyoruz
app = FastAPI(
    title="Dual-Mode Web Security Laboratory",
    description="BGT208 - Interactive Attacker/Defender Lab",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
async def health_check():
    """
    Laboratuvarın ana giriş noktası (Health Check).
    Sistemin ayakta olup olmadığını kontrol eder.
    """
    return {
        "status": "online",
        "message": "Welcome to the Web Security Lab",
        "mode": "Initialization"
    }
