from abc import ABC, abstractmethod


class IZMQClientManager(ABC):
    @abstractmethod
    def send_request(self, request):
        pass