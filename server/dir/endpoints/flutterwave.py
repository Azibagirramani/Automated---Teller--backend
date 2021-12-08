from fastapi import APIRouter
from ..modules.flutterwave.controllers.flutterwaveController import FlutterwaveController

endpoints = APIRouter()

@endpoints.get("/transactions")
async def get_transactions():
    return FlutterwaveController().get_flutterwave_transactions()


@endpoints.get("/settlements")
async def get_settlements():
    return FlutterwaveController().get_flutterwave_settlements()