from pydantic import BaseModel

class AddAndRemovePersonRequest(BaseModel):
    person_id: str