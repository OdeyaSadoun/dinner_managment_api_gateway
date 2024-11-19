from fastapi import HTTPException
from api.routers.base_router import BaseRouter

from globals.consts.http_const_strings import HttpConstStrings
from models.data_classes.zmq_response import Response


class AuthRouter(BaseRouter):
    def __init__(self, prefix, ctrl):
        super().__init__(prefix, ctrl)
        self.setup_routes()
        
    def setup_routes(self) -> None:
        @self._router.post(HttpConstStrings.login_route)
        async def login(username: str, password: str) -> Response:
            try:
                return self._ctrl.login(username, password)
            except HTTPException as e:
                raise e
        
        @self._router.post(HttpConstStrings.register_route)
        async def register(username: str, password: str) -> Response:
            try:
                return self._ctrl.register(username, password)
            except HTTPException as e:
                raise e

