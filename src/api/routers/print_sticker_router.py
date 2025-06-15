from fastapi import Depends, HTTPException
from api.routers.base_router import BaseRouter
from api.middlewares.jwt_middlware import JWTMiddleware
from fastapi import Request  

from models.data_classes.participant_sticker import ParticipantSticker
from globals.consts.http_const_strings import HttpConstStrings


class PrintStickerRouter(BaseRouter):
    def __init__(self, prefix, ctrl):
        super().__init__(prefix, ctrl)
        self.setup_routes()
        
    def setup_routes(self) -> None:
        @self._router.post(HttpConstStrings.print_sticker_route)
        async def print_sticker(data: ParticipantSticker, request: Request):
            try:
                client_ip = request.client.host
                return self._ctrl.print_sticker(data, client_ip)
            except HTTPException as e:
                raise e


