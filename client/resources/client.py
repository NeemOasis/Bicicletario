from pydantic import BaseModel

class Client(BaseModel):
    nome: str
    rg: str
    cpf: str
    email: str
    telefone: str
    endereco: str
    data_nascimento: str