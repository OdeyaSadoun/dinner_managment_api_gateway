from fastapi import Depends, File, HTTPException, UploadFile

from api.routers.base_router import BaseRouter
from api.middlewares.jwt_middlware import JWTMiddleware
from models.data_classes.add_and_remove_person_request import AddAndRemovePersonRequest
from models.data_classes.table import Table
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
            
        @self._router.post(HttpConstStrings.sync_tables_with_people_route)
        async def sync_tables_with_people():
            try:
                return self._ctrl.sync_tables_with_people()
            except HTTPException as e:
                raise e

        @self._router.get(HttpConstStrings.get_table_by_id_route)
        async def get_table_by_id(table_id: str):
            try:
                return self._ctrl.get_table_by_id(table_id)
            except HTTPException as e:
                raise e

        @self._router.post(HttpConstStrings.create_table_route, dependencies=[Depends(JWTMiddleware(roles=["admin"]))])
        async def create_table(table: Table):
            try:
                return self._ctrl.create_table(table)
            except HTTPException as e:
                raise e
        
        @self._router.patch(HttpConstStrings.update_table_position_route, dependencies=[Depends(JWTMiddleware(roles=["admin"]))])
        async def update_table_position(table_id: str, position: dict):
            try:
                return self._ctrl.update_table_position(table_id, position["position"])
            except HTTPException as e:
                raise e
            
        @self._router.post("/import_csv", dependencies=[Depends(JWTMiddleware(roles=["admin"]))])
        async def import_tables_from_csv(file: UploadFile = File(...)):
            try:
                return self._ctrl.import_tables_from_csv(file)
            except HTTPException as e:
                raise e
            
        @self._router.put(HttpConstStrings.update_table_route, dependencies=[Depends(JWTMiddleware(roles=["admin"]))])
        async def update_table(table_id: str, table: Table):
            try:
                return self._ctrl.update_table(table_id, table)
            except HTTPException as e:
                raise e

        @self._router.patch(HttpConstStrings.delete_table_route, dependencies=[Depends(JWTMiddleware(roles=["admin"]))])
        async def delete_table(table_id: str):
            try:
                return self._ctrl.delete_table(table_id)
            except HTTPException as e:
                raise e