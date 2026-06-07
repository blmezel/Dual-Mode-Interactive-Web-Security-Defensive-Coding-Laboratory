from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# FastAPI'nin standart Bearer token altyapısını kullanıyoruz
security = HTTPBearer()

async def verify_authentication(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Gelen isteğin yetkilendirme (Authorization) başlığını kontrol eder.
    Geçerli bir Bearer token (kimlik kartı) sunulup sunulmadığını doğrular.
    """
    token = credentials.credentials
    
    # Token içeriğini doğrulamak için alt fonksiyona yönlendiriyoruz
    user_payload = await validate_token(token)
    return user_payload

async def validate_token(token: str):
    """
    Token'ın geçerliliğini simüle eder ve kontrol sağlar.
    Geçersiz bir token durumunda anında HTTP 401 fırlatarak işlemi keser.
    """
    # Laboratuvar için statik kontrol. (İleride JWT eklenebilir)
    if token != "lab-secret-token-123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Geçersiz veya süresi dolmuş token. Engellendiniz."
        )
    
    # Token geçerliyse örnek bir kullanıcı profili (payload) dönüyoruz
    return {"user_id": 1, "username": "test_user", "role": "user"}
