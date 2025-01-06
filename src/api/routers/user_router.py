from fastapi import Depends, HTTPException
from api.routers.base_router import BaseRouter

from api.middlewares.jwt_middlware import JWTMiddleware
from models.data_classes.login_user import LoginUser
from models.data_classes.user import User
from globals.consts.http_const_strings import HttpConstStrings


class UserRouter(BaseRouter):
    def __init__(self, prefix, ctrl):
        super().__init__(prefix, ctrl)
        self.setup_routes()
        
    def setup_routes(self) -> None:
        @self._router.post(HttpConstStrings.login_route)
        async def login(user: LoginUser):
            try:
                return self._ctrl.login(user)
            except HTTPException as e:
                raise e
        
        @self._router.post(HttpConstStrings.register_route, dependencies=[Depends(JWTMiddleware(roles=["admin"]))])
        async def register(user : User):
            try:
                return self._ctrl.register(user)
            except HTTPException as e:
                raise e

