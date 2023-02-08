from fastapi import FastAPI
from src.routers import requests
from src.models import database
from src.controllers import RequestLogic

api = FastAPI()

routers = [
    requests.router,
]

for router in routers:
    api.include_router(router=router)

