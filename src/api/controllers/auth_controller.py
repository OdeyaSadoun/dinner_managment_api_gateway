from fastapi import HTTPException

from models.data_classes.auth import Auth
from globals.consts.consts import Consts
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from infrastructures.interfaces.icontroller_manager import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.zmq_request import Request
from models.data_classes.zmq_response import Response


class AuthController(IControllerManager):
    def __init__(self, zmq_client: IZMQClientManager) -> None:
        self._zmq_client = zmq_client

    def login(self, user: Auth):
        try:
            request = Request(
                resource=ZMQConstStrings.auth_resource,
                operation=ZMQConstStrings.login_operation,
                data={
                    ConstStrings.auth_key: user
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(status_code=Consts.error_status_code, detail=str(e))

    def register(self, user: Auth):
        try:
            request = Request(
                resource=ZMQConstStrings.auth_resource,
                operation=ZMQConstStrings.register_operation,
                data={
                    ConstStrings.auth_key: user
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(status_code=Consts.error_status_code, detail=str(e))
