import json
from typing import Any, Dict, Optional
from pydantic import BaseModel

from globals.enums.response_status import ResponseStatus
from globals.consts.zmq_const_strings import ZMQConstStrings


class Response():
    def __init__(self, status: ResponseStatus, data: Dict = {}) -> None:
        self.status = status
        self.data = data
        
    status: ResponseStatus
    data: Optional[Dict] = None
    
    def to_json(self) -> Any:
        return json.dumps({
            ZMQConstStrings.status_identifier: self.status.name,
            ZMQConstStrings.data_identifier: self.data
        })

    @classmethod
    def from_json(self, json_str: str) -> Any:
        json_dict = json.loads(json_str)
        status = ResponseStatus[json_dict[ZMQConstStrings.status_identifier]]
        data = json_dict.get(ZMQConstStrings.data_identifier, {})
        return self(status=status, data=data)

