from pydantic import BaseModel

class DeleteParticipantRequest(BaseModel):
    table_number: int