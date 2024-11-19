from abc import ABC, abstractmethod

from models.data_classes.zmq_request import Request
from models.data_classes.zmq_response import Response


class IZMQClientManager(ABC):
    @abstractmethod
    def send_request(self, request: Request) -> Response:
        pass