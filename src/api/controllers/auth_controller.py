class AuthController():
    def __init__(self, zmq_client):
        super().__init__()
        self._zmq_client = zmq_client