import os
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
import jwt

class JWTMiddleware(HTTPBearer):
    def __init__(self, roles: list[str] = None):
        super().__init__()
        self.roles = roles

    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        if not credentials:
            raise HTTPException(status_code=401, detail="Unauthorized")

        try:
            payload = jwt.decode(
                credentials.credentials,
                os.getenv("JWT_SECRET"),
                algorithms=[os.getenv("JWT_ALGORITHM")]
            )
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

        if self.roles and payload.get("role") not in self.roles:
            raise HTTPException(status_code=403, detail="Permission denied")

        request.state.user = payload
