from src.models.database import PublicRequestsDB, PublicInventoryDB, PublicRequestsInventoryDB
from src.models.database import engine
from src.models.api import PublicRequestsAPI
from sqlalchemy.orm import Session
from dataclasses import asdict
from sqlalchemy import select, update

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
def update_request_id(REQUEST_ID:int)->PublicRequestsDB:
    with Session(engine) as db:
        query = select(PublicRequestsDB).where(PublicRequestsDB.id == REQUEST_ID)
        result = db.scalars(query).one()
    if not result:
        raise Exception("cant update request")
    return result

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

        
