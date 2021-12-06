from fastapi import APIRouter
from ..modules.stats.controllerStats import ControllerStats

endpoints = APIRouter()

@endpoints.get('/')
def get_stats():
    return ControllerStats().get_process_stats()

@endpoints.get('/get_process_stats')
def get_stats():
    return ControllerStats().get_thread_ids()