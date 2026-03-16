from sqlalchemy import Column, Integer, String
from database import Base
from fastapi import APIRouter, Query, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from modelos import modelo_producto
from esquema import eschema

router = APIRouter()


@router.get("/")
async def consultar():
    return "Consultar Alumnos del Programa...."


@router.get("/prod_all")
def get_users(db: Session = Depends(get_db)):
    producto = db.query(modelo_producto.Producto).all()
    return producto


@router.get("/prov_all")
def get_proveedores(db: Session = Depends(get_db)):
    proveedor = db.query(modelo_producto.Proveedor).all()
    return proveedor


@router.get("/prod/{prodId}")
def get_id(prodId: int, db: Session = Depends(get_db)):
    producto = db.query(modelo_producto.Producto).filter(
        modelo_producto.Producto.id_prod == prodId).first()
    if (producto):
        return producto
    else:
        raise HTTPException(
            status_code=404, detail=f"producto con id {prodId} no encontrado")


@router.get("/add")
def crearProducto(
    id_prod: int,
    nom_prod: str,
    proveedor: int,
    db: Session = Depends(get_db)
):
    productoAdd = modelo_producto.Producto(
        id_prod=id_prod,
        nombre=nom_prod,
        id_prov=proveedor
    )
    db.add(productoAdd)
    db.commit()
    db.refresh(productoAdd)
    return productoAdd


@router.put("/update/{id_prod}", response_model=eschema.productos)
async def update_Prod(id_prod: int, producs: eschema.productos, db: Session = Depends(get_db)):
    producto = db.query(modelo_producto.Producto).filter(
        modelo_producto.Producto.id_prod == id_prod
    ).first()
    if not producto:
        raise HTTPException(
            status_code=404, detail="Producto no encontrado....")
    producto.id_prod = producs.id_prod
    producto.nom_prod = producs.nom_prod
    producto.proveedor = producs.proveedor
    db.commit()
    db.refresh(producto)
    return producto


# metodo borrado
@router.delete("/borrar/{id_prod}")
async def borrarProd(id_prod: int, db: Session = Depends(get_db)):
    producto = db.query(modelo_producto.Producto).filter(
        modelo_producto.Producto.id_prod == id_prod
    ).first()
    if not producto:
        raise HTTPException(
            status_code=404, detail="Producto no encontrado....")
    db.delete(producto)
    db.commit()
    return f"El campo {id_prod} ha sido borrado"
