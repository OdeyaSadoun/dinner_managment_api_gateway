from fastapi import HTTPException
from typing import Dict

from api.routers.base_router import BaseRouter
from models.data_classes.person import Person
from models.data_classes.zmq_response import Response
from infrastructures.interfaces.icontroller_manager import IControllerManager
from globals.consts.http_const_strings import HttpConstStrings


class PersonRouter(BaseRouter):
    def __init__(self, prefix: str, ctrl: IControllerManager):
        super().__init__(prefix, ctrl)
        self.setup_routes()

    def setup_routes(self) -> None:
        @self._router.get(HttpConstStrings.get_all_people_route)
        async def get_all_people() -> Response:
            try:
                return self._ctrl.get_all_people()
            except HTTPException as e:
                raise e

        @self._router.get(HttpConstStrings.get_person_by_id_route)
        async def get_person_by_id(person_id: str) -> Response:
            try:
                return self._ctrl.get_person_by_id(person_id)
            except HTTPException as e:
                raise e

        @self._router.post(HttpConstStrings.create_person_route)
        async def create_person(person: Person) -> Response:
            try:
                return self._ctrl.create_person(person)
            except HTTPException as e:
                raise e

        @self._router.put(HttpConstStrings.update_person_route)
        async def update_person(person_id: str, person: Person) -> Response:
            try:
                return self._ctrl.update_person(person_id, person)
            except HTTPException as e:
                raise e

        @self._router.patch(HttpConstStrings.seat_person_route)
        async def seat_person(person_id: str) -> Response:
            try:
                return self._ctrl.seat_person(person_id)
            except HTTPException as e:
                raise e

        @self._router.patch(HttpConstStrings.delete_person_route)
        async def delete_person(person_id: str) -> Response:
            try:
                return self._ctrl.delete_person(person_id)
            except HTTPException as e:
                raise e
