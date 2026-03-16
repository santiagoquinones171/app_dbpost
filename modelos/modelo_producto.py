from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Proveedor(Base):
    __tablename__ = "proveedor"  

    id_prov = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    gmail = Column(String(100))

class Producto(Base):
    __tablename__ = "producto"    

    id_prod = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    id_prov = Column(Integer, ForeignKey("proveedor.id_prov"))  



