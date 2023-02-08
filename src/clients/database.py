from src.models.database import PublicRequestsDB, PublicRequestsInventoryDB
from src.models.database import engine
from src.models.api import PublicRequestsAPI
from sqlalchemy.orm import Session
from dataclasses import asdict
from sqlalchemy import select

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
        result = db.scalar(query).one()
    if not result:
        raise Exception("request does not exist")
    return list(result)

def update_request_id():
    pass

