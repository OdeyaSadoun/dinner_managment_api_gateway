from fastapi import HTTPException

from api.routers.base_router import BaseRouter
from models.data_classes.add_and_remove_person_request import AddAndRemovePersonRequest
from models.data_classes.person import Person
from models.data_classes.table import Table
from models.data_classes.zmq_response import Response
from globals.consts.http_const_strings import HttpConstStrings


class TableRouter(BaseRouter):
    def __init__(self, prefix, ctrl):
        super().__init__(prefix, ctrl)
        self.setup_routes()
        
    def setup_routes(self) -> None:
        @self._router.get(HttpConstStrings.get_all_tables_route)
        async def get_all_tables():
            try:
                return self._ctrl.get_all_tables()
            except HTTPException as e:
                raise e

        @self._router.get(HttpConstStrings.get_table_by_id_route)
        async def get_table_by_id(table_id: str):
            try:
                return self._ctrl.get_table_by_id(table_id)
            except HTTPException as e:
                raise e

        @self._router.post(HttpConstStrings.create_table_route)
        async def create_table(table: Table):
            try:
                return self._ctrl.create_table(table)
            except HTTPException as e:
                raise e
        
        @self._router.patch(HttpConstStrings.update_table_position_route)
        async def update_table_position(table_id: str, position: dict):
            try:
                print(position)
                print(position["position"])
                return self._ctrl.update_table_position(table_id, position["position"])
            except HTTPException as e:
                raise e

        @self._router.patch(HttpConstStrings.remove_person_from_table_route)
        async def remove_person_from_table(table_id: str, request: AddAndRemovePersonRequest):
            try:
                return self._ctrl.remove_person_from_table(table_id, request.person_id)
            except HTTPException as e:
                raise e
            
        @self._router.patch(HttpConstStrings.add_person_to_table_route)
        async def add_person_to_table(table_id: str, request: AddAndRemovePersonRequest):
            try:
                return self._ctrl.add_person_to_table(table_id, request.person_id)
            except HTTPException as e:
                raise e

        # @self._router.put(HttpConstStrings.update_table_route)
        # async def update_table(table_id: str, table: Table):
        #     try:
        #         return self._ctrl.update_table(table_id, table)
        #     except HTTPException as e:
        #         raise e

        @self._router.patch(HttpConstStrings.delete_table_route)
        async def delete_table(table_id: str):
            try:
                return self._ctrl.delete_table(table_id)
            except HTTPException as e:
                raise e

        # @self._router.patch(HttpConstStrings.add_person_to_table_route)
        # async def add_person_to_table(table_id: str,  person: Person):
        #     try:
        #         return self._ctrl.add_person_to_table(table_id, person)
        #     except HTTPException as e:
        #         raise e