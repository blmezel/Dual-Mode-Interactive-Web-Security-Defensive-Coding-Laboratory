from fastapi import APIRouter, Depends, Request
from src.security.limiter import verify_rate_limit
from src.security.auth import verify_authentication
from src.security.rbac import require_roles

# Bu modüle ait tüm uç noktalar /lab01 ön ekiyle başlayacak
router = APIRouter(prefix="/lab01", tags=["Lab 01 - Middleware Pipeline"])

@router.get("/public", dependencies=[Depends(verify_rate_limit)])
async def public_endpoint(request: Request):
    """
    Sadece hız sınırlayıcı (Rate Limiter) kontrolünden geçen uç nokta.
    Auth veya RBAC gerektirmez.
    """
    return {"message": "Rate limit başarılı. Genel erişim sağlandı."}

@router.get("/protected", dependencies=[Depends(verify_rate_limit)])
async def protected_endpoint(request: Request, user_payload=Depends(verify_authentication)):
    """
    Rate Limiter -> Auth zincirini gerektiren uç nokta.
    Geçerli bir token zorunludur.
    """
    username = user_payload.get("username")
    return {"message": f"Kimlik doğrulama başarılı. Hoş geldin, {username}."}

@router.get("/admin", dependencies=[Depends(verify_rate_limit)])
async def admin_endpoint(
    request: Request,
    user_payload=Depends(verify_authentication),
    authorized=Depends(require_roles(["admin"]))
):
    """
    Tam zincir: Rate Limiter -> Auth -> RBAC.
    Sadece admin rolüne sahip geçerli tokenlar girebilir.
    """
    return {"message": "Tam zincir aşıldı. Admin paneline erişim sağlandı."}
