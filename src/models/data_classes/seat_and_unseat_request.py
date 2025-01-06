from pydantic import BaseModel

class SeatAndUnseatRequest(BaseModel):
    table_id: str