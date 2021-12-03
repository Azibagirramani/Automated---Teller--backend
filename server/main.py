from fastapi import FastAPI

from dir.endpoints import splynx, synchronizaton

server = FastAPI()

server.include_router(splynx.endpoints, tags=["splynx"])
server.include_router(synchronizaton.endpoints,  tags=["Operations"])