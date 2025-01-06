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
            print("login")
            request = Request(
                resource=ZMQConstStrings.auth_resource,
                operation=ZMQConstStrings.login_operation,
                data={
                    ConstStrings.user_key: user
                }
            )
            response =  self._zmq_client.send_request(request)
            
            print("response", response.data)
            print("check")
            print(response.status.value)
             # בדיקת סטטוס התגובה
            if response.status.value != "success":
                return response

            # יצירת טוקן JWT אם התגובה הצליחה
            # user_data = response.data.get(ConstStrings.user_key)
            print("user_data", response.data, response.data["username"], response.data.get("role"))
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
            print("token", token)
            # החזרת התגובה עם הטוקן
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
