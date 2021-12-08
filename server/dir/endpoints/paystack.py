from fastapi import APIRouter
from ..modules.paystack.controllers.controllersPaystack import PaystackController

endpoints = APIRouter()



@endpoints.get("/")
def get_transactions():
    return PaystackController().get_transactions()


@endpoints.get("/settlements")
def get_settlements():
    return PaystackController().get_settlements()