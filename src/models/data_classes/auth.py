from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Auth(BaseModel):
    id: Optional[str]
    username: str
    password: str
    date_created: Optional[datetime]
    is_active: Optional[bool]