from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dir.endpoints import splynx, synchronizaton as operations, stats, customers as customerEndpoints

server = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


server.include_router(splynx.endpoints, tags=["splynx"])

server.include_router(operations.endpoints,  tags=["Operations"], prefix="/operations")
server.include_router(stats.endpoints,  tags=["Stats"])
server.include_router(customerEndpoints.endpoints,  tags=["Customers"] )