import json
from typing import Any, Dict, Optional

from infrastructures.utils.seralization import Serializer
from globals.consts.zmq_const_strings import ZMQConstStrings


class Request():
    def __init__(self, resource: str, operation: str, data: Dict = {}) -> None:
        self.resource = resource
        self.operation = operation
        self.data = data
        
    resource: str
    operation: str
    data: Optional[Dict] = None

    def to_json(self) -> Any:
        print("data", self.data)
        obj = json.dumps(Serializer.serialize_data({
            ZMQConstStrings.resource_identifier: self.resource,
            ZMQConstStrings.operation_identifier: self.operation,
            ZMQConstStrings.data_identifier: self.data
        }))
        print("obj", obj)
        return obj
    
    @classmethod
    def from_json(self, json_str: str) -> Any:
        request = json.loads(json_str)
        return self(resource=request[ZMQConstStrings.resource_identifier], 
                    operation=request[ZMQConstStrings.operation_identifier], 
                    data=request.get(ZMQConstStrings.data_identifier, {}))
    
