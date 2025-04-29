from pydantic import BaseModel

class ParticipantSticker(BaseModel):
    name: str
    phone: str
    table_number: str
