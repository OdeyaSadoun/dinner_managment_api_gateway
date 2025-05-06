from pydantic import BaseModel

class ParticipantSticker(BaseModel):
    full_name: str
    gender: str 
    table_number: int
