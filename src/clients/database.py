from src.models.database import PublicRequestsDB, PublicInventoryDB, PublicRequestsInventoryDB
from src.models.database import engine
from src.models.api import PublicRequestsAPI, UpdateRequest
from sqlalchemy.orm import Session
from dataclasses import asdict
from sqlalchemy import select, update
import json

def create_request(public_requests_api_Model:PublicRequestsAPI):
    with Session(engine) as session:
        new_request = PublicRequestsDB(**public_requests_api_Model.dict())
        session.add(new_request)
        session.commit()

def get_all_requests():
    with Session(engine) as db:
        query = select(PublicRequestsDB)
        result = db.scalars(query).all()
    return list(result)

def get_request_id(REQUEST_ID:int)->PublicRequestsDB:
    with Session(engine) as db:
        query = select(PublicRequestsDB).where(PublicRequestsDB.id == REQUEST_ID)
        result = db.scalars(query).one()
    if not result:
        raise Exception("request does not exist")
    return result

#atualizar campo delivered
# buscar todas as
# update table

def update_request_id(REQUEST_ID:int, public_requests_api_Model:UpdateRequest)->PublicRequestsDB:
    with Session(engine) as db:
        query = select(PublicRequestsDB).where(PublicRequestsDB.id == REQUEST_ID)
        old_request = db.scalars(query).one()
        
        update_request = UpdateRequest(**public_requests_api_Model.dict())

        if update_request.requester != str(getattr(old_request, "requester")):
            setattr(old_request, "requester", update_request.requester)
        
        if update_request.end_datetime != str(getattr(old_request, "end_datetime")):
            setattr(old_request, "end_datetime", update_request.end_datetime)

        if update_request.subject != str(getattr(old_request, "subject")):
            setattr(old_request, "subject", update_request.subject)

        if update_request.observations != str(getattr(old_request, "observations")):
            setattr(old_request, "observations", update_request.observations)

        db.add(old_request)
        db.commit()
        db.refresh(old_request)

        return old_request

#material requisitado nao estar delivered
#filtrar sku para ver se é maior que 0
#select inventory 
#select public_requests_inventory 
#where delivered ( entregar a escola )
# count delivered < sku ( nao esta disponivel )

def get_avaliable_material():
    with Session(engine) as db:
        query = select(PublicInventoryDB).where(PublicInventoryDB.sku > 0)
        result = db.scalars(query).all()
    return list(result)

        
