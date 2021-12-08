from fastapi import APIRouter
from ..modules.customers.controllers.controllerCustomer import ControllerCustomer
from typing import Optional
endpoints = APIRouter()


@endpoints.get("/customer-summary")
async def get_customer_summary():
    return ControllerCustomer().customerSummary()

@endpoints.get("/customers")
async def get_customers():
    return ControllerCustomer().controllerGetCustomers()


@endpoints.get("/customers/filter")
async def customers_by_filter(add_date: Optional[str] = None, status: Optional[str] = None, last_update: Optional[str] = None, billing_type: Optional[str] = None, search: Optional[str] = None):
    return ControllerCustomer().controllerCustomerFilter(add_date, status, last_update, billing_type, search)