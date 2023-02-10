from fastapi import APIRouter,status, Response
from src.models.api import PublicRequestsAPI, UpdateRequest
from src.controllers import RequestLogic

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
    result:list = RequestLogic.get_single_request_id(REQUEST_ID)
    return result

#receber Lista material disponivel 
@router.get("", status_code=status.HTTP_200_OK)
def get_available_material_endpoint():
    result:list = RequestLogic.get_all_available_material()
    if not result:
        return "No Items Available"
    return result

@router.patch("/{REQUEST_ID}", status_code=status.HTTP_202_ACCEPTED)
def update_request_id_endpoint(REQUEST_ID:int, request_api_model: UpdateRequest):
    result:list = RequestLogic.update_single_request_id(REQUEST_ID, request_api_model)
    if not result:
        return "Cant update request"
    return result




