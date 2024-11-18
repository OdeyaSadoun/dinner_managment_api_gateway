from abc import abstractmethod


class IZMQClientManager:
    @abstractmethod
    def send_request(self, request):
        pass