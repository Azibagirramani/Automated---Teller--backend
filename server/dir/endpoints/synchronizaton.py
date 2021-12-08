from fastapi import APIRouter
from ..modules.synchronization.sync_splynx_customers_with_local import SyncSplynxCustomersWithLocal
from sse_starlette.sse import EventSourceResponse
endpoints = APIRouter()



@endpoints.get("/synchronise_splynx_customers_to_localdatabase")
async def synchronise_splynx_customers_to_localdatabase():
    return SyncSplynxCustomersWithLocal().sync()
