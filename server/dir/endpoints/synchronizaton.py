from fastapi import APIRouter
from ..modules.synchronization.sync_splynx_customers_with_local import SplynxCustomersWithLocal


endpoints = APIRouter()



@endpoints.get("/")
async def synchronise_splynx_customers_to_localdatabase():
    return SplynxCustomersWithLocal.sync()


@endpoints.get("/synchronise_splynx_customers_to_localdatabase")
async def test_deuplicates():
    return SplynxCustomersWithLocal.remove_duplicates()


@endpoints.get("/synchronise_localdatabase_to_paystack")
async def synchronise_localdatabase_to_paystack():
    return SplynxCustomersWithLocal.sync_localdatabase_to_paystack()