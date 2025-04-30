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
        async def register(user: User):
            try:
                return self._ctrl.register(user)
            except HTTPException as e:
                raise e

        @self._router.get(HttpConstStrings.get_all_users_route, dependencies=[Depends(JWTMiddleware(roles=["admin"]))])
        async def get_all_users():
            try:
                print("router")
                return self._ctrl.get_all_users()
            except HTTPException as e:
                raise e
            
        @self._router.get(HttpConstStrings.get_user_by_id_route)
        async def get_user_by_id(user_id: str):
            try:
                return self._ctrl.get_user_by_id(user_id)
            except HTTPException as e:
                raise e

        @self._router.get(HttpConstStrings.get_user_by_username_and_password_route, dependencies=[Depends(JWTMiddleware(roles=["admin"]))])
        async def get_user_by_username_and_password(username: str, password: str):
            try:
                return self._ctrl.get_user_by_username_and_password(username, password)
            except HTTPException as e:
                raise e

        @self._router.patch(HttpConstStrings.delete_user_route, dependencies=[Depends(JWTMiddleware(roles=["admin"]))])
        async def delete_user(user_id: str):
            try:
                print("user_id api", user_id)
                return self._ctrl.delete_user(user_id)
            except HTTPException as e:
                raise e

        @self._router.put(HttpConstStrings.update_user_route, dependencies=[Depends(JWTMiddleware(roles=["admin"]))])
        async def update_user(user_id: str, updated_user_data: dict):
            try:
                print("updated_user_data", updated_user_data)
                return self._ctrl.update_user(user_id, updated_user_data)
            except HTTPException as e:
                raise e
