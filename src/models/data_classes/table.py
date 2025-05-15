from datetime import datetime
from pydantic import BaseModel
from typing import Dict, List, Literal, Optional

from models.data_classes.person import Person


class Table(BaseModel):
    people_list: List[str]
    position: Dict[str, int]
    chairs: int
    table_number: int
    rotation: Optional[int] = 0
    gender: Literal["male", "female"]
    shape: Literal["rectangle", "circle", "square", "vip", "reserva", "bima"]
