from pydantic import BaseModel
from typing import Literal


class User(BaseModel):
    name: str
    username: str
    password: str
    role: Literal["admin", "user"]
    
