from pydantic import BaseModel
from typing import Optional

class Movement(BaseModel):
    id_movimentacao: int
    id_bike: int
    data_entrada: str
    data_saida: Optional[str] = None
