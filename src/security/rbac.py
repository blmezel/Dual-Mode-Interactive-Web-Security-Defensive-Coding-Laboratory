from fastapi import HTTPException, status, Depends
from typing import List

def require_roles(allowed_roles: List[str]):
    """
    Belirli rollere sahip kullanıcıların erişimine izin veren bağımlılık (dependency) oluşturur.
    Auth katmanından gelen payload'u kullanarak yetkiyi denetler.
    """
    async def role_checker(user_payload: dict):
        """
        Kullanıcının rolünün, izin verilen roller listesinde olup olmadığını kontrol eder.
        """
        user_role = user_payload.get("role")
        
        # Eğer kullanıcının rolü izin verilenler listesinde yoksa erişimi engelle
        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Yetkisiz erişim denemesi. {user_role} rolü ile bu alana giremezsiniz."
            )
            
        return user_payload
        
    return role_checker
