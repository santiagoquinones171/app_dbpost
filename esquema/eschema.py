from pydantic import BaseModel
from typing import Optional

class productos(BaseModel):
    nom_prod: str
    proveedor: int

    class Config:
        from_attributes = True