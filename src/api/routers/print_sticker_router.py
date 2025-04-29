from fastapi import Depends, HTTPException
from api.routers.base_router import BaseRouter
from api.middlewares.jwt_middlware import JWTMiddleware

from models.data_classes.participant_sticker import ParticipantSticker
from globals.consts.http_const_strings import HttpConstStrings


class PrintStickerRouter(BaseRouter):
    def __init__(self, prefix, ctrl):
        super().__init__(prefix, ctrl)
        self.setup_routes()
        
    def setup_routes(self) -> None:
        @self._router.get(HttpConstStrings.print_sticker_route)
        async def print_sticker():
            try:
                print("route")
                return self._ctrl.print_sticker()
            except HTTPException as e:
                raise e