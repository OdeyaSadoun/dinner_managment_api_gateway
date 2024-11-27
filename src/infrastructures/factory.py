import os
from typing import List

from api.controllers.person_controller import PersonController
from api.routers.person_router import PersonRouter
from api.controllers.auth_controller import AuthController
from api.routers.auth_router import AuthRouter
from api.controllers.table_controller import TableController
from api.routers.table_router import TableRouter
from api.routers.base_router import BaseRouter
from globals.consts.http_const_strings import HttpConstStrings
from globals.consts.const_strings import ConstStrings
from infrastructures.interfaces.ihttp_server_manager import IHTTPServerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.managers.http_server_manager import HTTPServerManager
from models.managers.zmq_client_manager import ZMQClientManager


class Factory:
    def create_zmq_client() -> IZMQClientManager:
        host = os.getenv(ConstStrings.business_logic_host_env_key)
        port = int(os.getenv(ConstStrings.business_logic_port_env_key))
        return ZMQClientManager(host, port)

    def create_auth_router(zmq_client: IZMQClientManager) -> BaseRouter:
        auth_controller = AuthController(zmq_client)
        return AuthRouter(HttpConstStrings.auth_prefix, auth_controller)

    def create_person_router(zmq_client: IZMQClientManager) -> BaseRouter:
        person_controller = PersonController(zmq_client)
        return PersonRouter(HttpConstStrings.person_prefix, person_controller)

    def create_table_router(zmq_client: IZMQClientManager) -> BaseRouter:
        table_controller = TableController(zmq_client)
        return TableRouter(HttpConstStrings.table_prefix, table_controller)

    def create_routes(zmq_client: IZMQClientManager) -> List[BaseRouter]:
        return [
            Factory.create_person_router(zmq_client),
            Factory.create_table_router(zmq_client),
            Factory.create_auth_router(zmq_client)
        ]

    def create_http_server(routes: List[BaseRouter]) -> IHTTPServerManager:
        return HTTPServerManager(routes)

    def create_all() -> None:
        zmq_client = Factory.create_zmq_client()
        routes = Factory.create_routes(zmq_client)
        Factory.create_http_server(routes)
