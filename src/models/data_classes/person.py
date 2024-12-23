from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    name: str
    phone: str
    table_number: int
    is_reach_the_dinner: bool
