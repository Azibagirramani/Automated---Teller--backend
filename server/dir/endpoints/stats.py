from fastapi import APIRouter
from ..modules.stats.controllerStats import ControllerStats

endpoints = APIRouter()

@endpoints.get('/get_process_stats')
def get_stats():
    return ControllerStats().get_process_stats()