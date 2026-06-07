from fastapi import FastAPI
from contextlib import asynccontextmanager
import redis.asyncio as redis
import os
from dotenv import load_dotenv

# Router'ımızı içeri aktarıyoruz
from src.routers import lab01_middleware

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

# Router'ı FastAPI ana uygulamasına bağlıyoruz
app.include_router(lab01_middleware.router)

@app.get("/")
async def health_check():
    """Sistem ayakta mı kontrolü."""
    return {"status": "online", "message": "Welcome to the Web Security Lab"}
