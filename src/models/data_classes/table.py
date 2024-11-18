from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Table(BaseModel):
    id: Optional[str]
    date_created: Optional[datetime]
    is_active: Optional[bool]