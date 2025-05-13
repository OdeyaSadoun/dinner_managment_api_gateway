from pydantic import BaseModel

class DeleteParticipantRequest(BaseModel):
    table_number: int
    is_reach_the_dinner: bool