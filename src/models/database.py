from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import String, Column,Integer, ForeignKey, DateTime, Enum
from sqlalchemy import create_engine
from src.config import Settings
import enum

engine = create_engine(Settings().database_connection)

BaseDatabaseModel = declarative_base()

class Context(enum.Enum):
    Curricular = "Curricular"
    Extracurricular = "Extracurricular"

class PublicRequestsDB(BaseDatabaseModel):
    __tablename__ = "public_requests"

    id = Column(Integer, primary_key=True)
    school_class = Column(String(100))
    requester = Column(String(100))
    start_datetime = Column(DateTime)
    end_datetime = Column(DateTime)
    subject = Column(String(100))
    context = Column(Enum(Context))
    observations = Column(String(100) , nullable=True)

class PublicInventoryGroupDB(BaseDatabaseModel):
    __tablename__ = "public_inventory_group"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class PublicInventoryCategoryDB(BaseDatabaseModel):
    __tablename__ = "public_inventory_category"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("public_inventory_group.id"))
    name = Column(String(100))

class PublicInventoryDB(BaseDatabaseModel):
    __tablename__ = "public_inventory"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    category = Column(Integer, ForeignKey("public_inventory_category.id"))
    sku = Column(Integer)


class PublicRequestsInventoryDB(BaseDatabaseModel):
    __tablename__ = "public_requests_inventory"

    request_id = Column(Integer, ForeignKey("public_requests.id"), primary_key= True)
    material_requested_id = Column(Integer, ForeignKey("public_inventory.id"))
    requested = Column(DateTime)
    delivered = Column(DateTime)

BaseDatabaseModel.metadata.create_all(engine)