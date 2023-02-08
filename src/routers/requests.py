from fastapi import APIRouter,status, Response
from src.models.api import PublicRequestsAPI
from src.controllers import RequestLogic
from sqlalchemy import select
from src.clients import database

router = APIRouter(prefix="/request", tags=["Requests"])

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_request_endpoint(request_api_model: PublicRequestsAPI, response:Response):
    try:
        RequestLogic.create_request(request_api_model=request_api_model)
    except Exception as exc:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return str(exc)

#receber Lista de todos os pedidos
@router.get("/", status_code=status.HTTP_200_OK)
def get_all_requests_endpoint():
    result:list = RequestLogic.get_all()
    if not result:
        return "No Requests Registred"
    return result

@router.get("/{REQUEST_ID}", status_code=status.HTTP_200_OK)
def get_request_id_endpoint(REQUEST_ID:int):
    result:list = RequestLogic.get_single_request_id()
    return result
  
    
#receber Lista material disponivel , Id request
@router.get("", status_code=status.HTTP_200_OK)
def get_available_material_endpoint():
    pass

@router.patch("/{REQUEST_ID}", status_code=status.HTTP_202_ACCEPTED)
def update_request_id_endpoint():
    pass


