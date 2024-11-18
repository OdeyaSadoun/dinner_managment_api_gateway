from fastapi import APIRouter


class BaseRouter:
    def __init__(self, prefix, ctrl):
        self._router = APIRouter()
        self.prefix = prefix
        self._ctrl = ctrl

    def setup_routers(self):
        pass

    def get_router(self):
        return self._router