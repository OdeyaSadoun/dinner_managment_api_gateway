from typing import Any
from fastapi import APIRouter

from dinner_managment_api_gateway.src.infrastructures.interfaces.icontroller_manager import IControllerManager


class BaseRouter:
    def __init__(self, prefix: str, ctrl: IControllerManager) -> None:
        self._router = APIRouter()
        self.prefix = prefix
        self._ctrl = ctrl

    def setup_routers(self) -> None:
        pass

    def get_router(self) -> Any:
        return self._router