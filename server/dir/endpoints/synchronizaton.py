from fastapi import APIRouter
from ..modules.synchronization.sync_splynx_customers_with_local import SplynxCustomersWithLocal
from sse_starlette.sse import EventSourceResponse

endpoints = APIRouter()



@endpoints.get("/synchronise_splynx_customers_to_localdatabase")
async def synchronise_splynx_customers_to_localdatabase():
    return EventSourceResponse(SplynxCustomersWithLocal.sync())

# @endpoints.get("/synchronise_localdatabase_to_paystack")
# async def synchronise_localdatabase_to_paystack():
#     return SplynxCustomersWithLocal.sync_localdatabase_to_paystack()