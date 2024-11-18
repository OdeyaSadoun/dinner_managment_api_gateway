from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    id: Optional[str]
    personal_number: str
    name: str
    phone: str
    table_number: int
    is_reach_the_dinner: bool
    date_created: Optional[datetime]
    is_active: Optional[bool]