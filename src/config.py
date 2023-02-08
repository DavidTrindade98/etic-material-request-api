from pydantic import BaseSettings

class Settings(BaseSettings):

    database_connection: str = "mysql://root:admin@db/etic_material_request_api_db"
