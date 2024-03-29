from fastapi import APIRouter
from ..modules.splynx.controllers.splynx import Splynx

endpoints = APIRouter()




@endpoints.get("/splynx")
async def get_customers():
    return Splynx.get_customers()

@endpoints.get("/splynx-transactions")
async def endpoint_transactios():
    return Splynx.get_transactions()