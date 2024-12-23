from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Auth(BaseModel):
    username: str
    password: str
    
