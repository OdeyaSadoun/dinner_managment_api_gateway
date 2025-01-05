from datetime import datetime
from pydantic import BaseModel
from typing import Dict, List, Optional

from models.data_classes.person import Person


class Table(BaseModel):
    people_list: List[Person]
    position: Dict[str, int]
    chairs: int
    table_number: int