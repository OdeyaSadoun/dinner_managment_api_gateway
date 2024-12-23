from fastapi import HTTPException
from api.routers.base_router import BaseRouter

from models.data_classes.auth import Auth
from globals.consts.http_const_strings import HttpConstStrings
from models.data_classes.zmq_response import Response


class AuthRouter(BaseRouter):
    def __init__(self, prefix, ctrl):
        super().__init__(prefix, ctrl)
        self.setup_routes()
        
    def setup_routes(self) -> None:
        @self._router.post(HttpConstStrings.login_route)
        async def login(username: str, password: str):
            try:
                return self._ctrl.login(username, password)
            except HTTPException as e:
                raise e
        
        @self._router.post(HttpConstStrings.register_route)
        async def register(user : Auth):
            try:
                return self._ctrl.register(user)
            except HTTPException as e:
                raise e

