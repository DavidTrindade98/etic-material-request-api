from src.clients import database
from src.models.api import PublicRequestsAPI


def create_request(request_api_model: PublicRequestsAPI):
    database.create_request(request_api_model)

def get_all():
    return database.get_all_requests()