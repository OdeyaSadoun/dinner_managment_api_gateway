import os
import threading
from typing import List
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from uvicorn import Config, Server

load_dotenv()  
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
        print("ROUTERS:", self._routers)
        for router in self._routers:
            self._app.include_router(router.get_router(), prefix=router.prefix)

    def _add_cors_middleware(self) -> None:
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=[HttpConstStrings.all_sources], 
            allow_credentials=True,
            allow_methods=[HttpConstStrings.all_sources], 
            allow_headers=[HttpConstStrings.all_sources],
        )
        

    def _run_server(self) -> None:
        host = os.getenv(ConstStrings.host_env_key)
        port = int(os.getenv(ConstStrings.http_port_evn_key))
        print(f"run server on {host}:{port}")

        config = Config(app=self._app, host=host, port=port, log_level="info")
        server = Server(config)

        server.run()
