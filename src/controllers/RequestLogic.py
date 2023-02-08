from src.clients import database
from src.models.api import PublicRequestsAPI


def create_request(request_api_model: PublicRequestsAPI):
    database.create_request(request_api_model)

def get_all():
    return database.get_all_requests()

def get_single_request_id(REQUEST_ID):
    return database.get_request_id(REQUEST_ID)

def update_single_request_id(REQUEST_ID):
    return database.update_request_id(REQUEST_ID)

def get_all_available_material():
    return database.get_avaliable_material()