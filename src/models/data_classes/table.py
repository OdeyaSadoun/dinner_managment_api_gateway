from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

from models.data_classes.person import Person


class Table(BaseModel):
    id: Optional[str]
    people_list: List[Person]
    date_created: Optional[datetime]
    is_active: Optional[bool]