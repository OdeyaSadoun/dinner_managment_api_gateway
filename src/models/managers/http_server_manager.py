from typing import List
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api.routers.base_router import BaseRouter
from globals.consts.consts import Consts
from globals.consts.const_strings import ConstStrings
from infrastructures.interfaces.ihttp_server_manager import IHTTPServerManager


class HTTPServerManager(IHTTPServerManager):
    def __init__(self, routers: List[BaseRouter]) -> None:
        self._app = FastAPI()
        self._router = APIRouter()
        self._routers = routers
        self._include_routers()
        self._add_cors_middleware()
        self._run_server()

    def _include_routers(self) -> None:
        for router in self._routers:
            self._app.include_router(router.get_router(), prefix=router.prefix)

    def _add_cors_middleware(self) -> None:
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=[ConstStrings.all_sources], 
            allow_credentials=True,
            allow_methods=[ConstStrings.get_method, ConstStrings.post_method, ConstStrings.put_method, ConstStrings.delete_method, ConstStrings.patch_method], 
            allow_headers=[ConstStrings.all_sources],
        )

    def _run_server(self) -> None:
        uvicorn.run(self._app, host=ConstStrings.localhost, port=Consts.port)