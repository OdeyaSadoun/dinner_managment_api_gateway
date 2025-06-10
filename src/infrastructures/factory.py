import os
from typing import List
from dotenv import load_dotenv

load_dotenv()  
from api.controllers.person_controller import PersonController
from api.routers.person_router import PersonRouter
from api.controllers.user_controller import UserController
from api.routers.user_router import UserRouter
from api.controllers.table_controller import TableController
from api.routers.table_router import TableRouter
from api.routers.base_router import BaseRouter
from api.controllers.print_sticker_controller import PrintStickerController
from api.routers.print_sticker_router import PrintStickerRouter
from globals.consts.http_const_strings import HttpConstStrings
from globals.consts.const_strings import ConstStrings
from infrastructures.interfaces.ihttp_server_manager import IHTTPServerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.managers.http_server_manager import HTTPServerManager
from models.managers.zmq_client_manager import ZMQClientManager


class Factory:
    def create_zmq_client() -> IZMQClientManager:
        host = os.getenv(ConstStrings.localhost_env_key)
        port = int(os.getenv(ConstStrings.business_logic_port_env_key))
        print(host, port)
        return ZMQClientManager(host, port)

    def create_user_router(zmq_client: IZMQClientManager) -> BaseRouter:
        user_controller = UserController(zmq_client)
        return UserRouter(HttpConstStrings.auth_prefix, user_controller)

    def create_person_router(zmq_client: IZMQClientManager) -> BaseRouter:
        person_controller = PersonController(zmq_client)
        return PersonRouter(HttpConstStrings.person_prefix, person_controller)

    def create_table_router(zmq_client: IZMQClientManager) -> BaseRouter:
        table_controller = TableController(zmq_client)
        return TableRouter(HttpConstStrings.table_prefix, table_controller)    
    
    def create_print_router() -> BaseRouter:
        print_controller = PrintStickerController()
        print("in factory")
        return PrintStickerRouter(HttpConstStrings.print_prefix, print_controller)

    def create_routes(zmq_client: IZMQClientManager) -> List[BaseRouter]:
        return [
            Factory.create_person_router(zmq_client),
            Factory.create_table_router(zmq_client),
            Factory.create_user_router(zmq_client),
            Factory.create_print_router()
        ]

    def create_http_server(routes: List[BaseRouter]) -> IHTTPServerManager:
        return HTTPServerManager(routes)

    def create_all() -> None:
        print(">>> Factory.create_all called")
        zmq_client = Factory.create_zmq_client()
        routes = Factory.create_routes(zmq_client)
        Factory.create_http_server(routes)