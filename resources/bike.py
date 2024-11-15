from enum import Enum
from pydantic import BaseModel

class BikeStatus(Enum):
    INSERT = 'cadastrada'
    ENTRY = 'entrada'
    REMOVAL = 'retirada'
    NOT_VALID = 'invalida'

class Bike(BaseModel):
    id_bike: int
    aro: str
    condicao: str
    id_cliente: str
    status_bike: str
