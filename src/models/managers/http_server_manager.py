import os
from typing import List
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api.routers.base_router import BaseRouter
from globals.consts.const_strings import ConstStrings
from globals.consts.http_const_strings import HttpConstStrings
from globals.consts.consts import Consts
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
            allow_origins=[HttpConstStrings.all_sources], 
            allow_credentials=True,
            allow_methods=[HttpConstStrings.get_method, HttpConstStrings.post_method, HttpConstStrings.put_method, HttpConstStrings.delete_method, HttpConstStrings.patch_method], 
            allow_headers=[HttpConstStrings.all_sources],
        )

    def _run_server(self) -> None:
        uvicorn.run(self._app, host=os.getenv(ConstStrings.localhost_env_key), port=int(os.getenv(ConstStrings.http_port_evn_key)))