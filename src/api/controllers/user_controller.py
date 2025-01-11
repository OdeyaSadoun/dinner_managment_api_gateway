from datetime import datetime, timedelta
import os
from fastapi import HTTPException
from jwt import encode

from globals.enums.response_status import ResponseStatus
from models.data_classes.zmq_response import Response
from models.data_classes.login_user import LoginUser
from models.data_classes.user import User
from globals.consts.consts import Consts
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from infrastructures.interfaces.icontroller_manager import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.zmq_request import Request


class UserController(IControllerManager):
    def __init__(self, zmq_client: IZMQClientManager) -> None:
        self._zmq_client = zmq_client

    def login(self, user: LoginUser):
        try:
            request = Request(
                resource=ZMQConstStrings.auth_resource,
                operation=ZMQConstStrings.login_operation,
                data={
                    ConstStrings.user_key: user
                }
            )
            response = self._zmq_client.send_request(request)
            if response.status.value != "success":
                return response

            exp = datetime.utcnow() + timedelta(hours=1)  # תוקף לשעה
            token = encode(
                {
                    "username": response.data.get("username"),
                    "role": response.data.get("role"),  
                    "exp": int(exp.timestamp()), 
                },
                os.getenv("JWT_SECRET"),
                algorithm=os.getenv("JWT_ALGORITHM")
            )
            return Response(
                status=ResponseStatus.SUCCESS,
                data={
                    ConstStrings.username_key: response.data.get("username"),
                    ConstStrings.token_key: token
                }
            )

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def register(self, user: User):
        try:
            request = Request(
                resource=ZMQConstStrings.auth_resource,
                operation=ZMQConstStrings.register_operation,
                data={
                    ConstStrings.user_key: user
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(status_code=Consts.error_status_code, detail=str(e))

    def get_all_users(self):
        try:
            print("ctrl")
            request = Request(
                resource=ZMQConstStrings.auth_resource,
                operation=ZMQConstStrings.get_all_users_operation,
                data={}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(status_code=Consts.error_status_code, detail=str(e))

    def get_user_by_id(self, user_id: str):
        try:
            request = Request(
                resource=ZMQConstStrings.auth_resource,
                operation=ZMQConstStrings.get_user_by_id_operation,
                data={
                    ConstStrings.user_id_key: user_id
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(status_code=Consts.error_status_code, detail=str(e))

    def get_user_by_username_and_password(self, username: str, password: str):
        try:
            request = Request(
                resource=ZMQConstStrings.auth_resource,
                operation=ZMQConstStrings.get_user_by_username_and_password_operation,
                data={
                    ConstStrings.username_key: username,
                    ConstStrings.password_key: password
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(status_code=Consts.error_status_code, detail=str(e))

    def delete_user(self, user_id: str):
        try:
            request = Request(
                resource=ZMQConstStrings.auth_resource,
                operation=ZMQConstStrings.delete_user_operation,
                data={
                    ConstStrings.user_id_key: user_id
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(status_code=Consts.error_status_code, detail=str(e))

    def update_user(self, user_id: str, updated_user_data: dict):
        try:
            request = Request(
                resource=ZMQConstStrings.auth_resource,
                operation=ZMQConstStrings.update_user_operation,
                data={
                    ConstStrings.user_id_key: user_id,
                    ConstStrings.user_key: updated_user_data
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(status_code=Consts.error_status_code, detail=str(e))
