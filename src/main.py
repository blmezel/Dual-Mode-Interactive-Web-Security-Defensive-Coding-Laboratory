from fastapi import FastAPI
from contextlib import asynccontextmanager
import redis.asyncio as redis
import os
from dotenv import load_dotenv

# Tüm Router'ları içeri aktarıyoruz
from src.routers import lab01_middleware
from src.routers import lab02_bruteforce
from src.routers import lab03_session
from src.routers import lab04_traversal

load_dotenv()
redis_client = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Sistem başlarken Redis bağlantısını kurar, kapanırken temizler."""
    global redis_client
    host = os.getenv("REDIS_HOST", "127.0.0.1")
    port = int(os.getenv("REDIS_PORT", 6379))
    redis_client = redis.Redis(host=host, port=port, decode_responses=True)
    yield
    await redis_client.close()

app = FastAPI(
    title="Dual-Mode Web Security Laboratory",
    description="BGT208 - Interactive Attacker/Defender Lab",
    version="1.0.0",
    lifespan=lifespan
)

# Tüm Router'ları FastAPI ana uygulamasına bağlıyoruz
app.include_router(lab01_middleware.router)
app.include_router(lab02_bruteforce.router)
app.include_router(lab03_session.router)
app.include_router(lab04_traversal.router)

@app.get("/")
async def health_check():
    """Sistem ayakta mı kontrolü."""
    return {"status": "online", "message": "Welcome to the Web Security Lab"}
