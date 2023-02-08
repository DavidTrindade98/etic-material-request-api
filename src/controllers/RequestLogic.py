from src.clients import database
from src.models.api import PublicRequestsAPI


def create_request(request_api_model: PublicRequestsAPI):
    database.create_request(request_api_model)

def get_request():
    return database.get_request_id()