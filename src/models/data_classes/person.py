from datetime import datetime
from pydantic import BaseModel
from typing import Literal, Optional


class Person(BaseModel):
    name: str
    phone: str
    table_number: int
    is_reach_the_dinner: bool
    gender: Literal["male", "female"]
    contact_person: str
    add_manual: bool