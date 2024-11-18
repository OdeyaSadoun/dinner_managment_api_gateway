from api.controllers.person_controller import PersonController
from api.routers.person_router import PersonRouter
from api.controllers.auth_controller import AuthController
from api.routers.auth_router import AuthRouter
from api.controllers.table_controller import TableController
from api.routers.table_router import TableRouter
from globals.consts.consts import Consts
from globals.consts.const_strings import ConstStrings
from models.managers.http_server_manager import HTTPServerManager
from models.managers.zmq_client_manager import ZMQClientManager


class Factory:
    def create_zmq_client():
        return ZMQClientManager(ConstStrings.business_logic_host, Consts.business_logic_port)
    
    def create_person_router(zmq_client):
        person_controller = PersonController(zmq_client)
        return PersonRouter(ConstStrings.person_prefix, person_controller)
    
    def create_table_router(zmq_client):
        table_controller = TableController(zmq_client)
        return TableRouter(ConstStrings.table_prefix, table_controller)    
    
    def create_auth_router(zmq_client):
        auth_controller = AuthController(zmq_client)
        return AuthRouter(ConstStrings.auth_prefix, auth_controller)

    def create_routes(zmq_client):
        return [
            Factory.create_person_router(zmq_client),
            Factory.create_table_router(zmq_client),
            Factory.create_auth_router(zmq_client)
        ]
    
    def create_http_server(routes):
        return HTTPServerManager(routes)

    def create_all():
        zmq_client = Factory.create_zmq_client()
        routes = Factory.create_routes(zmq_client)
        Factory.create_http_server(routes)