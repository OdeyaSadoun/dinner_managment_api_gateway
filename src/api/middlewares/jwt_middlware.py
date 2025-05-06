import os
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
import jwt
from dotenv import load_dotenv

load_dotenv()  

class JWTMiddleware(HTTPBearer):
    def __init__(self, roles: list[str] = None):
        super().__init__()
        self.roles = roles

    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        print(1)
        if not credentials:
            raise HTTPException(status_code=401, detail="Unauthorized")
        print(2)
        try:
            payload = jwt.decode(
                credentials.credentials,
                os.getenv("JWT_SECRET"),
                algorithms=[os.getenv("JWT_ALGORITHM")]
            )
            print(3)
        except jwt.ExpiredSignatureError:
            print(4)
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            print(5)
            raise HTTPException(status_code=401, detail="Invalid token")

        print(6)
        if self.roles and payload.get("role") not in self.roles:
            print(7)
            raise HTTPException(status_code=403, detail="Permission denied")
        print(8)
        request.state.user = payload
        print(9)
