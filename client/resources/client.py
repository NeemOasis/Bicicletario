from pydantic import BaseModel
from typing import Optional

class Client(BaseModel):
    name: str
    rg: str
    cpf: str
    email: str
    tel: str
    address: str
    birth_date: str
    id: Optional[int] = None

class Cliente(BaseModel):
    nome: str
    rg: str
    cpf: str
    email: str
    telefone: str
    endereco: str
    data_nascimento: str