from fastapi import APIRouter, Request, HTTPException, status
from pydantic import BaseModel
from src.security.brute_force import process_login_attempt

router = APIRouter(prefix="/lab02", tags=["Lab 02 - Progressive Brute Force"])

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
async def simulated_login(request: Request, data: LoginData):
    client_ip = request.client.host
    is_correct_password = (data.password == "SuperSecret123!")
    
    await process_login_attempt(data.username, client_ip, is_correct_password)
    
    if not is_correct_password:
        raise HTTPException(status_code=401, detail="Hatalı şifre.")
        
    return {"message": "Giriş başarılı! Sayaçlar sıfırlandı."}

@router.post("/unlock")
async def unlock_account(data: LoginData):
    from src.main import redis_client
    key = f"brute_force:{data.username}:127.0.0.1" 
    if redis_client:
        await redis_client.delete(key)
    return {"message": f"{data.username} hesabının kilidi başarıyla açıldı."}
