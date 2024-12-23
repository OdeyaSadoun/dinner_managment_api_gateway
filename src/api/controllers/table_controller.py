from fastapi import HTTPException

from globals.consts.zmq_const_strings import ZMQConstStrings
from globals.consts.consts import Consts
from globals.consts.const_strings import ConstStrings
from infrastructures.interfaces.icontroller_manager import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.person import Person
from models.data_classes.table import Table
from models.data_classes.zmq_response import Response
from models.data_classes.zmq_request import Request


class TableController(IControllerManager):
    def __init__(self, zmq_client: IZMQClientManager) -> None:
        self._zmq_client = zmq_client

    def get_all_tables(self):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.get_all_tables_operation
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def get_table_by_id(self, table_id: str):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.get_table_by_id_operation,
                data={
                    ConstStrings.table_id_key: table_id
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def create_table(self, table: Table):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.create_table_operation,
                data={
                    ConstStrings.table_key: table
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def update_table(self, table_id: str, table: Table):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.update_table_operation,
                data={
                    ConstStrings.table_id_key: table_id,
                    ConstStrings.table_key: table
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def delete_table(self, table_id: str):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.delete_table_operation,
                data={
                    ConstStrings.table_id_key: table_id
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    # def add_person_to_table(self, table_id: str, person: Person):
    #     try:
    #         request = Request(
    #             resource=ZMQConstStrings.table_resource,
    #             operation=ZMQConstStrings.add_person_to_table_operation,
    #             data={
    #                 ConstStrings.table_id_key: table_id,
    #                 ConstStrings.person_key: person
    #             }
    #         )
    #         return self._zmq_client.send_request(request)
    #     except Exception as e:
    #         raise HTTPException(
    #             status_code=Consts.error_status_code, detail=str(e))
